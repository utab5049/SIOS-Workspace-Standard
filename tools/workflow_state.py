"""Local checkpoint state for safe workflow resume."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import tempfile
from typing import Any


class WorkflowStateError(ValueError):
    """Raised when workflow state cannot be safely read or written."""


def resolve_state_path(workflow_path: Path, value: str) -> Path:
    workflow_path = workflow_path.resolve()
    base = workflow_path.parent
    candidate = Path(value)
    if candidate.is_absolute():
        raise WorkflowStateError("state path must be relative to the workflow directory")
    resolved = (base / candidate).resolve()
    if resolved == base or base not in resolved.parents:
        raise WorkflowStateError("state path must stay inside the workflow directory")
    try:
        document = json.loads(workflow_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WorkflowStateError(f"could not read workflow for state safety check: {exc}") from exc
    protected = {workflow_path}
    if isinstance(document, dict):
        for key in ("manifest_path", "rules_path", "context_path"):
            value = document.get(key)
            if isinstance(value, str) and value.strip() and not Path(value).is_absolute():
                protected.add((base / value).resolve())
    if resolved in protected:
        raise WorkflowStateError("state path must not overwrite a workflow input file")
    if not resolved.parent.is_dir():
        raise WorkflowStateError("state directory must already exist")
    return resolved


def workflow_fingerprint(workflow_path: Path) -> str:
    """Hash the workflow definition and all three referenced input files."""
    workflow_path = workflow_path.resolve()
    try:
        document = json.loads(workflow_path.read_text(encoding="utf-8"))
        if not isinstance(document, dict):
            raise ValueError("workflow root must be an object")
        digest = hashlib.sha256()
        for key in ("workflow", "manifest_path", "rules_path", "context_path"):
            if key == "workflow":
                path = workflow_path
            else:
                value = document.get(key)
                if not isinstance(value, str) or not value.strip() or Path(value).is_absolute():
                    raise WorkflowStateError(f"cannot fingerprint invalid {key}")
                path = (workflow_path.parent / value).resolve()
                if workflow_path.parent not in path.parents or not path.is_file():
                    raise WorkflowStateError(f"cannot fingerprint unsafe or missing {key}")
            digest.update(key.encode("utf-8") + b"\0")
            digest.update(path.read_bytes())
            digest.update(b"\0")
        return digest.hexdigest()
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        if isinstance(exc, WorkflowStateError):
            raise
        raise WorkflowStateError(f"could not fingerprint workflow inputs: {exc}") from exc


def read_state(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WorkflowStateError(f"could not read state file: {exc}") from exc
    if not isinstance(value, dict) or value.get("state_schema_version") != "1.0":
        raise WorkflowStateError("state file has an unsupported or invalid structure")
    if not isinstance(value.get("status"), str) or not isinstance(value.get("fingerprint"), str):
        raise WorkflowStateError("state file requires status and fingerprint")
    return value


def write_state(path: Path, value: dict[str, Any]) -> None:
    """Atomically replace a checkpoint file in its existing directory."""
    temporary_name = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent,
            prefix=f".{path.name}.", suffix=".tmp", delete=False,
        ) as stream:
            temporary_name = stream.name
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_name, path)
    except OSError as exc:
        if temporary_name:
            try:
                os.unlink(temporary_name)
            except OSError:
                pass
        raise WorkflowStateError(f"could not write workflow state: {exc}") from exc

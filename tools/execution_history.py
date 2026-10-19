"""Append-only local execution history for SIOS workflow runs."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class HistoryWriteError(ValueError):
    """Raised when an execution history path is unsafe or cannot be written."""


def append_history(workflow_path: Path, history_value: str, entry: dict[str, Any]) -> Path:
    workflow_path = workflow_path.resolve()
    base = workflow_path.parent
    candidate = Path(history_value)
    if candidate.is_absolute():
        raise HistoryWriteError("history path must be relative to the workflow directory")
    resolved = (base / candidate).resolve()
    if resolved == base or base not in resolved.parents:
        raise HistoryWriteError("history path must stay inside the workflow directory")
    try:
        workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise HistoryWriteError(f"could not read workflow for history safety check: {exc}") from exc
    protected = {workflow_path}
    if isinstance(workflow, dict):
        for key in ("manifest_path", "rules_path", "context_path"):
            value = workflow.get(key)
            if isinstance(value, str) and value.strip() and not Path(value).is_absolute():
                protected.add((base / value).resolve())
    if resolved in protected:
        raise HistoryWriteError("history path must not overwrite a workflow input file")
    if not resolved.parent.is_dir():
        raise HistoryWriteError("history directory must already exist")
    try:
        with resolved.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(entry, ensure_ascii=False, separators=(",", ":")) + "\n")
    except OSError as exc:
        raise HistoryWriteError(f"could not append execution history: {exc}") from exc
    return resolved

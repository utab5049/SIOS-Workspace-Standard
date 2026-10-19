"""Run a small, declarative SIOS workflow with precondition gating."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from tools.registry_runtime import ManifestValidationError, RegistryRuntime
from tools.rules_engine import RulesConfigurationError, RulesEngine


class WorkflowConfigurationError(ValueError):
    """Raised when a workflow definition is malformed or unsafe."""


_ALLOWED_WORKFLOW_KEYS = {
    "schema_version", "workflow_id", "manifest_path", "rules_path",
    "context_path", "operation",
}
_ALLOWED_OPERATIONS = {"registry.list", "registry.get", "registry.search"}


def _resolve_file(base: Path, value: Any, label: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise WorkflowConfigurationError(f"{label} must be a non-empty relative path")
    candidate = Path(value)
    if candidate.is_absolute():
        raise WorkflowConfigurationError(f"{label} must be relative to the workflow file")
    root = base.resolve()
    resolved = (root / candidate).resolve()
    if resolved != root and root not in resolved.parents:
        raise WorkflowConfigurationError(f"{label} escapes the workflow directory")
    if not resolved.is_file():
        raise WorkflowConfigurationError(f"{label} does not point to an existing file: {value}")
    return resolved


def _load_json(path: Path, label: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WorkflowConfigurationError(f"could not read {label}: {exc}") from exc


def _validate_workflow(document: Any) -> dict[str, Any]:
    if not isinstance(document, dict):
        raise WorkflowConfigurationError("workflow must be a JSON object")
    unknown = set(document) - _ALLOWED_WORKFLOW_KEYS
    if unknown:
        raise WorkflowConfigurationError(f"unsupported workflow keys: {', '.join(sorted(unknown))}")
    required = ("schema_version", "workflow_id", "manifest_path", "rules_path", "context_path", "operation")
    for key in required:
        if key not in document:
            raise WorkflowConfigurationError(f"{key} is required")
    if document["schema_version"] != "1.0":
        raise WorkflowConfigurationError("schema_version must be '1.0'")
    if not isinstance(document["workflow_id"], str) or not document["workflow_id"].strip():
        raise WorkflowConfigurationError("workflow_id must be a non-empty string")
    operation = document["operation"]
    if not isinstance(operation, dict):
        raise WorkflowConfigurationError("operation must be an object")
    operation_type = operation.get("type")
    if not isinstance(operation_type, str) or operation_type not in _ALLOWED_OPERATIONS:
        raise WorkflowConfigurationError(f"unsupported operation type: {operation_type}")
    if set(operation) - {"type", "artifact_id", "query"}:
        raise WorkflowConfigurationError("operation contains unsupported arguments")
    if operation_type == "registry.get":
        if not isinstance(operation.get("artifact_id"), str) or not operation["artifact_id"].strip():
            raise WorkflowConfigurationError("registry.get requires a non-empty artifact_id")
        if "query" in operation:
            raise WorkflowConfigurationError("registry.get does not accept query")
    elif operation_type == "registry.search":
        if not isinstance(operation.get("query"), str):
            raise WorkflowConfigurationError("registry.search requires a string query")
        if "artifact_id" in operation:
            raise WorkflowConfigurationError("registry.search does not accept artifact_id")
    elif set(operation) != {"type"}:
        raise WorkflowConfigurationError("registry.list accepts only type")
    return document


def run_workflow(workflow_path: Path) -> dict[str, Any]:
    workflow_path = workflow_path.resolve()
    document = _validate_workflow(_load_json(workflow_path, "workflow"))
    base = workflow_path.parent
    rules_path = _resolve_file(base, document["rules_path"], "rules_path")
    context_path = _resolve_file(base, document["context_path"], "context_path")
    context = _load_json(context_path, "context")
    if not isinstance(context, dict):
        raise WorkflowConfigurationError("context JSON root must be an object")

    engine = RulesEngine.from_file(rules_path)
    gate = engine.evaluate(context)
    envelope: dict[str, Any] = {
        "workflow_id": document["workflow_id"],
        "status": "blocked" if gate["decision"] == "deny" else "completed",
        "gate": gate,
        "operation": {"type": document["operation"]["type"], "status": "not_run"},
    }
    # The registry is not loaded and the operation is not dispatched unless the gate allows it.
    if gate["decision"] == "deny":
        return envelope

    manifest_path = _resolve_file(base, document["manifest_path"], "manifest_path")
    runtime = RegistryRuntime.from_file(manifest_path)
    operation = document["operation"]
    if operation["type"] == "registry.list":
        value: Any = runtime.list_records()
    elif operation["type"] == "registry.get":
        value = runtime.get_by_id(operation["artifact_id"])
        if value is None:
            envelope["status"] = "operation_failed"
            envelope["operation"] = {
                "type": operation["type"], "status": "not_found",
                "artifact_id": operation["artifact_id"],
            }
            return envelope
    else:
        value = runtime.search(operation["query"])

    envelope["operation"] = {"type": operation["type"], "status": "completed", "result": value}
    return envelope


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a gated, read-only SIOS registry workflow.")
    parser.add_argument("workflow", type=Path, help="path to workflow definition JSON")
    args = parser.parse_args(argv)
    try:
        result = run_workflow(args.workflow)
    except (WorkflowConfigurationError, RulesConfigurationError, ManifestValidationError, OSError, TypeError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] == "blocked":
        return 2
    if result["status"] == "operation_failed":
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())

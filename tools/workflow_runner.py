"""Run a small, declarative SIOS workflow with precondition gating."""
from __future__ import annotations

import argparse
import json
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools.registry_runtime import ManifestValidationError, RegistryRuntime
from tools.rules_engine import RulesConfigurationError, RulesEngine
from tools.execution_history import HistoryWriteError, append_history
from tools.workflow_state import WorkflowStateError, read_state, resolve_state_path, workflow_fingerprint, write_state


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


def _write_report(workflow_path: Path, report_value: str, result: dict[str, Any]) -> Path:
    base = workflow_path.resolve().parent
    report = Path(report_value)
    if report.is_absolute():
        raise WorkflowConfigurationError("report path must be relative to the workflow directory")
    resolved = (base / report).resolve()
    if resolved == base or base not in resolved.parents:
        raise WorkflowConfigurationError("report path must stay inside the workflow directory")
    workflow_document = _load_json(workflow_path.resolve(), "workflow")
    protected = {workflow_path.resolve()}
    for key in ("manifest_path", "rules_path", "context_path"):
        value = workflow_document.get(key)
        if isinstance(value, str) and value.strip() and not Path(value).is_absolute():
            protected.add((base / value).resolve())
    if resolved in protected:
        raise WorkflowConfigurationError("report path must not overwrite a workflow input file")
    if not resolved.parent.is_dir():
        raise WorkflowConfigurationError("report directory must already exist")
    payload = {
        "report_schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "workflow_file": workflow_path.name,
        "result": result,
    }
    resolved.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return resolved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a gated, read-only SIOS registry workflow.")
    parser.add_argument("workflow", type=Path, help="path to workflow definition JSON")
    parser.add_argument("--report", help="optional report path relative to the workflow directory")
    parser.add_argument("--history", help="optional append-only JSONL history path relative to the workflow directory")
    parser.add_argument("--state", help="optional checkpoint file path relative to the workflow directory")
    parser.add_argument("--resume", action="store_true", help="reuse a matching completed result; requires --state")
    args = parser.parse_args(argv)
    if args.resume and not args.state:
        parser.error("--resume requires --state")

    started = time.perf_counter()
    run_id = str(uuid.uuid4())
    result: dict[str, Any] | None = None
    error_message: str | None = None
    state_path: Path | None = None
    fingerprint: str | None = None
    try:
        if args.state:
            state_path = resolve_state_path(args.workflow, args.state)
            fingerprint = workflow_fingerprint(args.workflow)
            prior_state = read_state(state_path)
            if args.resume and prior_state and prior_state.get("status") == "completed" and prior_state.get("fingerprint") == fingerprint:
                cached = prior_state.get("result")
                if not isinstance(cached, dict):
                    raise WorkflowStateError("completed state has no valid result")
                result = dict(cached)
                result["resumed"] = True
            else:
                write_state(state_path, {
                    "state_schema_version": "1.0",
                    "workflow_id": None,
                    "status": "running",
                    "fingerprint": fingerprint,
                    "started_at": datetime.now(timezone.utc).isoformat(),
                    "result": None,
                })
                result = run_workflow(args.workflow)
        else:
            result = run_workflow(args.workflow)
        if state_path and fingerprint and result is not None and not result.get("resumed"):
            write_state(state_path, {
                "state_schema_version": "1.0",
                "workflow_id": result.get("workflow_id"),
                "status": result.get("status", "error"),
                "fingerprint": fingerprint,
                "finished_at": datetime.now(timezone.utc).isoformat(),
                "result": result,
            })
        if args.report:
            report_path = _write_report(args.workflow, args.report, result)
            result["report_path"] = str(report_path.relative_to(args.workflow.resolve().parent))
    except (WorkflowConfigurationError, RulesConfigurationError, ManifestValidationError, WorkflowStateError, OSError, TypeError) as exc:
        error_message = str(exc)
        print(json.dumps({"status": "error", "error": error_message}, ensure_ascii=False, indent=2), file=sys.stderr)

    if args.history:
        operation = result.get("operation", {}) if result else {}
        gate = result.get("gate", {}) if result else {}
        entry = {
            "history_schema_version": "1.0",
            "run_id": run_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "workflow_id": result.get("workflow_id") if result else None,
            "status": "error" if error_message else (result.get("status", "error") if result else "error"),
            "duration_ms": round((time.perf_counter() - started) * 1000, 3),
            "gate_decision": gate.get("decision"),
            "operation_type": operation.get("type"),
            "operation_status": operation.get("status"),
            "error": error_message,
        }
        try:
            history_path = append_history(args.workflow, args.history, entry)
            entry["history_file"] = str(history_path.relative_to(args.workflow.resolve().parent))
        except (HistoryWriteError, OSError, TypeError) as exc:
            print(json.dumps({"status": "history_error", "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1

    if result is None or error_message is not None:
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] == "blocked":
        return 2
    if result["status"] == "operation_failed":
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Execute a gated, declarative multi-step read-only SIOS workflow."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
from datetime import datetime, timezone
from typing import Any

from tools.registry_runtime import ManifestValidationError, RegistryRuntime
from tools.rules_engine import RulesConfigurationError, RulesEngine


class MultiStepWorkflowError(ValueError):
    """Raised when a multi-step workflow is malformed or unsafe."""


_ALLOWED_OPERATIONS = {"registry.list", "registry.get", "registry.search"}
_CONDITION_OPERATORS = {"equals", "not_equals", "in", "contains", "exists", "truthy"}
_WORKFLOW_KEYS = {"schema_version", "workflow_id", "manifest_path", "rules_path", "context_path", "steps"}


def _load_json(path: Path, label: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise MultiStepWorkflowError(f"could not read {label}: {exc}") from exc


def _resolve_file(base: Path, value: Any, label: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise MultiStepWorkflowError(f"{label} must be a non-empty relative path")
    candidate = Path(value)
    if candidate.is_absolute():
        raise MultiStepWorkflowError(f"{label} must be relative to the workflow directory")
    root = base.resolve()
    resolved = (root / candidate).resolve()
    if resolved == root or root not in resolved.parents:
        raise MultiStepWorkflowError(f"{label} escapes the workflow directory")
    if not resolved.is_file():
        raise MultiStepWorkflowError(f"{label} does not point to an existing file: {value}")
    return resolved


def _is_reference(value: Any) -> bool:
    return (
        isinstance(value, dict) and set(value) == {"$ref"}
        and isinstance(value["$ref"], dict)
        and set(value["$ref"]) == {"step_id", "path"}
        and isinstance(value["$ref"]["step_id"], str) and bool(value["$ref"]["step_id"].strip())
        and isinstance(value["$ref"]["path"], str) and bool(value["$ref"]["path"].strip())
    )

def _validate_operation(operation: Any, step_id: str) -> dict[str, Any]:
    if not isinstance(operation, dict):
        raise MultiStepWorkflowError(f"step {step_id}: operation must be an object")
    kind = operation.get("type")
    if kind not in _ALLOWED_OPERATIONS:
        raise MultiStepWorkflowError(f"step {step_id}: unsupported operation type: {kind}")
    if set(operation) - {"type", "artifact_id", "query"}:
        raise MultiStepWorkflowError(f"step {step_id}: operation contains unsupported arguments")
    def valid(value: Any) -> bool:
        return (isinstance(value, str) and bool(value.strip())) or _is_reference(value)
    if kind == "registry.get":
        if not valid(operation.get("artifact_id")) or "query" in operation:
            raise MultiStepWorkflowError(f"step {step_id}: registry.get requires artifact_id only")
    elif kind == "registry.search":
        if not valid(operation.get("query")) or "artifact_id" in operation:
            raise MultiStepWorkflowError(f"step {step_id}: registry.search requires query only")
    elif set(operation) != {"type"}:
        raise MultiStepWorkflowError(f"step {step_id}: registry.list accepts only type")
    return operation

def _resolve_operation(step: dict[str, Any], prior_results: dict[str, dict[str, Any]]) -> dict[str, Any]:
    operation = dict(step["operation"])
    dependencies = set(step["depends_on"])
    for key, value in list(operation.items()):
        if key == "type" or not _is_reference(value):
            continue
        ref = value["$ref"]
        source_id = ref["step_id"]
        if source_id not in dependencies:
            raise MultiStepWorkflowError(
                f"step {step['step_id']}: reference source {source_id} must be a direct dependency"
            )
        current = _resolve_reference(ref, prior_results, step["step_id"])
        if not isinstance(current, str) or not current.strip():
            raise MultiStepWorkflowError(
                f"step {step['step_id']}: reference {source_id}.{ref['path']} must resolve to a non-empty string"
            )
        operation[key] = current
    return operation

def _validate_condition(condition: Any, step_id: str) -> dict[str, Any]:
    if not isinstance(condition, dict) or set(condition) - {"$ref", "operator", "value"}:
        raise MultiStepWorkflowError(f"step {step_id}: when must contain a reference, operator, and optional value")
    ref = condition.get("$ref")
    if not _is_reference({"$ref": ref}):
        raise MultiStepWorkflowError(f"step {step_id}: when.$ref must contain step_id and path")
    operator = condition.get("operator")
    if operator not in _CONDITION_OPERATORS:
        raise MultiStepWorkflowError(f"step {step_id}: unsupported condition operator: {operator}")
    if operator not in {"exists", "truthy"} and "value" not in condition:
        raise MultiStepWorkflowError(f"step {step_id}: when.value is required for {operator}")
    if operator == "exists" and "value" in condition and not isinstance(condition["value"], bool):
        raise MultiStepWorkflowError(f"step {step_id}: when.value must be boolean for exists")
    return condition


def _resolve_reference(ref: dict[str, Any], prior_results: dict[str, dict[str, Any]], step_id: str) -> Any:
    source_id, path = ref["step_id"], ref["path"]
    source = prior_results.get(source_id)
    if not isinstance(source, dict) or source.get("status") != "completed" or "result" not in source:
        raise MultiStepWorkflowError(f"step {step_id}: reference source {source_id} has no completed result")
    current: Any = source["result"]
    segments = path.split(".")
    if segments and segments[0] == "result":
        segments = segments[1:]
    for segment in segments:
        if isinstance(current, dict) and segment in current:
            current = current[segment]
        elif isinstance(current, list) and segment.isdigit() and int(segment) < len(current):
            current = current[int(segment)]
        else:
            raise MultiStepWorkflowError(f"step {step_id}: reference path {path!r} does not exist in {source_id}")
    return current


def _condition_matches(condition: dict[str, Any], prior_results: dict[str, dict[str, Any]], step_id: str) -> bool:
    try:
        actual = _resolve_reference(condition["$ref"], prior_results, step_id)
        exists = True
    except MultiStepWorkflowError:
        if condition["operator"] == "exists":
            return condition.get("value", True) is False
        return False
    operator, expected = condition["operator"], condition.get("value")
    if operator == "exists":
        return exists is expected if "value" in condition else exists
    if operator == "truthy":
        return bool(actual)
    if operator == "equals":
        return actual == expected
    if operator == "not_equals":
        return actual != expected
    if operator == "in":
        return isinstance(expected, list) and actual in expected
    if operator == "contains":
        if isinstance(actual, (str, list, tuple, dict)):
            try:
                return expected in actual
            except (TypeError, ValueError):
                return False
        return False
    return False


def _validate_workflow(document: Any) -> dict[str, Any]:
    if not isinstance(document, dict):
        raise MultiStepWorkflowError("workflow must be a JSON object")
    unknown = set(document) - _WORKFLOW_KEYS
    if unknown:
        raise MultiStepWorkflowError(f"unsupported workflow keys: {', '.join(sorted(unknown))}")
    for key in _WORKFLOW_KEYS:
        if key not in document:
            raise MultiStepWorkflowError(f"{key} is required")
    if document["schema_version"] != "1.0":
        raise MultiStepWorkflowError("schema_version must be '1.0'")
    if not isinstance(document["workflow_id"], str) or not document["workflow_id"].strip():
        raise MultiStepWorkflowError("workflow_id must be a non-empty string")
    steps = document["steps"]
    if not isinstance(steps, list) or not steps:
        raise MultiStepWorkflowError("steps must be a non-empty array")
    by_id: dict[str, dict[str, Any]] = {}
    for step in steps:
        if not isinstance(step, dict) or set(step) - {"step_id", "depends_on", "operation", "when"} or not {"step_id", "depends_on", "operation"} <= set(step):
            raise MultiStepWorkflowError("each step must contain only step_id, depends_on, and operation")
        step_id = step["step_id"]
        if not isinstance(step_id, str) or not step_id.strip():
            raise MultiStepWorkflowError("step_id must be a non-empty string")
        if step_id in by_id:
            raise MultiStepWorkflowError(f"duplicate step_id: {step_id}")
        deps = step["depends_on"]
        if not isinstance(deps, list) or any(not isinstance(dep, str) or not dep for dep in deps):
            raise MultiStepWorkflowError(f"step {step_id}: depends_on must be an array of step IDs")
        if len(set(deps)) != len(deps):
            raise MultiStepWorkflowError(f"step {step_id}: duplicate dependency")
        _validate_operation(step["operation"], step_id)
        if "when" in step:
            _validate_condition(step["when"], step_id)
        by_id[step_id] = step
    for step_id, step in by_id.items():
        for dep in step["depends_on"]:
            if dep not in by_id:
                raise MultiStepWorkflowError(f"step {step_id}: unknown dependency {dep}")
            if dep == step_id:
                raise MultiStepWorkflowError(f"step {step_id}: cannot depend on itself")
        for key, value in step["operation"].items():
            if key != "type" and _is_reference(value):
                source_id = value["$ref"]["step_id"]
                if source_id not in step["depends_on"]:
                    raise MultiStepWorkflowError(f"step {step_id}: reference source {source_id} must be a direct dependency")
        if "when" in step:
            source_id = step["when"]["$ref"]["step_id"]
            if source_id not in step["depends_on"]:
                raise MultiStepWorkflowError(f"step {step_id}: condition source {source_id} must be a direct dependency")
    # Stable topological sort: among ready steps, preserve declaration order.
    ordered: list[dict[str, Any]] = []
    done: set[str] = set()
    while len(ordered) < len(steps):
        ready = [step for step in steps if step["step_id"] not in done and set(step["depends_on"]) <= done]
        if not ready:
            raise MultiStepWorkflowError("step dependencies contain a cycle")
        for step in ready:
            ordered.append(step)
            done.add(step["step_id"])
    return {**document, "_ordered_steps": ordered}


def _fingerprint(workflow_path: Path, document: dict[str, Any]) -> str:
    digest = hashlib.sha256()
    base = workflow_path.parent
    for key in ("workflow", "manifest_path", "rules_path", "context_path"):
        path = workflow_path if key == "workflow" else _resolve_file(base, document[key], key)
        digest.update(key.encode() + b"\0" + path.read_bytes() + b"\0")
    return digest.hexdigest()


def _state_path(workflow_path: Path, value: str, document: dict[str, Any]) -> Path:
    base = workflow_path.parent.resolve()
    candidate = Path(value)
    if candidate.is_absolute():
        raise MultiStepWorkflowError("state path must be relative to the workflow directory")
    resolved = (base / candidate).resolve()
    if resolved == base or base not in resolved.parents:
        raise MultiStepWorkflowError("state path must stay inside the workflow directory")
    protected = {workflow_path.resolve()}
    for key in ("manifest_path", "rules_path", "context_path"):
        raw = document[key]
        if not Path(raw).is_absolute():
            protected.add((base / raw).resolve())
    if resolved in protected:
        raise MultiStepWorkflowError("state path must not overwrite workflow input files")
    if not resolved.parent.is_dir():
        raise MultiStepWorkflowError("state directory must already exist")
    return resolved


def _read_state(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    value = _load_json(path, "workflow state")
    if not isinstance(value, dict) or value.get("state_schema_version") != "2.0":
        raise MultiStepWorkflowError("state file has an unsupported or invalid structure")
    if not isinstance(value.get("steps"), dict) or not isinstance(value.get("fingerprint"), str):
        raise MultiStepWorkflowError("state file requires fingerprint and steps object")
    return value


def _write_state(path: Path, value: dict[str, Any]) -> None:
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                         prefix=f".{path.name}.", suffix=".tmp", delete=False) as stream:
            temp_name = stream.name
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    except OSError as exc:
        if temp_name:
            try:
                os.unlink(temp_name)
            except OSError:
                pass
        raise MultiStepWorkflowError(f"could not write workflow state: {exc}") from exc


def _dispatch(runtime: RegistryRuntime, operation: dict[str, Any]) -> tuple[str, Any]:
    kind = operation["type"]
    if kind == "registry.list":
        return "completed", runtime.list_records()
    if kind == "registry.get":
        value = runtime.get_by_id(operation["artifact_id"])
        return ("completed", value) if value is not None else ("not_found", None)
    return "completed", runtime.search(operation["query"])


def run_multi_step(workflow_path: Path, *, state_path: Path | None = None, resume: bool = False) -> dict[str, Any]:
    workflow_path = workflow_path.resolve()
    document = _validate_workflow(_load_json(workflow_path, "workflow"))
    base = workflow_path.parent
    rules_path = _resolve_file(base, document["rules_path"], "rules_path")
    context_path = _resolve_file(base, document["context_path"], "context_path")
    context = _load_json(context_path, "context")
    if not isinstance(context, dict):
        raise MultiStepWorkflowError("context JSON root must be an object")
    gate = RulesEngine.from_file(rules_path).evaluate(context)
    if gate["decision"] == "deny":
        return {
            "workflow_id": document["workflow_id"], "status": "blocked", "gate": gate,
            "steps": [{"step_id": step["step_id"], "status": "not_run", "outcome": "not_run"} for step in document["_ordered_steps"]],
        }

    # Only compute a fingerprint/read the manifest after the gate allows execution.
    fingerprint = _fingerprint(workflow_path, document)
    prior = _read_state(state_path) if state_path else None
    reusable = bool(resume and prior and prior.get("fingerprint") == fingerprint)
    step_results: dict[str, dict[str, Any]] = dict(prior.get("steps", {})) if reusable else {}
    manifest_path = _resolve_file(base, document["manifest_path"], "manifest_path")
    runtime = RegistryRuntime.from_file(manifest_path)
    final_status = "completed"
    ordered_results: list[dict[str, Any]] = []

    def checkpoint(status: str) -> None:
        if state_path:
            _write_state(state_path, {
                "state_schema_version": "2.0", "workflow_id": document["workflow_id"],
                "status": status, "fingerprint": fingerprint,
                "updated_at": datetime.now(timezone.utc).isoformat(), "steps": step_results,
            })

    checkpoint("running")
    for step in document["_ordered_steps"]:
        step_id = step["step_id"]
        deps = step["depends_on"]
        if any(step_results.get(dep, {}).get("status") != "completed" for dep in deps):
            item = {"step_id": step_id, "status": "skipped", "outcome": "skipped", "reason": "dependency_not_completed"}
            step_results[step_id] = item
            ordered_results.append(item)
            continue
        if "when" in step and not _condition_matches(step["when"], step_results, step_id):
            item = {"step_id": step_id, "status": "skipped", "outcome": "skipped", "reason": "condition_not_met"}
            step_results[step_id] = item
            ordered_results.append(item)
            checkpoint("running")
            continue
        cached = step_results.get(step_id)
        if reusable and isinstance(cached, dict) and cached.get("status") == "completed":
            item = {**cached, "resumed": True}
            ordered_results.append(item)
            continue
        try:
            resolved_operation = _resolve_operation(step, step_results)
            op_status, value = _dispatch(runtime, resolved_operation)
            item = {"step_id": step_id, "operation_type": step["operation"]["type"], "status": op_status}
            if op_status == "completed":
                item["result"] = value
                item["outcome"] = "empty" if isinstance(value, (list, dict, str)) and len(value) == 0 else "success"
            else:
                message = f"artifact not found: {step['operation']['artifact_id']}"
                item.update({
                    "outcome": "not_found",
                    "error": message,
                    "error_detail": {"code": "ARTIFACT_NOT_FOUND", "message": message, "retryable": False},
                })
                final_status = "operation_failed"
            step_results[step_id] = item
            ordered_results.append(item)
            checkpoint("running" if final_status == "completed" else final_status)
            if final_status != "completed":
                break
        except MultiStepWorkflowError as exc:
            item = {"step_id": step_id, "operation_type": step["operation"]["type"],
                    "status": "failed", "outcome": "failed", "error": str(exc),
                    "error_detail": {"code": "INVALID_STEP_INPUT", "message": str(exc), "retryable": False}}
            step_results[step_id] = item
            ordered_results.append(item)
            final_status = "operation_failed"
            checkpoint(final_status)
            break
        except (ManifestValidationError, OSError, TypeError, ValueError) as exc:
            item = {"step_id": step_id, "operation_type": step["operation"]["type"],
                    "status": "failed", "outcome": "failed", "error": str(exc),
                    "error_detail": {"code": "OPERATION_ERROR", "message": str(exc), "retryable": False}}
            step_results[step_id] = item
            ordered_results.append(item)
            final_status = "operation_failed"
            checkpoint(final_status)
            break
    completed_ids = {item["step_id"] for item in ordered_results}
    for step in document["_ordered_steps"]:
        if step["step_id"] not in completed_ids:
            item = {"step_id": step["step_id"], "status": "skipped", "outcome": "skipped", "reason": "workflow_stopped_after_failure"}
            ordered_results.append(item)
            step_results[step["step_id"]] = item
    checkpoint(final_status)
    return {"workflow_id": document["workflow_id"], "status": final_status, "gate": gate, "steps": ordered_results}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a gated, multi-step read-only SIOS workflow.")
    parser.add_argument("workflow", type=Path, help="path to multi-step workflow JSON")
    parser.add_argument("--state", help="optional checkpoint path relative to workflow directory")
    parser.add_argument("--resume", action="store_true", help="resume completed steps from a matching checkpoint; requires --state")
    args = parser.parse_args(argv)
    if args.resume and not args.state:
        parser.error("--resume requires --state")
    try:
        workflow_path = args.workflow.resolve()
        state_path = None
        if args.state:
            preliminary = _validate_workflow(_load_json(workflow_path, "workflow"))
            state_path = _state_path(workflow_path, args.state, preliminary)
        result = run_multi_step(workflow_path, state_path=state_path, resume=args.resume)
    except (MultiStepWorkflowError, RulesConfigurationError, ManifestValidationError, OSError, TypeError) as exc:
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

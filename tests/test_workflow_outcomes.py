"""Tests for normalized workflow step outcomes and error details."""
import json
from pathlib import Path
import tempfile
import unittest

from tools.multi_step_workflow import run_multi_step

def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


def setup_workflow(root, *, approved=True, steps=None):
    write_json(root / "manifest.json", {
        "schema_version": "1.0.0", "authority_state": "proposed",
        "source_document": "tests/synthetic-outcomes.md",
        "artifacts": [
            {"artifact_id": "DEMO-001", "status": "Frozen", "version": "1.0", "path": None,
             "record_state": "explicit", "source_location": "Fixture", "notes": ["alpha record"]},
            {"artifact_id": "DEMO-002", "status": "Draft", "version": "0.2", "path": None,
             "record_state": "explicit", "source_location": "Fixture", "notes": ["beta record"]},
        ],
    })
    write_json(root / "context.json", {"request": {"approved": approved}})
    write_json(root / "rules.json", {"schema_version": "1.0", "rules": [{
        "rule_id": "PRE-001", "field": "request.approved", "operator": "equals",
        "value": True, "message": "Approval is required",
    }]})
    write_json(root / "workflow.json", {
        "schema_version": "1.0", "workflow_id": "WF-OUTCOME-TEST",
        "manifest_path": "manifest.json", "rules_path": "rules.json", "context_path": "context.json",
        "steps": steps or [
            {"step_id": "list", "depends_on": [], "operation": {"type": "registry.list"}},
        ],
    })
    return root / "workflow.json"


class WorkflowOutcomeTests(unittest.TestCase):
    def test_empty_search_has_explicit_empty_outcome(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = setup_workflow(Path(directory), steps=[
                {"step_id": "search", "depends_on": [], "operation": {"type": "registry.search", "query": "no-such-record-token"}},
            ])
            result = run_multi_step(workflow)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["steps"][0]["status"], "completed")
        self.assertEqual(result["steps"][0]["outcome"], "empty")
        self.assertEqual(result["steps"][0]["result"], [])

    def test_missing_artifact_has_stable_non_retryable_error(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = setup_workflow(Path(directory), steps=[
                {"step_id": "get", "depends_on": [], "operation": {"type": "registry.get", "artifact_id": "NO-SUCH-ID"}},
            ])
            result = run_multi_step(workflow)
        step = result["steps"][0]
        self.assertEqual(step["outcome"], "not_found")
        self.assertEqual(step["error_detail"]["code"], "ARTIFACT_NOT_FOUND")
        self.assertFalse(step["error_detail"]["retryable"])
        self.assertEqual(step["error_detail"]["message"], step["error"])

    def test_invalid_data_binding_becomes_structured_step_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = setup_workflow(root, steps=[
                {"step_id": "search", "depends_on": [], "operation": {"type": "registry.search", "query": "alpha record"}},
                {"step_id": "get", "depends_on": ["search"], "operation": {"type": "registry.get", "artifact_id": {"$ref": {"step_id": "search", "path": "result.99.artifact_id"}}}},
                {"step_id": "after", "depends_on": ["get"], "operation": {"type": "registry.list"}},
            ])
            result = run_multi_step(workflow)
        self.assertEqual(result["status"], "operation_failed")
        self.assertEqual(result["steps"][1]["outcome"], "failed")
        self.assertEqual(result["steps"][1]["error_detail"]["code"], "INVALID_STEP_INPUT")
        self.assertFalse(result["steps"][1]["error_detail"]["retryable"])
        self.assertEqual(result["steps"][2]["outcome"], "skipped")
        self.assertEqual(result["steps"][2]["reason"], "dependency_not_completed")

    def test_gate_block_has_not_run_outcome(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = setup_workflow(Path(directory), approved=False)
            result = run_multi_step(workflow)
        self.assertEqual(result["steps"][0]["outcome"], "not_run")


if __name__ == "__main__":
    unittest.main()

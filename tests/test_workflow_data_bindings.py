"""Tests for explicit data references between multi-step workflow operations."""
import json
from pathlib import Path
import tempfile
import unittest

from tools.multi_step_workflow import MultiStepWorkflowError, run_multi_step


def put(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


class WorkflowDataBindingTests(unittest.TestCase):
    def fixture(self, root):
        put(root / "manifest.json", {
            "schema_version": "1.0.0", "authority_state": "proposed",
            "source_document": "synthetic-fixture.md",
            "artifacts": [
                {"artifact_id": "DEMO-001", "status": "Frozen", "version": "1.0", "path": None,
                 "record_state": "explicit", "source_location": "Example", "notes": ["binding test record"]},
                {"artifact_id": "DEMO-002", "status": "Draft", "version": "0.1", "path": None,
                 "record_state": "explicit", "source_location": "Example", "notes": ["second record"]},
            ],
        })
        put(root / "rules.json", {"schema_version": "1.0", "rules": []})
        put(root / "context.json", {})
        workflow = {
            "schema_version": "1.0", "workflow_id": "WF-BINDING-TEST",
            "manifest_path": "manifest.json", "rules_path": "rules.json", "context_path": "context.json",
            "steps": [
                {"step_id": "search", "depends_on": [], "operation": {"type": "registry.search", "query": "binding test"}},
                {"step_id": "get", "depends_on": ["search"], "operation": {
                    "type": "registry.get", "artifact_id": {"$ref": {"step_id": "search", "path": "result.0.artifact_id"}}
                }},
            ],
        }
        put(root / "workflow.json", workflow)
        return root / "workflow.json"

    def test_output_reference_feeds_next_operation(self):
        with tempfile.TemporaryDirectory() as temp:
            result = run_multi_step(self.fixture(Path(temp)))
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["steps"][1]["result"]["artifact_id"], "DEMO-001")

    def test_reference_must_use_direct_dependency(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            workflow = self.fixture(root)
            doc = json.loads(workflow.read_text(encoding="utf-8"))
            doc["steps"].append({
                "step_id": "third", "depends_on": [],
                "operation": {"type": "registry.get", "artifact_id": {
                    "$ref": {"step_id": "search", "path": "result.0.artifact_id"}
                }},
            })
            put(workflow, doc)
            with self.assertRaisesRegex(MultiStepWorkflowError, "direct dependency"):
                run_multi_step(workflow)

    def test_invalid_reference_path_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            workflow = self.fixture(root)
            doc = json.loads(workflow.read_text(encoding="utf-8"))
            doc["steps"][1]["operation"]["artifact_id"]["$ref"]["path"] = "result.99.artifact_id"
            put(workflow, doc)
            result = run_multi_step(workflow)
        self.assertEqual(result["status"], "operation_failed")
        self.assertEqual(result["steps"][1]["outcome"], "failed")
        self.assertEqual(result["steps"][1]["error_detail"]["code"], "INVALID_STEP_INPUT")
        self.assertIn("reference path", result["steps"][1]["error"])


if __name__ == "__main__":
    unittest.main()

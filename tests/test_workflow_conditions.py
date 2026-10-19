"""Tests for output-driven conditional workflow steps."""
import json
from pathlib import Path
import tempfile
import unittest

from tools.multi_step_workflow import MultiStepWorkflowError, run_multi_step


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


class ConditionalWorkflowTests(unittest.TestCase):
    def make_workflow(self, root, *, condition, steps=None):
        write_json(root / "manifest.json", {
            "schema_version": "1.0.0", "authority_state": "proposed",
            "source_document": "synthetic-test-fixture.md",
            "artifacts": [
                {"artifact_id": "DEMO-001", "status": "Frozen", "version": "1.0", "path": None,
                 "record_state": "explicit", "source_location": "Example", "notes": ["alpha marker"]},
                {"artifact_id": "DEMO-002", "status": "Draft", "version": "0.1", "path": None,
                 "record_state": "explicit", "source_location": "Example", "notes": ["beta marker"]},
            ],
        })
        write_json(root / "rules.json", {"schema_version": "1.0", "rules": []})
        write_json(root / "context.json", {})
        if steps is None:
            steps = [
                {"step_id": "search", "depends_on": [], "operation": {"type": "registry.search", "query": "alpha marker"}},
                {"step_id": "conditional_get", "depends_on": ["search"], "when": condition,
                 "operation": {"type": "registry.get", "artifact_id": {"$ref": {"step_id": "search", "path": "result.0.artifact_id"}}}},
                {"step_id": "independent_list", "depends_on": [], "operation": {"type": "registry.list"}},
            ]
        workflow = {
            "schema_version": "1.0", "workflow_id": "WF-CONDITION-TEST",
            "manifest_path": "manifest.json", "rules_path": "rules.json", "context_path": "context.json",
            "steps": steps,
        }
        write_json(root / "workflow.json", workflow)
        return root / "workflow.json"

    def test_condition_true_runs_step_and_resolves_input(self):
        with tempfile.TemporaryDirectory() as temp:
            workflow = self.make_workflow(Path(temp), condition={
                "$ref": {"step_id": "search", "path": "result.0.artifact_id"},
                "operator": "equals", "value": "DEMO-001",
            })
            result = run_multi_step(workflow)
        self.assertEqual(result["status"], "completed")
        conditional = next(item for item in result["steps"] if item["step_id"] == "conditional_get")
        self.assertEqual(conditional["status"], "completed")
        self.assertEqual(conditional["result"]["artifact_id"], "DEMO-001")

    def test_condition_false_skips_only_that_branch(self):
        with tempfile.TemporaryDirectory() as temp:
            workflow = self.make_workflow(Path(temp), condition={
                "$ref": {"step_id": "search", "path": "result.0.artifact_id"},
                "operator": "equals", "value": "DEMO-999",
            })
            result = run_multi_step(workflow)
        statuses = {item["step_id"]: item["status"] for item in result["steps"]}
        self.assertEqual(result["status"], "completed")
        self.assertEqual(statuses["conditional_get"], "skipped")
        self.assertEqual(statuses["independent_list"], "completed")

    def test_condition_source_must_be_direct_dependency(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            workflow = self.make_workflow(root, condition={
                "$ref": {"step_id": "search", "path": "result.0.artifact_id"},
                "operator": "truthy",
            })
            document = json.loads(workflow.read_text(encoding="utf-8"))
            document["steps"][1]["depends_on"] = []
            document["steps"][1]["operation"]["artifact_id"] = "DEMO-001"
            write_json(workflow, document)
            with self.assertRaisesRegex(MultiStepWorkflowError, "condition source.*direct dependency"):
                run_multi_step(workflow)

    def test_unknown_condition_operator_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            workflow = self.make_workflow(Path(temp), condition={
                "$ref": {"step_id": "search", "path": "result.0.artifact_id"},
                "operator": "execute",
            })
            with self.assertRaisesRegex(MultiStepWorkflowError, "unsupported condition operator"):
                run_multi_step(workflow)


if __name__ == "__main__":
    unittest.main()

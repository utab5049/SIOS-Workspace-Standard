"""Tests for local workflow checkpoint state and resume."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.workflow_runner import main
from tools.workflow_state import WorkflowStateError, resolve_state_path, workflow_fingerprint


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


class WorkflowStateTests(unittest.TestCase):
    def make_workflow(self, root):
        write_json(root / "manifest.json", {
            "schema_version": "1.0.0", "authority_state": "proposed",
            "source_document": "fixture.md",
            "artifacts": [{
                "artifact_id": "SIOS-001", "status": "Frozen", "version": "1.0",
                "path": None, "record_state": "explicit", "source_location": "Foundation",
                "notes": ["synthetic test record"],
            }],
        })
        write_json(root / "rules.json", {"schema_version": "1.0", "rules": [{
            "rule_id": "PRE-001", "field": "request.approved", "operator": "equals",
            "value": True, "message": "Approval required",
        }]})
        write_json(root / "context.json", {"request": {"approved": True}})
        write_json(root / "workflow.json", {
            "schema_version": "1.0", "workflow_id": "WF-STATE-TEST",
            "manifest_path": "manifest.json", "rules_path": "rules.json",
            "context_path": "context.json", "operation": {"type": "registry.list"},
        })
        return root / "workflow.json"

    def test_completed_state_can_be_resumed_without_reexecuting_operation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.make_workflow(root)
            state = "workflow-state.json"
            with patch("sys.stdout"):
                self.assertEqual(main([str(workflow), "--state", state]), 0)
            with patch("tools.workflow_runner.run_workflow", side_effect=AssertionError("must not rerun")), patch("sys.stdout"):
                self.assertEqual(main([str(workflow), "--state", state, "--resume"]), 0)

    def test_changed_context_invalidates_resume(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.make_workflow(root)
            with patch("sys.stdout"):
                self.assertEqual(main([str(workflow), "--state", "state.json"]), 0)
            write_json(root / "context.json", {"request": {"approved": False}})
            with patch("sys.stdout"):
                self.assertEqual(main([str(workflow), "--state", "state.json", "--resume"]), 2)
            state = json.loads((root / "state.json").read_text(encoding="utf-8"))
            self.assertEqual(state["status"], "blocked")

    def test_state_path_cannot_overwrite_inputs_or_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.make_workflow(root)
            with self.assertRaisesRegex(WorkflowStateError, "overwrite"):
                resolve_state_path(workflow, "context.json")
            with self.assertRaisesRegex(WorkflowStateError, "stay inside"):
                resolve_state_path(workflow, "../outside.json")

    def test_fingerprint_changes_when_context_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.make_workflow(root)
            before = workflow_fingerprint(workflow)
            write_json(root / "context.json", {"request": {"approved": False}})
            self.assertNotEqual(before, workflow_fingerprint(workflow))


if __name__ == "__main__":
    unittest.main()

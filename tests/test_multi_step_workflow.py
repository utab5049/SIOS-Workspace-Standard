"""Tests for the gated multi-step read-only workflow engine."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.multi_step_workflow import MultiStepWorkflowError, main, run_multi_step


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


def setup_workflow(root, *, approved=True, steps=None):
    write_json(root / "manifest.json", {
        "schema_version": "1.0.0", "authority_state": "proposed",
        "source_document": "tests/fixture-source.md",
        "artifacts": [
            {"artifact_id": "DEMO-001", "status": "Frozen", "version": "1.0", "path": None,
             "record_state": "explicit", "source_location": "Foundation", "notes": ["alpha record"]},
            {"artifact_id": "DEMO-002", "status": "Draft", "version": "0.2", "path": None,
             "record_state": "explicit", "source_location": "Runtime", "notes": ["beta record"]},
        ],
    })
    write_json(root / "context.json", {"request": {"approved": approved}})
    write_json(root / "rules.json", {"schema_version": "1.0", "rules": [{
        "rule_id": "PRE-001", "field": "request.approved", "operator": "equals",
        "value": True, "message": "Approval is required",
    }]})
    write_json(root / "workflow.json", {
        "schema_version": "1.0", "workflow_id": "WF-MULTI-TEST",
        "manifest_path": "manifest.json", "rules_path": "rules.json", "context_path": "context.json",
        "steps": steps or [
            {"step_id": "list", "depends_on": [], "operation": {"type": "registry.list"}},
            {"step_id": "get", "depends_on": ["list"], "operation": {"type": "registry.get", "artifact_id": "DEMO-001"}},
            {"step_id": "search", "depends_on": ["get"], "operation": {"type": "registry.search", "query": "beta"}},
        ],
    })
    return root / "workflow.json"


class MultiStepWorkflowTests(unittest.TestCase):
    def test_dag_runs_in_dependency_order_and_returns_each_result(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = setup_workflow(Path(directory))
            result = run_multi_step(workflow)
        self.assertEqual(result["status"], "completed")
        self.assertEqual([x["step_id"] for x in result["steps"]], ["list", "get", "search"])
        self.assertEqual(result["steps"][1]["result"]["artifact_id"], "DEMO-001")
        self.assertEqual(result["steps"][2]["result"][0]["artifact_id"], "DEMO-002")

    def test_gate_blocks_before_manifest_is_loaded(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = setup_workflow(root, approved=False)
            (root / "manifest.json").unlink()
            result = run_multi_step(workflow)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(all(x["status"] == "not_run" for x in result["steps"]))

    def test_missing_artifact_stops_downstream_steps(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = setup_workflow(Path(directory), steps=[
                {"step_id": "bad", "depends_on": [], "operation": {"type": "registry.get", "artifact_id": "MISSING"}},
                {"step_id": "after", "depends_on": ["bad"], "operation": {"type": "registry.list"}},
            ])
            result = run_multi_step(workflow)
        self.assertEqual(result["status"], "operation_failed")
        self.assertEqual(result["steps"][0]["status"], "not_found")
        self.assertEqual(result["steps"][1]["status"], "skipped")

    def test_unknown_dependency_and_cycle_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = setup_workflow(root, steps=[
                {"step_id": "a", "depends_on": ["missing"], "operation": {"type": "registry.list"}},
            ])
            with self.assertRaisesRegex(MultiStepWorkflowError, "unknown dependency"):
                run_multi_step(workflow)
            write_json(workflow, {
                "schema_version": "1.0", "workflow_id": "WF-CYCLE",
                "manifest_path": "manifest.json", "rules_path": "rules.json", "context_path": "context.json",
                "steps": [
                    {"step_id": "a", "depends_on": ["b"], "operation": {"type": "registry.list"}},
                    {"step_id": "b", "depends_on": ["a"], "operation": {"type": "registry.list"}},
                ],
            })
            with self.assertRaisesRegex(MultiStepWorkflowError, "cycle"):
                run_multi_step(workflow)

    def test_resume_reuses_completed_steps_and_input_change_invalidates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = setup_workflow(root)
            state = root / "state.json"
            run_multi_step(workflow, state_path=state)
            with patch("tools.multi_step_workflow._dispatch", side_effect=AssertionError("should reuse")):
                resumed = run_multi_step(workflow, state_path=state, resume=True)
            self.assertTrue(all(x.get("resumed") for x in resumed["steps"]))
            write_json(root / "context.json", {"request": {"approved": True, "revision": 2}})
            with patch("tools.multi_step_workflow._dispatch", wraps=__import__("tools.multi_step_workflow", fromlist=["_dispatch"])._dispatch) as dispatch:
                changed = run_multi_step(workflow, state_path=state, resume=True)
            self.assertEqual(dispatch.call_count, 3)
            self.assertTrue(all(not x.get("resumed") for x in changed["steps"]))

    def test_state_path_cannot_overwrite_input(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = setup_workflow(root)
            with patch("sys.stdout"), patch("sys.stderr"):
                self.assertEqual(main([str(workflow), "--state", "manifest.json"]), 1)


if __name__ == "__main__":
    unittest.main()

"""Tests for normalized workflow step outcomes and error details."""
import json
from pathlib import Path
import tempfile
import unittest

from tools.multi_step_workflow import run_multi_step
from tests.test_multi_step_workflow import setup_workflow, write_json


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
        self.assertEqual(result["steps"][2]["reason"], "workflow_stopped_after_failure")

    def test_gate_block_has_not_run_outcome(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = setup_workflow(Path(directory), approved=False)
            result = run_multi_step(workflow)
        self.assertEqual(result["steps"][0]["outcome"], "not_run")


if __name__ == "__main__":
    unittest.main()

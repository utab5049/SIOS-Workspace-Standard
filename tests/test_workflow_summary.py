"""Tests for compact multi-step workflow summaries."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.multi_step_workflow import run_multi_step


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


def make_workflow(root, *, approved=True, steps=None):
    write_json(root / "manifest.json", {
        "schema_version": "1.0.0", "authority_state": "proposed",
        "source_document": "synthetic-summary-fixture.md",
        "artifacts": [{
            "artifact_id": "DEMO-001", "status": "Frozen", "version": "1.0",
            "path": None, "record_state": "explicit", "source_location": "Fixture",
            "notes": ["summary test"],
        }],
    })
    write_json(root / "rules.json", {"schema_version": "1.0", "rules": [{
        "rule_id": "PRE-001", "field": "approved", "operator": "equals",
        "value": True, "message": "Approval required",
    }]})
    write_json(root / "context.json", {"approved": approved})
    write_json(root / "workflow.json", {
        "schema_version": "1.0", "workflow_id": "WF-SUMMARY-TEST",
        "manifest_path": "manifest.json", "rules_path": "rules.json",
        "context_path": "context.json",
        "steps": steps or [
            {"step_id": "first", "depends_on": [], "operation": {"type": "registry.list"}},
            {"step_id": "dependent", "depends_on": ["first"], "operation": {"type": "registry.list"}},
        ],
    })
    return root / "workflow.json"


class WorkflowSummaryTests(unittest.TestCase):
    def test_summary_counts_success_and_reports_blocked_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = make_workflow(root, steps=[
                {"step_id": "failed", "depends_on": [], "operation": {"type": "registry.list"}},
                {"step_id": "blocked", "depends_on": ["failed"], "operation": {"type": "registry.list"}},
                {"step_id": "independent", "depends_on": [], "operation": {"type": "registry.list"}},
            ])
            with patch("tools.multi_step_workflow._dispatch", side_effect=[
                OSError("fixture failure"), ("completed", [{"artifact_id": "DEMO-001"}])
            ]):
                result = run_multi_step(workflow)
        summary = result["summary"]
        self.assertEqual(summary["counts"]["total"], 3)
        self.assertEqual(summary["counts"]["failed"], 1)
        self.assertEqual(summary["counts"]["skipped"], 1)
        self.assertEqual(summary["counts"]["successful"], 1)
        by_id = {item["step_id"]: item for item in summary["steps"]}
        self.assertEqual(by_id["blocked"]["blocked_dependencies"], ["failed"])
        self.assertEqual(by_id["blocked"]["reason"], "dependency_not_completed")
        self.assertEqual(by_id["failed"]["error"], "fixture failure")

    def test_blocked_gate_marks_every_step_not_run_in_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = make_workflow(Path(directory), approved=False)
            result = run_multi_step(workflow)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["summary"]["counts"]["not_run"], 2)
        self.assertEqual(result["summary"]["counts"]["successful"], 0)


if __name__ == "__main__":
    unittest.main()

"""Tests for gated, read-only SIOS workflow execution."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.workflow_runner import WorkflowConfigurationError, _write_report, main, run_workflow


def manifest():
    return {
        "schema_version": "1.0.0",
        "authority_state": "proposed",
        "source_document": "tests/fixture-source.md",
        "artifacts": [{
            "artifact_id": "SIOS-001",
            "status": "Frozen",
            "version": "1.0",
            "path": None,
            "record_state": "explicit",
            "source_location": "Foundation",
            "notes": ["baseline contract"],
        }],
    }


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


class WorkflowRunnerTests(unittest.TestCase):
    def make_files(self, root, *, approved=True, operation=None, manifest_file=True):
        if manifest_file:
            write_json(root / "manifest.json", manifest())
        write_json(root / "context.json", {"request": {"approved": approved}})
        write_json(root / "rules.json", {
            "schema_version": "1.0",
            "rules": [{
                "rule_id": "PRE-001",
                "field": "request.approved",
                "operator": "equals",
                "value": True,
                "message": "Approval is required",
            }],
        })
        write_json(root / "workflow.json", {
            "schema_version": "1.0",
            "workflow_id": "WF-REGISTRY-001",
            "manifest_path": "manifest.json",
            "rules_path": "rules.json",
            "context_path": "context.json",
            "operation": operation or {"type": "registry.get", "artifact_id": "SIOS-001"},
        })
        return root / "workflow.json"

    def test_gate_passes_then_registry_get_runs(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = self.make_files(Path(directory))
            result = run_workflow(workflow)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["gate"]["decision"], "allow")
        self.assertEqual(result["operation"]["status"], "completed")
        self.assertEqual(result["operation"]["result"]["artifact_id"], "SIOS-001")

    def test_failed_gate_blocks_before_manifest_is_loaded(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = self.make_files(Path(directory), approved=False, manifest_file=False)
            result = run_workflow(workflow)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["operation"]["status"], "not_run")
        self.assertEqual(result["gate"]["blocking_failures"], ["PRE-001"])

    def test_registry_list_and_search_are_supported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.make_files(root, operation={"type": "registry.list"})
            self.assertEqual(len(run_workflow(workflow)["operation"]["result"]), 1)
            write_json(root / "workflow.json", {
                "schema_version": "1.0", "workflow_id": "WF-SEARCH",
                "manifest_path": "manifest.json", "rules_path": "rules.json",
                "context_path": "context.json",
                "operation": {"type": "registry.search", "query": "baseline"},
            })
            result = run_workflow(root / "workflow.json")
        self.assertEqual(result["operation"]["result"][0]["artifact_id"], "SIOS-001")

    def test_unknown_operation_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = self.make_files(Path(directory), operation={"type": "shell.exec", "command": "whoami"})
            with self.assertRaisesRegex(WorkflowConfigurationError, "unsupported operation"):
                run_workflow(workflow)

    def test_path_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.make_files(root)
            data = json.loads(workflow.read_text(encoding="utf-8"))
            data["manifest_path"] = "../outside.json"
            write_json(workflow, data)
            with self.assertRaisesRegex(WorkflowConfigurationError, "escapes"):
                run_workflow(workflow)

    def test_missing_artifact_returns_operation_failed(self):
        with tempfile.TemporaryDirectory() as directory:
            workflow = self.make_files(Path(directory), operation={"type": "registry.get", "artifact_id": "NOPE"})
            result = run_workflow(workflow)
        self.assertEqual(result["status"], "operation_failed")
        self.assertEqual(result["operation"]["status"], "not_found")



    def test_example_workflow_is_reproducible(self):
        example = Path(__file__).resolve().parents[1] / "examples" / "workflows" / "registry-lookup" / "workflow.json"
        result = run_workflow(example)
        self.assertEqual(result["workflow_id"], "WF-DEMO-REGISTRY-LOOKUP")
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["operation"]["result"][0]["artifact_id"], "DEMO-001")

    def test_cli_persists_json_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.make_files(root)
            with patch("sys.stdout"), patch("sys.stderr"):
                code = main([str(workflow), "--report", "reports/run.json"])
            self.assertEqual(code, 1)  # The report directory must already exist.
            (root / "reports").mkdir()
            with patch("sys.stdout"), patch("sys.stderr"):
                code = main([str(workflow), "--report", "reports/run.json"])
            self.assertEqual(code, 0)
            report = json.loads((root / "reports" / "run.json").read_text(encoding="utf-8"))
            self.assertEqual(report["report_schema_version"], "1.0")
            self.assertEqual(report["result"]["status"], "completed")
            self.assertIn("generated_at", report)

    def test_cli_appends_execution_history(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.make_files(root)
            with patch("sys.stdout"), patch("sys.stderr"):
                self.assertEqual(main([str(workflow), "--history", "history.jsonl"]), 0)
                self.assertEqual(main([str(workflow), "--history", "history.jsonl"]), 0)
            records = [json.loads(line) for line in (root / "history.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(records), 2)
        self.assertNotEqual(records[0]["run_id"], records[1]["run_id"])
        self.assertTrue(all(record["status"] == "completed" for record in records))
        self.assertTrue(all(record["operation_status"] == "completed" for record in records))
        self.assertTrue(all(record["history_schema_version"] == "1.0" for record in records))

    def test_report_cannot_overwrite_inputs_or_escape_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.make_files(root)
            with self.assertRaisesRegex(WorkflowConfigurationError, "overwrite"):
                _write_report(workflow, "rules.json", {"status": "completed"})
            with self.assertRaisesRegex(WorkflowConfigurationError, "inside"):
                _write_report(workflow, "../outside.json", {"status": "completed"})


if __name__ == "__main__":
    unittest.main()

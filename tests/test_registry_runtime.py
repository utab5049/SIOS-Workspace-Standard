"""Tests for the read-only SIOS registry runtime."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.registry_runtime import ManifestValidationError, RegistryRuntime, main


def sample_manifest():
    return {
        "schema_version": "1.0.0",
        "authority_state": "proposed",
        "source_document": "tests/fixture-source.md",
        "artifacts": [
            {
                "artifact_id": "SIOS-001",
                "status": "Frozen",
                "version": "1.0",
                "path": None,
                "record_state": "explicit",
                "source_location": "Foundation",
                "notes": ["baseline contract"],
            },
            {
                "artifact_id": "SIOS-002",
                "status": "Draft",
                "version": None,
                "path": "docs/draft.md",
                "record_state": "unverified",
                "source_location": "Research",
                "notes": ["runtime prototype"],
            },
            {
                "artifact_id": "RULE-003",
                "status": "Frozen",
                "version": "2.0",
                "path": None,
                "record_state": "grouped",
                "source_location": None,
                "notes": [],
            },
        ],
    }


class RegistryRuntimeTests(unittest.TestCase):
    def test_list_preserves_manifest_order(self):
        runtime = RegistryRuntime(sample_manifest())
        self.assertEqual([r["artifact_id"] for r in runtime.list_records()],
                         ["SIOS-001", "SIOS-002", "RULE-003"])

    def test_get_by_id_is_exact_and_returns_none_when_missing(self):
        runtime = RegistryRuntime(sample_manifest())
        self.assertEqual(runtime.get_by_id("SIOS-002")["status"], "Draft")
        self.assertIsNone(runtime.get_by_id("sios-002"))

    def test_search_is_case_insensitive_across_fields_and_notes(self):
        runtime = RegistryRuntime(sample_manifest())
        self.assertEqual([r["artifact_id"] for r in runtime.search("PROTOTYPE")], ["SIOS-002"])
        self.assertEqual([r["artifact_id"] for r in runtime.search("frozen")], ["SIOS-001", "RULE-003"])

    def test_empty_search_returns_all_records(self):
        self.assertEqual(len(RegistryRuntime(sample_manifest()).search("  ")), 3)

    def test_filter_can_combine_status_and_record_state(self):
        runtime = RegistryRuntime(sample_manifest())
        records = runtime.filter_records(status="frozen", record_state="grouped")
        self.assertEqual([r["artifact_id"] for r in records], ["RULE-003"])

    def test_returned_records_cannot_mutate_runtime_index(self):
        runtime = RegistryRuntime(sample_manifest())
        record = runtime.get_by_id("SIOS-001")
        record["status"] = "Changed"
        record["notes"].append("tampered")
        self.assertEqual(runtime.get_by_id("SIOS-001")["status"], "Frozen")
        self.assertEqual(runtime.get_by_id("SIOS-001")["notes"], ["baseline contract"])

    def test_invalid_manifest_is_rejected(self):
        data = sample_manifest()
        data["artifacts"].append(dict(data["artifacts"][0]))
        with self.assertRaises(ManifestValidationError):
            RegistryRuntime(data)

    def test_from_file_loads_validated_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(sample_manifest()), encoding="utf-8")
            runtime = RegistryRuntime.from_file(path)
            self.assertEqual(runtime.get_by_id("SIOS-002")["artifact_id"], "SIOS-002")

    def test_cli_get_returns_zero_for_existing_id(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(sample_manifest()), encoding="utf-8")
            with patch("builtins.print") as output:
                code = main([str(path), "get", "SIOS-001"])
            self.assertEqual(code, 0)
            self.assertIn("SIOS-001", output.call_args.args[0])

    def test_cli_get_returns_two_for_missing_id(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(sample_manifest()), encoding="utf-8")
            with patch("sys.stderr"):
                self.assertEqual(main([str(path), "get", "missing"]), 2)


if __name__ == "__main__":
    unittest.main()

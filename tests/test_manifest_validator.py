"""Tests for the read-only validator for the proposed machine-readable manifest."""
import json
from pathlib import Path
import tempfile
import unittest

from tools.manifest_validator import main, validate_manifest, validate_manifest_file


def valid_manifest():
    return {
        "schema_version": "1.0.0",
        "authority_state": "proposed",
        "source_document": None,
        "artifacts": [
            {
                "artifact_id": "SIOS-BASELINE-001",
                "status": "Frozen 1.1.0",
                "version": "1.1.0",
                "path": None,
                "record_state": "explicit",
                "source_location": "Registry section",
                "notes": [],
            }
        ],
    }


class ManifestValidatorTests(unittest.TestCase):
    def test_accepts_valid_proposed_manifest(self):
        self.assertEqual(validate_manifest(valid_manifest()), [])

    def test_empty_artifact_list_is_valid_and_does_not_infer_records(self):
        data = valid_manifest()
        data["artifacts"] = []
        self.assertEqual(validate_manifest(data), [])

    def test_rejects_non_object_root(self):
        findings = validate_manifest(["not", "an", "object"])
        self.assertEqual([(f.code, f.location) for f in findings], [("ROOT_TYPE", "$")])

    def test_rejects_non_array_artifacts(self):
        data = valid_manifest()
        data["artifacts"] = {"artifact_id": "not-an-array"}
        findings = validate_manifest(data)
        self.assertIn(("FIELD_TYPE", "$.artifacts"), {(f.code, f.location) for f in findings})

    def test_rejects_non_object_artifact_item(self):
        data = valid_manifest()
        data["artifacts"] = ["not-an-object"]
        findings = validate_manifest(data)
        self.assertIn(("RECORD_TYPE", "$.artifacts[0]"), {(f.code, f.location) for f in findings})

    def test_rejects_wrong_types_for_nullable_fields(self):
        data = valid_manifest()
        data["source_document"] = 42
        data["artifacts"][0]["version"] = 7
        data["artifacts"][0]["path"] = False
        data["artifacts"][0]["source_location"] = []
        findings = validate_manifest(data)
        locations = {f.location for f in findings if f.code == "FIELD_TYPE"}
        self.assertTrue({
            "$.source_document",
            "$.artifacts[0].version",
            "$.artifacts[0].path",
            "$.artifacts[0].source_location",
        }.issubset(locations))

    def test_rejects_missing_required_field(self):
        data = valid_manifest()
        del data["artifacts"][0]["version"]
        findings = validate_manifest(data)
        self.assertIn(("FIELD_REQUIRED", "$.artifacts[0].version"),
                      {(f.code, f.location) for f in findings})

    def test_rejects_duplicate_artifact_ids(self):
        data = valid_manifest()
        data["artifacts"].append(dict(data["artifacts"][0]))
        findings = validate_manifest(data)
        self.assertIn("ARTIFACT_ID_DUPLICATE", {f.code for f in findings})

    def test_rejects_invalid_artifact_id_and_record_state(self):
        data = valid_manifest()
        data["artifacts"][0]["artifact_id"] = "../bad id"
        data["artifacts"][0]["record_state"] = "approved"
        findings = validate_manifest(data)
        codes = {f.code for f in findings}
        self.assertIn("ARTIFACT_ID_INVALID", codes)
        self.assertIn("RECORD_STATE_INVALID", codes)

    def test_rejects_path_traversal_and_absolute_paths(self):
        for unsafe_path in ("../secret.txt", "/etc/passwd", r"docs\\secret.md", "C:/secret.txt"):
            with self.subTest(path=unsafe_path):
                data = valid_manifest()
                data["artifacts"][0]["path"] = unsafe_path
                self.assertIn("PATH_UNSAFE", {f.code for f in validate_manifest(data)})

    def test_unknown_fields_and_non_proposed_authority_are_errors(self):
        data = valid_manifest()
        data["authority_state"] = "ratified"
        data["unexpected"] = True
        findings = validate_manifest(data)
        self.assertIn("AUTHORITY_STATE", {f.code for f in findings})
        self.assertIn("FIELD_UNKNOWN", {f.code for f in findings})

    def test_reports_malformed_json(self):
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "manifest.json"
            file_path.write_text("{ not json", encoding="utf-8")
            findings = validate_manifest_file(file_path)
            self.assertEqual([f.code for f in findings], ["JSON_INVALID"])

    def test_reports_unreadable_or_missing_manifest(self):
        missing_path = Path(tempfile.gettempdir()) / "sios-test-file-that-does-not-exist.json"
        findings = validate_manifest_file(missing_path)
        self.assertEqual([f.code for f in findings], ["FILE_READ_ERROR"])

    def test_missing_repository_path_is_warning_not_error(self):
        with tempfile.TemporaryDirectory() as directory:
            data = valid_manifest()
            data["artifacts"][0]["path"] = "docs/not-present.md"
            findings = validate_manifest(data, repo_root=Path(directory))
            self.assertEqual([(f.code, f.severity) for f in findings],
                             [("PATH_NOT_FOUND", "warning")])

    def test_existing_repository_path_does_not_emit_warning(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "known.md").write_text("synthetic test file", encoding="utf-8")
            data = valid_manifest()
            data["artifacts"][0]["path"] = "docs/known.md"
            findings = validate_manifest(data, repo_root=root)
            self.assertEqual(findings, [])

    def test_cli_returns_error_for_malformed_json(self):
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "manifest.json"
            file_path.write_text("{ invalid", encoding="utf-8")
            self.assertEqual(main([str(file_path)]), 1)

    def test_does_not_modify_manifest_file(self):
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "manifest.json"
            file_path.write_text(json.dumps(valid_manifest(), indent=2), encoding="utf-8")
            before = file_path.read_bytes()
            validate_manifest_file(file_path, repo_root=Path(directory))
            self.assertEqual(file_path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()

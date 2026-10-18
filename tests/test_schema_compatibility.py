"""Contract-drift tests between the proposed JSON Schema and Python validator.

These tests compare the supported subset implemented by the validator; they do
not claim to implement or fully validate the JSON Schema specification.
"""
import json
from pathlib import Path
import unittest

from tools import manifest_validator as validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "registry-manifest.schema.json"


class SchemaCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.top_properties = cls.schema["properties"]
        cls.artifact_schema = cls.top_properties["artifacts"]["items"]
        cls.artifact_properties = cls.artifact_schema["properties"]

    def test_schema_version_matches_validator_constant(self):
        self.assertEqual(self.top_properties["schema_version"]["const"],
                         validator.SCHEMA_VERSION)

    def test_authority_state_remains_proposed(self):
        self.assertEqual(self.top_properties["authority_state"]["const"],
                         validator.AUTHORITY_STATE)
        self.assertEqual(validator.AUTHORITY_STATE, "proposed")

    def test_top_level_fields_match_validator(self):
        self.assertEqual(set(self.top_properties), validator.TOP_LEVEL_FIELDS)
        self.assertEqual(set(self.schema["required"]), validator.REQUIRED_TOP_LEVEL)
        self.assertFalse(self.schema["additionalProperties"])

    def test_artifact_fields_match_validator(self):
        self.assertEqual(set(self.artifact_properties), validator.ARTIFACT_FIELDS)
        self.assertEqual(set(self.artifact_schema["required"]), validator.REQUIRED_ARTIFACT)
        self.assertFalse(self.artifact_schema["additionalProperties"])

    def test_artifact_id_pattern_matches_validator(self):
        self.assertEqual(self.artifact_properties["artifact_id"]["pattern"],
                         validator.ARTIFACT_ID_PATTERN)

    def test_record_state_enum_matches_validator(self):
        self.assertEqual(set(self.artifact_properties["record_state"]["enum"]),
                         validator.RECORD_STATES)

    def test_nullable_field_types_match_validator_expectations(self):
        self.assertEqual(set(self.top_properties["source_document"]["type"]),
                         {"string", "null"})
        for field in ("status", "version", "path", "source_location"):
            self.assertEqual(set(self.artifact_properties[field]["type"]),
                             {"string", "null"})

    def test_notes_is_an_array_of_strings(self):
        self.assertEqual(self.artifact_properties["notes"]["type"], "array")
        self.assertEqual(self.artifact_properties["notes"]["items"]["type"], "string")


if __name__ == "__main__":
    unittest.main()

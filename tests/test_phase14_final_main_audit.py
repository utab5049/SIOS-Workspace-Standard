"""Phase 14 regression check for the known final-main registry discrepancy.

This test does not endorse the discrepancy. It ensures the validator continues
to surface it rather than silently presenting the current registry as clean.
"""
from pathlib import Path
import unittest

from tools.registry_validator import validate


ROOT = Path(__file__).resolve().parents[1]


class FinalMainAuditTests(unittest.TestCase):
    def test_known_registry_discrepancy_is_reported(self):
        findings = validate(ROOT)
        conflict_paths = {
            path
            for finding in findings
            if finding.code == "MAI_REGISTRY_CONFLICT"
            for path in finding.paths
        }

        self.assertEqual(
            len([f for f in findings if f.code == "MAI_REGISTRY_CONFLICT"]),
            2,
            "Expected the known MAI-001 vs secondary-registry discrepancy to remain visible.",
        )
        self.assertTrue(
            {
                "01-Foundation/Registry/MAI-001.md",
                "12-Registry/README.md",
                "12-Registry/INDEX.md",
            }.issubset(conflict_paths)
        )


if __name__ == "__main__":
    unittest.main()

import json
import unittest
from pathlib import Path

from scripts.validate_gdr_oai import ROOT, STAGED_GDR, STAGED_OAI, validate_package


class GdrOaiMigrationValidationTests(unittest.TestCase):
    def test_staged_package_satisfies_schemas_and_cross_references(self):
        self.assertEqual([], validate_package())

    def test_staged_records_match_migration_map_entry_counts(self):
        migration_path = ROOT / "02-Research/Registry/migration/phase-20-migration-map.json"
        migration = json.loads(migration_path.read_text(encoding="utf-8"))
        self.assertEqual(
            len(migration["governance_decisions"]),
            len(list(STAGED_GDR.glob("*.json"))),
        )
        self.assertEqual(
            len(migration["operational_inventory"]),
            len(list(STAGED_OAI.glob("*.json"))),
        )

    def test_c1_record_remains_unresolved(self):
        c1_path = STAGED_GDR / "GOV-DEC-C1.json"
        c1 = json.loads(c1_path.read_text(encoding="utf-8"))
        self.assertEqual("unresolved", c1["status"])


if __name__ == "__main__":
    unittest.main()

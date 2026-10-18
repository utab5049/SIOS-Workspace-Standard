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

    def test_phase_27_proposed_oai_records_are_schema_validated(self):
        proposal_dir = ROOT / "02-Research/Registry/migration/proposals/phase-27-oai-candidates"
        proposals = sorted(proposal_dir.glob("*.json"))
        self.assertEqual(7, len(proposals))
        records = [json.loads(path.read_text(encoding="utf-8")) for path in proposals]
        self.assertEqual(
            {path.stem for path in proposals},
            {record["artifact_id"] for record in records},
        )
        self.assertIn("CIR-001", {record["artifact_id"] for record in records})
        self.assertIn("EIR-001", {record["artifact_id"] for record in records})
        self.assertEqual(
            {"disputed"},
            {
                record["reconciliation_status"]
                for record in records
                if record["artifact_id"].startswith("REVIEW-BATCH-")
            },
        )

    def test_phase_28_proposed_oai_records_and_reconciliation_dataset(self):
        proposal_dir = ROOT / "02-Research/Registry/migration/proposals/phase-28-oai-candidates"
        proposals = sorted(proposal_dir.glob("*.json"))
        self.assertEqual(7, len(proposals))
        records = [json.loads(path.read_text(encoding="utf-8")) for path in proposals]
        self.assertEqual(
            {path.stem for path in proposals},
            {record["artifact_id"] for record in records},
        )
        self.assertIn("SRC-000017", {record["artifact_id"] for record in records})
        self.assertIn("EV-000012", {
            evidence["evidence_id"]
            for evidence in json.loads(
                (ROOT / "02-Research/Registry/migration/phase-28-instance-evidence-reconciliation.json").read_text(encoding="utf-8")
            )["evidence_instance_reconciliation"]
        })
        self.assertEqual(
            "proposed_reconciliation_not_applied",
            json.loads(
                (ROOT / "02-Research/Registry/migration/phase-28-instance-evidence-reconciliation.json").read_text(encoding="utf-8")
            )["status"],
        )

    def test_phase_29_migration_plan_is_gated_and_non_destructive(self):
        plan_path = ROOT / "02-Research/Registry/migration/phase-29-controlled-migration-plan.json"
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        self.assertEqual("plan_only_not_applied", plan["status"])
        self.assertFalse(plan["target_architecture"]["canonical_registry_changes_allowed"])
        self.assertEqual(
            {"G1", "G2", "G3", "G4"},
            {gate["gate"] for gate in plan["required_gates"]},
        )
        c1 = next(op for op in plan["operations"] if op["operation_id"] == "MIG029-04")
        self.assertEqual("no_change_authorized", c1["status"])
        self.assertIn(
            "Keep GOV-DEC-C1 unresolved until an authorized governance decision is recorded.",
            plan["invariants"],
        )

    def test_c1_record_remains_unresolved(self):
        c1_path = STAGED_GDR / "GOV-DEC-C1.json"
        c1 = json.loads(c1_path.read_text(encoding="utf-8"))
        self.assertEqual("unresolved", c1["status"])


if __name__ == "__main__":
    unittest.main()

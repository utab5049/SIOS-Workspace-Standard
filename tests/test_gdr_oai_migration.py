import json
import unittest
from pathlib import Path

from scripts.validate_gdr_oai import ROOT, STAGED_GDR, STAGED_OAI, validate_package, validate_phase31_correction_package


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

    def test_phase_30_instance_review_matrix_is_unique_and_not_applied(self):
        matrix_path = ROOT / "02-Research/Registry/migration/phase-30-instance-review-matrix.json"
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        self.assertEqual("review_matrix_proposed_not_applied", matrix["status"])
        source_ids = [item["source_id"] for item in matrix["source_instances"]]
        evidence_ids = [item["evidence_id"] for item in matrix["evidence_instances"]]
        self.assertEqual(len(source_ids), len(set(source_ids)))
        self.assertEqual(len(evidence_ids), len(set(evidence_ids)))
        self.assertEqual(14, matrix["registry_level_findings"]["cir_rows"])
        self.assertTrue(matrix["registry_level_findings"]["cir_table_count_mismatch"])
        self.assertEqual("unresolved", matrix["registry_level_findings"]["c1_status"])
        for item in matrix["source_instances"]:
            if item.get("registration_path"):
                self.assertTrue((ROOT / item["registration_path"]).is_file(), item["registration_path"])
            for path in item.get("supplementary_paths", []):
                self.assertTrue((ROOT / path).is_file(), path)
        for item in matrix["evidence_instances"]:
            self.assertTrue((ROOT / item["record_or_container_path"]).is_file(), item["record_or_container_path"])
            for path in item.get("supplementary_paths", []):
                self.assertTrue((ROOT / path).is_file(), path)

    def test_phase_31_correction_package_is_proposal_only(self):
        package_path = ROOT / "02-Research/Registry/migration/phase-31-correction-package.json"
        package = json.loads(package_path.read_text(encoding="utf-8"))
        self.assertEqual("proposed_not_applied", package["status"])
        self.assertFalse(package["canonical_files_changed"])
        self.assertFalse(package["staged_oai_or_gdr_changed"])
        self.assertFalse(package["merge_authorized"])
        self.assertEqual(14, package["known_reconciliations"]["cir_current_table_rows"])
        self.assertEqual(5, package["known_reconciliations"]["cir_full_text_rows"])
        self.assertEqual(9, package["known_reconciliations"]["cir_abstract_only_rows"])
        for item in package["proposed_documents"]:
            self.assertTrue((ROOT / item["path"]).is_file(), item["path"])
        cir = (ROOT / package["proposed_documents"][0]["path"]).read_text(encoding="utf-8")
        eir = (ROOT / package["proposed_documents"][1]["path"]).read_text(encoding="utf-8")
        self.assertIn("SRC-000017", cir)
        self.assertIn("EV-000012", eir)
        self.assertIn("Disputed", eir)

    def test_phase_31_correction_package_paths_and_safety(self):
        self.assertEqual([], validate_phase31_correction_package())

    def test_phase_33_owner_decision_gate_is_explicit_and_non_authorizing(self):
        gate_path = ROOT / "02-Research/Registry/migration/phase-33-owner-decision-gate.json"
        gate = json.loads(gate_path.read_text(encoding="utf-8"))
        self.assertEqual("pending_owner_decisions_not_applied", gate["status"])
        self.assertEqual(7, len(gate["decisions"]))
        self.assertTrue(all(item["status"].startswith("pending_") for item in gate["decisions"]))
        self.assertFalse(gate["invariants"]["canonical_files_changed"])
        self.assertFalse(gate["invariants"]["staged_oai_or_gdr_changed"])
        self.assertFalse(gate["invariants"]["merge_authorized"])
        self.assertEqual("unresolved", gate["invariants"]["c1_status"])
        decision_ids = [item["decision_id"] for item in gate["decisions"]]
        self.assertEqual(len(decision_ids), len(set(decision_ids)))
        self.assertEqual({"G1", "G2", "G3", "G4"}, {item["gate"] for item in gate["release_gates"]})

    def test_phase_34_contract_audit_preserves_unverified_boundaries(self):
        audit_path = ROOT / "02-Research/Registry/migration/phase-34-cir-eir-contract-audit.json"
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        self.assertEqual("proposed_contract_audit_not_applied", audit["status"])
        self.assertEqual("5bc0ff427e7937139e85d3222e65cb0f4b1ab11b", audit["source_snapshot_commit"])
        source_ids = {item["instance_id"] for item in audit["source_contract_audit"]}
        evidence_ids = {item["instance_id"] for item in audit["evidence_contract_audit"]}
        self.assertEqual({"SRC-000017", "SRC-000018", "SRC-000019"}, source_ids)
        self.assertEqual({"EV-000006", "EV-000007", "EV-000008", "EV-000009", "EV-000012"}, evidence_ids)
        self.assertTrue(all(item["contract_status"] != "verified" for item in audit["source_contract_audit"]))
        self.assertTrue(all(item["contract_status"] != "verified" for item in audit["evidence_contract_audit"]))
        for collection in (audit["source_contract_audit"], audit["evidence_contract_audit"]):
            for item in collection:
                self.assertTrue((ROOT / item["path"]).is_file(), item["path"])
        self.assertFalse(audit["invariants"]["canonical_cir_eir_changed"])
        self.assertFalse(audit["invariants"]["staged_oai_or_gdr_changed"])
        self.assertFalse(audit["invariants"]["migration_map_changed"])
        self.assertFalse(audit["invariants"]["merge_authorized"])
        self.assertEqual("unresolved", audit["invariants"]["c1_status"])

    def test_c1_record_remains_unresolved(self):
        c1_path = STAGED_GDR / "GOV-DEC-C1.json"
        c1 = json.loads(c1_path.read_text(encoding="utf-8"))
        self.assertEqual("unresolved", c1["status"])


if __name__ == "__main__":
    unittest.main()

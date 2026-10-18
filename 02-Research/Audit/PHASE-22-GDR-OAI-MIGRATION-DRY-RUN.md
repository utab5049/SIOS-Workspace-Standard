# Phase 22 — GDR/OAI Migration Dry Run

**Status:** Dry run only; no canonical migration applied  
**Source snapshot:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Migration map:** `02-Research/Registry/migration/phase-20-migration-map.json`  
**Target model:** GDR (governance decisions) + OAI (operational artifact inventory)

## 1. Purpose and limits

This report evaluates the staged migration map against the source snapshot and identifies actions and blockers before any canonical registry file is changed. It is a bounded dry run over the three artifact records currently in the map, not a complete repository inventory or proof that every historical claim is true.

The Phase 21 validator checks schema conformance, duplicate IDs, decision references, repository-relative source paths, and protected migration invariants. Its CI run passed after the migration map's architecture-evidence reference was corrected. A passing validator does not resolve disputed source claims.

## 2. Proposed GDR records

| Decision ID | Current state | Dry-run handling |
|---|---|---|
| `GOV-DEC-001` | Architecture direction approved by explicit project-owner instruction; repository adoption pending review and merge | Preserve as the decision record for separating governance authority from inventory metadata. Do not describe repository adoption as complete until the dependent PR chain is reviewed and merged. |
| `GOV-DEC-C1` | Unresolved | Preserve the conflicting C1 ratification and decision-history claims as evidence. Do not promote, revoke, or rewrite C1 status in this migration. |

### C1 evidence gate

The staged map points to `C1-RATIFIED-FINAL.md`, `DECISIONS-RECORDED.md`, and `REVIEW-LEDGER.md`, with verification states `disputed`, `disputed`, and `unverified`. The dry run does not infer that missing source packages prove reviews did not occur. Before a C1 status change, the authorized governance owner must either identify and review the source packages or explicitly authorize an evidence-unavailable determination after a bounded recovery attempt.

## 3. Proposed OAI inventory records

| Artifact ID | Source path | Source claim at snapshot | Reconciliation state | Dry-run action |
|---|---|---|---|---|
| `MAI-001` | `01-Foundation/Registry/MAI-001.md` | Declares itself authoritative and lists registered artifacts | Disputed | Preserve as a legacy artifact and provenance source; do not let its self-declared authority override the adopted GDR/OAI precedence model before adoption is complete. |
| `REGISTRY-README` | `12-Registry/README.md` | States that no artifacts are currently registered | Disputed | Preserve as an inventory-related artifact with conflicting historical claims; do not silently rewrite its status. |
| `REGISTRY-INDEX` | `12-Registry/INDEX.md` | States that no artifacts are currently registered | Disputed | Preserve as an inventory-related artifact with conflicting historical claims; do not silently rewrite its status. |

All three records retain the source commit `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b` in provenance. The current map intentionally records the conflict instead of selecting a winner. These three records are the full scope of this dry run; they must not be represented as a complete OAI.

## 4. Expected change set for a future migration PR

1. Add versioned GDR records and OAI inventory records using the Phase 20 schemas.
2. Preserve source paths, source commit, source claims, lifecycle state, and reconciliation state.
3. Add explicit precedence and supersession links where an authorized decision exists; do not infer supersession merely from file age.
4. Leave original source documents and Git history intact. Any corrections should be separately reviewed and traceable.
5. Keep C1 unresolved until its evidence gate is satisfied by an authorized decision.
6. Update legacy registry entry points only in a separate migration PR, with a before/after mapping and rollback plan.

## 5. Blocking conditions before applying migration

- Phase 20 architecture adoption and Phase 21 validation changes must be reviewed in their dependency order; neither is merged by this report.
- The final target location and versioning convention for canonical GDR/OAI records must be confirmed in the migration PR.
- The OAI must be expanded through a bounded inventory pass; three mapped records are not sufficient to claim complete coverage.
- A migration PR must provide a source-to-target mapping, evidence preservation check, and explicit no-silent-resolution test for disputed records.
- C1 status must not be changed by the registry migration.

## 6. Dry-run result

**Result: READY FOR MIGRATION-PR DESIGN, NOT READY TO APPLY.**

The staged map preserves the currently known contradiction and separates the two governance decisions from inventory metadata. However, coverage is partial, the dependent architecture/validator PRs remain subject to review, and C1 remains unresolved. No source registry file was changed by this dry run.

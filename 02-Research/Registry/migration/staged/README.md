# Phase 23 — Staged GDR/OAI Records

**Status:** Staged migration package; not canonical  
**Source snapshot:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Migration ID:** `MIG-020`

## Scope

This package materializes the records already present in the Phase 20 migration map as individual JSON files under `migration/staged/`. It contains two governance decisions and three operational inventory records. It is a controlled, reviewable migration slice, not a complete repository inventory.

## Record layout

- `staged/gdr/GOV-DEC-001.json` — approved target architecture direction; repository adoption remains subject to the dependent PR review/merge sequence.
- `staged/gdr/GOV-DEC-C1.json` — C1 evidence status remains unresolved.
- `staged/oai/MAI-001.json` — legacy index record with disputed authority/claims.
- `staged/oai/REGISTRY-README.json` — conflicting operational registry claim.
- `staged/oai/REGISTRY-INDEX.json` — conflicting operational registry claim.

## Integrity and preservation rules

1. Individual records are copied from the migration map without silently resolving conflicting source claims.
2. Source paths and source commit provenance are retained where recorded.
3. The staged records are not promoted to canonical GDR/OAI directories in this phase.
4. No legacy source document is modified or deleted.
5. C1 remains unresolved; this package makes no new ratification decision.
6. The inventory scope remains explicitly limited to the three records already mapped.

## Acceptance checks

The validation code must validate each staged record against the corresponding Draft 2020-12 schema, check that every staged record matches the migration map entry for the same ID, detect duplicate/missing/extra staged files, and preserve the unresolved C1 invariant. A passing check establishes package consistency only; it does not prove the underlying historical claims are true.

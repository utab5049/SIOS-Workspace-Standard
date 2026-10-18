# Phase 29 — Controlled Registry Migration Plan

**Status:** Plan only; no canonical migration applied  
**Source snapshot:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Parent:** Phase 28 instance/evidence reconciliation  
**C1:** Unresolved

## 1. Purpose

Phase 29 turns the findings from Phase 28 into a gated migration plan. It does not edit CIR-001, EIR-001, the canonical registry entry points, or the staged migration records. The machine-readable plan is `02-Research/Registry/migration/phase-29-controlled-migration-plan.json`.

## 2. Proposed migration work

1. **CIR-001:** normalize detail locations to repository-relative paths; distinguish source registration files from supplementary full-text/search reports; reconcile the stated count of 16 against the 14 table rows and later source IDs.
2. **EIR-001:** normalize evidence paths; preserve EV-000003 version/split history; represent EV-000005 supersession and correction history; verify EV-000012 against the evidence-record contract before considering inclusion.
3. **OAI package:** only promote reviewed records in a later PR. Batch containers remain distinct from individual source, evidence, and observation instances.
4. **C1:** retain the unresolved state. No migration phase may ratify it by implication.
5. **Registry entry points:** prepare clearer GDR/OAI authority language only after the migration has governance review and the implementation PR is ready.

## 3. Required gates

| Gate | Required evidence | Effect |
|---|---|---|
| G1 — Content review | Per-ID CIR/EIR review with exact paths and provenance | Blocks path/count normalization |
| G2 — Governance review | Authorized decision on registry authority and conflicting claims | Blocks canonical registry/entry-point changes |
| G3 — Automated validation | Schema, path, unique-ID, staged/map parity and lineage checks | Blocks migration implementation |
| G4 — Separate migration PR | Reviewable canonical diff with provenance and rollback notes | Required before applying changes |

## 4. Non-negotiable invariants

- Preserve source files and Git history.
- OAI metadata does not confer governance approval.
- Conflicting claims remain visible until an authorized decision resolves them.
- Missing evidence is not proof that an event did not occur.
- Corrections, versions, splits, supersessions and review lineage remain traceable.
- Batch containers are not counted as individual instances.
- C1 stays unresolved until a separate authorized decision is recorded.

## 5. Exit criteria

Phase 29 is complete as a planning phase when its machine-readable operations and gates are reviewable. It is **not** evidence that the migration itself is complete. Phase 30 should create a per-ID review matrix and close the remaining content questions before a separate canonical migration PR is prepared.

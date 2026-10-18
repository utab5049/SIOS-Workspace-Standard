# Phase 26 — Content Classification and Conflict Reconciliation

**Status:** Partial content classification completed; full OAI inventory not yet ready  
**Pinned source commit:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Dependency:** Phase 25 tree-level inventory  
**Canonical migration:** Not applied

## 1. Executive result

Phase 25 established the complete repository tree. Phase 26 begins the next layer: classifying files by their stated purpose and capturing conflicts that filename matching cannot resolve.

The machine-readable classification dataset records **16 primary registry/governance documents** inspected at their headers and stated purpose, plus **18 additional source/evidence/review candidates** classified provisionally by path/name and surrounding repository context. The latter are not represented as fully content-verified.

The key finding is not a new decision. It is a **material conflict in the repository's recorded governance state**: C1 is represented as both ratified and blocked pending independent review. A filename or “final” label cannot resolve that conflict.

## 2. Reproducible classification dataset

File: `02-Research/Registry/migration/phase-26-content-classification.json`

It records:
- classification and rationale for 16 primary governance/registry documents;
- 18 additional evidence/source/review candidates requiring further content review;
- explicit distinction between an observed statement and an authoritative fact;
- unresolved issues and limits of the current pass.

## 3. Confirmed classifications

| File or group | Classification | Finding |
|---|---|---|
| `01-Foundation/Registry/MAI-001.md` | Registry candidate with authority claim | Calls itself authoritative and describes a post-ratification registry view |
| `12-Registry/README.md`, `12-Registry/INDEX.md` | Registry entry points | Both state that no artifacts are registered |
| `MAI-001-FINAL-MERGE-V3/V4/V5.md` | Historical merge/revision documents | They contain competing registry states; V5 claims pending decisions ratified |
| `MAI-001-REGISTRY-DELTA.md`, `...DELTA-V2.md` | Proposed registry deltas | Explicitly describe proposed/unmerged additions rather than the frozen canonical registry |
| `C1-RATIFIED-FINAL.md` | Governance decision claim | Claims C1 ratified on the current evidence base |
| `DECISIONS-RECORDED.md` | Governance decision claim | Records C1 as 1B, blocked on independent sample review |
| `DECISION-MAI001-OPTION-B.md` | Governance decision record | Records Option B and sub-registry approach under delegated pilot authority |
| `REVIEW-LEDGER.md` | Audit evidence template | Says evidence is not yet reconciled and the ledger does not certify independence |
| `INDEPENDENT-REVIEW-PROTOCOL.md` | Proposed protocol | Says maintainer approval is required before it is normative |
| `REGISTRY-MACHINE-READABLE-CONTRACT.md` | Proposed schema contract | Explicitly says it is not ratified or authoritative |
| `VALIDATION-COVERAGE-MATRIX.md` | Engineering audit report | Not a governance decision |

## 4. C1 conflict: preserve, do not auto-resolve

Two records make incompatible claims:

- `02-Research/Registry/C1-RATIFIED-FINAL.md` says C1 changed from 1B to ratified.
- `02-Research/Registry/DECISIONS-RECORDED.md` says C1 remains 1B and blocked on independent sample review.

`MAI-001-FINAL-MERGE-V5.md` additionally claims that all pending governance decisions were ratified. Other audit materials describe the independent-review evidence as unreconciled or incomplete.

This phase does **not** select the latest filename, assume one document supersedes another, or infer that a review did or did not occur. The GDR record must retain the competing claims, their source paths, the relevant source commit, and a reconciliation state pending an authorized governance decision and verifiable evidence.

## 5. SRE-000001-A path discrepancy

The Phase 25 exact-basename crosswalk found no file named `SRE-000001-A.md` in the pinned tree. However, `MAI-001-FINAL-MERGE-V4.md` includes a row for `SRE-000001-A` and names that path.

A path-specific GitHub commit-history query for `02-Research/Search/SRE-000001-A.md` returned no entries. This is evidence that the queried path has no returned commit history in the accessible repository view; it does not prove that the file never existed elsewhere or that review work never happened.

Required handling: mark `path_unverified_at_pinned_commit`, retain the V4 reference as provenance, and continue with reference/history investigation before making any lifecycle claim.

## 6. Additional source/evidence/review candidates

The classification dataset lists 18 candidates, including source extraction/resolution files, source batches, evidence batches, observation batches, review batches, and blind-test packages. These need a content-level pass to decide whether each is:
- a standalone artifact with its own lifecycle;
- a batch/container whose children are separate records;
- supporting evidence linked to another artifact;
- a report, template, draft, or superseded revision.

No candidate is promoted automatically to a canonical OAI record.

## 7. Readiness assessment

| Gate | Result |
|---|---|
| Pinned full tree available | Complete at Phase 25 |
| Primary governance conflict identified | Complete for inspected records |
| Candidate classification dataset created | Complete as a draft |
| All candidate contents reviewed | Not complete |
| C1 authority conflict resolved | Not complete |
| Full OAI proposed inventory validated | Not complete |
| Canonical registry migration | Not applied |

## 8. Next phase

Phase 27 should complete content review for remaining candidate files, especially:
1. `CIR-001.md` and `EIR-001.md` and their instance coverage;
2. source/evidence batch documents and their contained IDs;
3. review-batch and blind-test evidence, mapped to the review ledger;
4. the MAI-001 range/grouped cells against actual artifact headers;
5. the `SRE-000001-A` path discrepancy through cross-references and repository history.

Then generate proposed OAI records only for classified inventory items and run schema/parity checks. Any decision about C1's outcome must remain separate from mechanical inventory validation.

## 9. Decision

**Phase 26: PARTIAL CONTENT CLASSIFICATION COMPLETE. Full inventory reconciliation remains open.**

No canonical registry files were modified. `GOV-DEC-C1` remains unresolved in the staged GDR/OAI package.

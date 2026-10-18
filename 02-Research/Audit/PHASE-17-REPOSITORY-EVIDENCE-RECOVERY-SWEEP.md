# Phase 17 — Repository Evidence Recovery Sweep

**Status:** Search completed within the documented scope; evidence remains unverified.  
**Scope:** Repository code search and commit-message search, plus previously documented exact-path retrieval attempts.  
**Governance effect:** None. This report does not ratify C1, reject C1, select a canonical registry, or change registry statuses.

## 1. Purpose

Phase 16 identified conflicting records about whether three qualifying independent reviews (blind tests #1, #2, and #4) occurred. Phase 17 performs a bounded recovery sweep to see whether repository search surfaces locate the missing raw packages or event records.

## 2. Search results

The following searches were run against `utab5049/SIOS-Workspace-Standard`:

| Search surface | Query | Result |
|---|---|---|
| GitHub code search (default branch index) | `EV-BATCH-001` | No results returned |
| GitHub code search (default branch index) | `BLIND-TEST-PACKAGE-1` | No results returned |
| Commit search | `EV-BATCH-001` | No matching commits returned |
| Commit search | `BLIND-TEST-PACKAGE` | No matching commits returned |
| Commit search | `C1-RATIFIED-FINAL` | No matching commits returned |

The prior Phase 16 report also recorded 404 responses for these exact paths on the default branch:

- `02-Research/Registry/EV-BATCH-001.md`
- `02-Research/Registry/REVIEW-BATCH-001.md`
- `02-Research/Audit/Blind-Tests/BLIND-TEST-PACKAGE-1.md`
- `02-Research/Audit/Blind-Tests/BLIND-TEST-PACKAGE-2.md`
- `02-Research/Audit/Blind-Tests/BLIND-TEST-PACKAGE-4.md`
- `02-Research/Registry/APPLIED-CORRECTIONS-EV003-KSM001.md`
- `02-Research/Registry/CIR-001.md`
- `02-Research/Registry/EIR-001.md`

These results are limited. Code search covers the default branch index; commit-message search is not a complete Git object or historical-path audit. A 404 for an expected path does not establish that a file never existed, is absent from every branch, or cannot be recovered from another system.

## 3. What can and cannot be concluded

**Supported conclusion:** The repository search surfaces queried in this phase did not locate the named raw evidence packages or matching commits.

**Not supported:** That the reviews definitely did not happen; that reviewers were not independent; that the packages never existed; or that C1 should be rejected.

The claims of three independent reviews remain **unverified from the evidence located so far**. This is an evidence-status statement, not a negative finding about the underlying events.

## 4. Required next action

The governance owner should choose one of these controlled paths:

1. **Recover evidence:** Provide the original review packages, version-pinned artifacts, reviewer independence declarations, timestamps/event records, and traceable findings. Reconcile them against the review ledger before making a C1 decision.
2. **Record evidence unavailable:** If the original materials cannot be recovered after an owner-defined search, authorize an explicit status such as “unverified — source evidence unavailable,” retaining the search scope and date. Do not rewrite that status as “reviews did not occur.”
3. **Keep decision pending:** Leave the current C1 conflict unresolved until the authorized owner decides how to proceed.

The search itself does not authorize a change to `MAI-001`, `12-Registry/README.md`, `12-Registry/INDEX.md`, `C1-RATIFIED-FINAL.md`, or `DECISIONS-RECORDED.md`.

## 5. Acceptance criteria for a future evidence-based decision

Before a governance decision treats the reviews as qualifying independent reviews, the record should identify:

- The exact artifact/package version reviewed for each test.
- The original review output and a stable source location or content hash.
- Reviewer identity or accountable pseudonymous identifier, with an independence declaration and basis.
- Timestamped review event and traceable findings.
- The authority that accepts the evidence and the resulting decision.

Missing evidence must remain explicitly missing; it must not be reconstructed as fact from a summary claim alone.

# MAI-001 — Registry Delta v2 (Final, Consolidated)

**Supersedes:** MAI-001-REGISTRY-DELTA.md (v1)
**Status:** Proposed for Editorial Review merge, per AERA-001F §5.2 (Compatible Change)
**Date:** 2026-08-04

---

## What changed since v1

- EV-000001, EV-000002, EV-000005 corrections applied (EV-CORRECTIONS-BATCH-001.md) → all now Approved
- EV-000002 split into EV-000002a / EV-000002b
- KOM-001 added (was not yet drafted at v1)
- SRC-000015, SRC-000016 added (corpus gap closure, SRE-000001-E)
- SRE-000001-A status finalized as Failed (unchanged from v1, re-confirmed)

---

## Domain 02 — Research

### Search

| Artifact ID | Status | Version | Path |
|-------------|--------|---------|------|
| SRE-000001-A | Failed | 1.0.0 | 02-Research/Search/SRE-000001-A.md |
| SRE-000001-B | Draft | 1.0.0 | 02-Research/Search/SRE-000001-B.md |
| SRE-000001-C | Draft | 1.0.0 | 02-Research/Search/SRE-000001-C.md |
| SRE-000001-D | Draft | 1.0.0 | 02-Research/Search/SRE-000001-D.md |
| SRE-000001-E | Draft | 1.0.0 | 02-Research/Search/SRE-000001-E.md |

### Corpus / Sources

| Artifact ID | Status | Domain | Notes |
|-------------|--------|--------|-------|
| SRC-000002 – 000010 | Draft | A/B/C/D | Unchanged from v1 |
| SRC-000012 – 000014 | Draft | A/D | Unchanged from v1 |
| SRC-000015 | Draft | B (RQ-610) | **New** — Galárraga et al. 2014, DOI confirmed |
| SRC-000016 | **Draft — Conditional** | C/D (RQ-640) | **New** — DOI unconfirmed, Evidence extraction blocked pending verification |

### Evidence

| Artifact ID | Status | Version | Notes |
|-------------|--------|---------|-------|
| EV-000001 | **Approved** | 1.1 | *(was Needs Revision in v1)* — Support Level corrected E2→E1 |
| EV-000002 | **Superseded** | — | Replaced by split records below |
| EV-000002a | **Approved** | 1.0 | New, from split |
| EV-000002b | **Approved** | 1.0 | New, from split |
| EV-000003 | Approved | 1.0 | Unchanged |
| EV-000004 | Approved | 1.0 | Unchanged |
| EV-000005 | **Approved** | 1.1 | *(was Needs Revision in v1)* — Consistency field corrected |

**All 6 active Evidence Records (EV-000001, 002a, 002b, 003, 004, 005) now Approved.** See EV-CORRECTIONS-BATCH-001.md §"Important caveat" — "Approved" here still means single-session-pilot-approved, not independently reviewed by a separate party.

---

## Domain 03 — Framework

| Artifact ID | Status | Version | Path | Grounded In |
|-------------|--------|---------|------|-------------|
| KOM-001 | Draft | 0.1.0-draft.1 | 03-Framework/Specifications/KOM-001.md | EV-000001(rev.1.1), EV-000002a, EV-000002b |
| KSM-001 | Draft | 0.1.0-draft.1 | 03-Framework/Specifications/KSM-001.md | EV-000003, EV-000004 |

**Domain 03 now has 2 proposed artifacts** (was 0 before this pilot; 1 after Phase 3's first pass; 2 after this consolidation).

---

## Merge Readiness Assessment

| Artifact Group | Ready for Editorial Review merge? | Blocking issue |
|---|---|---|
| SRE-000001-A/B/C/D/E | ✅ Yes | None — execution records are historically accurate regardless of downstream status |
| SRC-000002–000015 | ✅ Yes | None |
| SRC-000016 | ❌ Not yet | DOI/venue unconfirmed |
| EV-000001, 002a, 002b, 003, 004, 005 | ⚠️ Conditionally | Real content is sound; "Approved" status caveat (no independent reviewer) should be carried into MAI-001 as a note, not silently dropped |
| KOM-001, KSM-001 | ⚠️ Conditionally | Same caveat — both explicitly Draft status already, so this is consistent, not a new problem |

**Recommendation:** Merge everything except SRC-000016 now. Carry the "single-session pilot, simulated review" caveat forward explicitly in MAI-001's Owner/Notes field for the Evidence and Framework rows, rather than letting "Approved"/"Draft" status alone imply a rigor level that wasn't actually reached. This is the same integrity principle applied consistently across this entire pilot — status labels should never claim more than the process actually delivered.

# MAI-001 — Registry Delta (Pilot Session, 2026-08-04)

**Purpose:** This is not a modification of the frozen MAI-001 file itself (that requires the governance process in AERA-001F §6). It is a **proposed delta** — the exact rows that would need to be added to MAI-001 §5 for the artifacts produced in this pilot session to be properly registered, per MAI-001's own Rule 1 ("No artifact may exist without a MAI-001 entry").

Until this delta is formally reviewed and merged, everything produced in this session (SRE-000001-B/C/D, the SRL/SRC batches, OBSU-BATCH-001, EV-BATCH-001, REVIEW-BATCH-001, KSM-001) exists **outside** MAI-001 — which is itself a small, self-contained instance of exactly the kind of gap EV-000003 documents at a larger scale. Flagging this explicitly rather than letting it recur silently.

---

## Proposed additions to Domain 02 — Research

### Search (extends existing table)

| Artifact ID | Status | Version | Path |
|-------------|--------|---------|------|
| SRE-000001-A | **Failed** *(status correction — was "Pending Empirical Retrieval")* | 1.0.0 | 02-Research/Search/SRE-000001-A.md |
| SRE-000001-B | Draft | 1.0.0 | 02-Research/Search/SRE-000001-B.md |
| SRE-000001-C | Draft | 1.0.0 | 02-Research/Search/SRE-000001-C.md |
| SRE-000001-D | Draft | 1.0.0 | 02-Research/Search/SRE-000001-D.md |

### Corpus (new sub-registry needed — SRC-000002 through SRC-000014 currently have no MAI-001 rows at all)

| Artifact ID | Status | Version | Path | Domain |
|-------------|--------|---------|------|--------|
| SRC-000002 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000002.md | C |
| SRC-000003 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000003.md | C |
| SRC-000004 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000004.md | C |
| SRC-000005 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000005.md | C |
| SRC-000006 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000006.md | C |
| SRC-000007 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000007.md | A |
| SRC-000008 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000008.md | B |
| SRC-000009 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000009.md | B |
| SRC-000010 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000010.md | D |
| SRC-000012 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000012.md | A |
| SRC-000013 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000013.md | D |
| SRC-000014 | Draft | 1.0.0 | 02-Research/Corpus/Sources/SRC-000014.md | D |

*(SRC-000011 intentionally skipped — reserved but unused in this batch, consistent with SIOS-ID-001 §13: "Identifiers SHALL NOT be reassigned.")*

### Evidence (new sub-registry needed)

| Artifact ID | Status | Version | Path |
|-------------|--------|---------|------|
| EV-000001 | Needs Revision | 1.0 | 02-Research/Evidence/Records/EV-000001.md |
| EV-000002 | Needs Revision | 1.0 | 02-Research/Evidence/Records/EV-000002.md |
| EV-000003 | **Approved** | 1.0 | 02-Research/Evidence/Records/EV-000003.md |
| EV-000004 | **Approved** | 1.0 | 02-Research/Evidence/Records/EV-000004.md |
| EV-000005 | Needs Revision | 1.0 | 02-Research/Evidence/Records/EV-000005.md |

---

## Proposed addition to Domain 03 — Framework

**This is the significant one** — Domain 03's MAI-001 table currently reads *"No frozen artifacts currently registered."* This pilot produces the **first artifact ever proposed for this domain**:

| Artifact ID | Status | Version | Path |
|-------------|--------|---------|------|
| KSM-001 | Draft | 0.1.0-draft.1 | 03-Framework/Specifications/KSM-001.md |

This is the first empirical validation that the Research → Framework dependency declared in AERA-001A §7 and AERA-001B §5 ("sios-framework depends on sios-research and sios-foundation") actually functions as a real artifact flow, not just a documented intention.

---

## Governance Note

Per AERA-001F §5.2, adding new artifacts to existing collections is classified as a **Compatible Change**, approvable via Editorial Review — the lightest governance tier. This delta should be straightforward to merge once the Needs Revision corrections (REVIEW-BATCH-001.md) are applied and independent review is genuinely obtained (not just simulated within a single session).

**Recommendation:** Do not merge EV-000001/002/005 or their downstream KSM-001 dependents until corrected. EV-000003, EV-000004, and KSM-001 (which relies only on those two) are the cleanest candidates for a first real merge.

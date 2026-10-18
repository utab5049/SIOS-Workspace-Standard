# SIOS Research Pilot — Final Report

**Date:** 2026-08-04
**Scope:** First end-to-end execution of the SIOS Research Pipeline (Search → Extraction → Review → Framework Synthesis → Architectural Self-Audit)
**Read time:** ~10 minutes

---

## TL;DR

Before this pilot, SIOS had a fully specified, frozen research methodology and **zero real evidence** produced by it. This pilot ran the pipeline for real, once, end-to-end, on 16 real academic sources. It worked. It also broke in a few small, specific, fixable places — and, notably, it found one genuine, previously-unknown flaw in SIOS's own constitution along the way. Nothing here should be treated as final or authoritative; every output below carries an explicit "single-session, no independent reviewer" caveat.

---

## 1. What Was Proven

| Pipeline Stage | Status | Evidence |
|---|---|---|
| Search & Source Registration | ✅ Works | 16 real sources registered (SRC-000002–000016), spanning 4 research domains, DOI/URL-traceable |
| Observation Extraction | ✅ Works | 14 observations, honestly marked by extraction depth |
| Evidence Creation | ✅ Works | 7 evidence records, correctly typed per EUM-001's taxonomy |
| Independent Review | ⚠️ Partially — see §4 | A critical review pass caught real errors in 3 of 5 first-round records and forced correction — but it wasn't independent in the way OPS-001 requires |
| Framework Synthesis | ✅ Works | 2 draft artifacts (KOM-001, KSM-001) — the first content ever proposed for the previously-empty 03-Framework domain |
| Registry Integration | ⚠️ Proposed, not merged | A full MAI-001 delta is ready but not yet formally reviewed/applied |

**Bottom line: the methodology, as specified across OUM-001/EUM-001/ERS-001/OPS-001, is executable and produces genuinely traceable output.** That was an open question before this pilot; it no longer is.

---

## 2. The Most Important Single Finding

**SIOS's own CSL-001 has cited RFC 2119 and RFC 8174 as normative external references since the Foundation Baseline freeze — but neither was ever registered in MAI-001.** This is a real, verifiable, self-referential gap: SIOS's constitution depends on something its own registry doesn't know about. It's a small, cheap fix (register both, or build a lightweight external-reference registry) — but it's exactly the kind of blind spot that only shows up when a system is actually *run*, not just read. The pipeline found this about itself, unprompted, on its first real execution.

---

## 3. What Broke, and What That Tells Us

| Problem | Root Cause | Fix Proposed | Governance Tier |
|---|---|---|---|
| OpenAlex API returns HTTP 429 on every attempt (7 attempts, 3 strategies, 2 sessions) | Infrastructure-level block, not query-specific | Amend SFA-001 to require empirical tier-availability checks before assuming Tier 1/2 access | Compatible |
| No mapping between OUM-001's 5 Observation Types and EUM-001's 12 Evidence Types | Never specified — surfaced only by actually doing the transformation | New EUM-001 §7.3 with an explicit mapping table | Compatible |
| No schema field for "evidence about SIOS's own artifacts" (needed for the RFC 2119/8174 finding) | ERS-001 assumes all evidence concerns external Sources only | New ERS-001 §11.1 (Cross-Reference Relationships) | Minor |
| Corpus was single-domain after the first search round | Normal — first pass, not a defect | Two follow-up search rounds closed it | N/A — resolved within the pilot |

**Notably: nothing found required Major or Breaking governance.** Every real problem this pilot hit was fixable with Editorial or Architecture Review — the lightest tiers AERA-001F defines. That's a small, real data point that SIOS's governance ladder isn't currently mismatched to the friction the project is actually experiencing.

---

## 4. What Did *Not* Get Solved (Say This Out Loud, Don't Bury It)

- **No genuinely independent reviewer existed at any point.** Every "Approved" status in this pilot was reached by the same reasoning process that produced the claim, run a second time. This is a real methodological gap, not a formality — it's precisely the failure mode OPS-001 §10.2 exists to prevent, and this pilot could not prevent it because no second party was available.
- **13 of 16 sources were only extracted at abstract-level, not full-text.** The claims built on them are honestly, correctly flagged as lower-confidence for exactly this reason.
- **Tier 1/2 database access (OpenAlex, Scopus, Web of Science) is confirmed non-functional from this environment.** This is now closed as a *known* limitation, not an open question — but it's still unsolved.
- **The MAI-001 registry delta was never actually merged.** Everything produced in this pilot technically still violates MAI-001's own Rule 1 ("no artifact may exist outside MAI-001") until someone applies it.

---

## 5. Recommendation

**Do not scale this pilot horizontally (more sources, more domains) before addressing the independent-review gap.** More output at the same review-rigor ceiling doesn't buy SIOS anything it doesn't already have. The highest-value next steps, in order:

1. Get a genuinely separate reviewer (human, or a different AI session with no access to this pilot's reasoning) to review the 7 Evidence Records and 2 Framework drafts.
2. Merge the three pending change proposals (MAI-001 delta, EUM-001/ERS-001 amendments, SFA-001 amendment) — small, low-risk, unblocks everything downstream.
3. Solve full-text access before doing more abstract-level extraction — it's the actual quality ceiling right now, not corpus size.

---

## Appendix — Full Artifact Index

*(All files below were produced across this pilot; see individual documents for full detail. This report is the entry point, not a replacement.)*

- **Search execution:** SRE-000001 through SRE-000001-E
- **Source/corpus registration:** SRC/SRL entries (3 batches)
- **Observation extraction:** OBSU-BATCH-001, plus SRC-000015/016 extractions
- **Evidence & review:** EV-BATCH-001, EV-CORRECTIONS-BATCH-001, REVIEW-BATCH-001
- **Framework drafts:** KOM-001, KSM-001
- **Architectural audit:** AC-001-REASSESSMENT
- **Change proposals:** CHANGE-PROPOSALS-EUM-ERS, PHASE-5-KICKOFF (§5.4, SFA-001 amendment)
- **Registry:** MAI-001-REGISTRY-DELTA-V2
- **Session administration:** SESSION-REPORT-001, OPENALEX-RETRY-FINAL, PILOT-SUMMARY-PHASES-0-4

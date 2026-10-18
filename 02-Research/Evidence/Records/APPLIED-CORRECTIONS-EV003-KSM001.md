# Applied Corrections — EV-000003 (rev. 1.1) and KSM-001 §4.1 (rev.)

**Source of both fixes:** Blind Test #4, Q1 and Q3 — the first blind test result in this entire engagement to specify a fix this precise (split-by-temporal-scope) rather than a general caution.

---

## Correction 1 — EV-000003, claim split by temporal scope

### Identity
Evidence ID: EV-000003
Version: **1.1** *(was 1.0)*

### Evidence Content (revised)

**Claim (split into two sub-claims, per ERS-R-001):**

**Sub-claim A — point-in-time (Support Level: E3, unchanged):** *"As of 2026-08-04, RFC 2119 and RFC 8174 are cited in CSL-001 Appendix C as adopted external normative references, and neither is registered as a Source in MAI-001."* Directly verified against both primary texts and the current document set — this part of the claim carries the original, justified E3/High confidence.

**Sub-claim B — historical continuity (Support Level: E1, new, downgraded):** *"This unregistered status has held continuously since the Foundation Baseline v1.0 freeze (2026-07-14)."* **Not directly verified** — no registry-history snapshot from 2026-07-14 was checked; this is an inference from CSL-001's Frozen date, not a confirmed continuous-absence record. Downgraded to E1 (assertion, pending historical verification) per Test #4's finding.

**Context Summary (unchanged):** AERA-001D §10 and MAI-001 §3 still apply as originally stated; the split above changes confidence attribution, not the underlying finding.

**Overall Approval Status:** Unchanged — "Needs Revision (pending independent review)" — this correction *is* that revision, applied.

---

## Correction 2 — KSM-001 §4.1, paraphrase flagged

**Original text:** *"...remains unregistered in the citing project's own artifact registry (MAI-001), for an extended period, without the citing specification's own status (Frozen) being affected."*

**Revised text:**

> "...remains unregistered in the citing project's own artifact registry (MAI-001), **for an extended period** *(qualitative paraphrase of EV-000003's dated claim — the original evidence anchors this to 2026-07-14 specifically; see EV-000003 Sub-claim A/B for the precise, confidence-differentiated version. This section's wording SHOULD NOT be cited as an independent source for the exact time period — refer to EV-000003 directly for that.)*, without the citing specification's own status (Frozen) being affected."

**Classification of both fixes:** Compatible — precision corrections to existing content, no new claims introduced, no structural change.

---

## Net effect

Both of Test #4's specific findings are now applied, not just noted. **This is the first blind test in the sequence whose fix required no reconstruction, no test-methodology correction, no reclassification of severity — a direct, surgical edit, done.**

## Decision 1 (C1) — status update, decision remains yours

Three real tests have now run: #1 (confirmed + refined the RFC finding), #2 (caught a genuine overclaim, corrected), #4 (confirmed the pipeline mostly holds, two precise fixes applied — verdict explicitly "not a fundamental problem"). Test #3's negative verdict is now understood to have been testing a flawed excerpt, not the real artifacts.

**This is meaningfully stronger evidence than existed when you chose 1B.** Whether it's now sufficient to move to ratification, or whether you want one more sample checked, is your call to make — consistent with the same reasoning you gave for choosing 1B in the first place.

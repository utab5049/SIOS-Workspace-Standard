# REVIEW-BATCH-002 — Adversarial Fresh Review

**Method:** Deliberately re-examined every Evidence Record against the newly-acquired full-text material (FULLTEXT-UPGRADE-005-012.md), actively looking for contradictions, mis-scoping, or overclaiming — not re-confirming prior conclusions. This is still not genuine reviewer independence (same session), but it is methodologically different from REVIEW-BATCH-001: that pass checked internal consistency of each record; this pass checks records **against each other and against newly available full text**, which is where the most interesting problems were found.

---

## Finding 1 — A Real, Internal Contradiction: EV-000001's "Consistent" Label Was Wrong

**What was claimed:** EV-000001 (Gruber's 1993 ontology definition) had its `Consistency` field marked "Consistent," strengthened by SRC-000016's independent citation of the same definition.

**What the full-text pass just found:** SRC-000005's full text (§2.1) explicitly grounds its own working definition of "ontology" in **Studer et al. (1998)** — "a formal, explicit specification of a shared conceptualization" — not Gruber (1993). This is a different, later, and arguably now more widely-adopted canonical definition in the ontology engineering literature. SRC-000005 does not even cite Gruber 1993 in its background section.

**This means:** the corpus now contains **two competing canonical definitions of "ontology"** (Gruber 1993 vs. Studer et al. 1998), cited by different sources for the same foundational concept, and EV-000001's "Consistent" label — which was based on only checking agreement with SRC-000016 — did not check against SRC-000005, where a genuine alternative exists.

**Correction required:**
- `Consistency` field on EV-000001: **"Conflicting"** → more precisely, **"Partially Consistent — competing canonical definition documented in corpus"**, not simply "Consistent."
- **New evidence needed, not yet in this corpus:** a source establishing which definition (or whether both) is considered authoritative in current practice. This pilot does not currently have that source — flagged as an open item rather than guessed at.
- **This is a genuine, non-trivial finding for KOM-001** (which currently states the Gruber definition as its sole §3.1 anchor without noting this competing alternative). KOM-001 should be revised to note this before being treated as settled, even at Draft status.

**Why this matters beyond just fixing one field:** This is exactly the kind of error that a same-session, non-independent review is structurally prone to missing — REVIEW-BATCH-001 checked each record in isolation and found real errors, but it never cross-checked EV-000001 against evidence gathered *later* in the same pilot (SRC-000005's full text wasn't available yet during that review). This is itself evidence for why genuine independent review, done at the *end* of a research cycle rather than mid-stream, matters — a point worth carrying into the "independent review" recommendation generally, not just as a one-off correction.

---

## Finding 2 — A Genuine Strengthening: EV-000004 Has a Corroborating Example It Didn't Cite

**What was claimed:** EV-000004 contrasts SIOS's Board-approval governance model with NRC (1995)'s abstract description of voluntary consensus standards processes.

**What this review pass noticed:** SRC-000013 and SRC-000014 (RFC 2119, RFC 8174) are not just *subjects* of EV-000003 — they are themselves **concrete, real-world instances** of exactly the consensus-based standards process NRC (1995) describes in the abstract. IETF's RFC process (rough consensus, working-group review, formal Best Current Practice status) is a live, currently-operating example of the governance model EV-000004 discusses only abstractly via a 1995 committee report.

**Correction:** EV-000004 should be updated to cite SRC-000013/SRC-000014 as a **second, concrete corroborating source**, not just NRC's general account. This makes the finding stronger and more falsifiable (a reader can now go look at an actual, currently-functioning IETF process rather than only a 1995 description of the category).

**No content in EV-000004's core claim changes — only its evidentiary strength improves.**

---

## Finding 3 — A Legitimate Scope Correction: The ERS-001 Amendment (Proposal 2) May Be Targeting the Wrong Specification

**Re-examining CHANGE-PROPOSALS-EUM-ERS.md's Proposal 2** (adding a "Cross-Reference Relationships" field to ERS-001 for evidence like EV-000003) with fresh skepticism:

RFC 2119 and RFC 8174 are not really "Evidence" in the EUM-001/ERS-001 sense — they are **normative external standards** that CSL-001 depends on, closer in kind to a dependency than a research finding. AERA-001D §10 (Dependency Rules) already states "every dependency SHALL be explicitly declared in MAI-001" — this suggests the *real* fix belongs in **AERA-001D or MAI-001's own registration schema** (adding an "External Normative Reference" artifact type/registration path), not in ERS-001's Evidence Record schema.

**Framing EV-000003 as an "Evidence Record" at all may have been a category mismatch from the start** — useful for demonstrating the pipeline's ability to surface findings, but not the natural long-term home for this kind of dependency-tracking fact.

**Revised recommendation:**
1. Keep EV-000003 as-is for this pilot's own record (it correctly demonstrates the finding).
2. **Redirect the actual fix** toward AERA-001D (add an "External Normative Reference" registration category, distinct from SRC-XXXXXX research sources) rather than ERS-001.
3. ERS-001's Proposal 2 (cross-reference relationships) may still have independent merit for *other* future cases where Evidence genuinely does concern SIOS's own artifacts (e.g., a future finding that critiques an SIOS specification's internal consistency) — but should not be justified primarily by the RFC 2119/8174 case, which has a cleaner home elsewhere.

---

## What This Adversarial Pass Did *Not* Find

For completeness (a review that only ever finds problems is as suspicious as one that never does): EV-000002a, EV-000002b, EV-000006, EV-000007, EV-000008, and EV-000009 were re-checked against all newly available full text and **no contradictions or mis-scoping were found** in any of them. They remain as previously assessed.

---

## Updated Status Table

| Evidence ID | Status After This Pass | Change |
|---|---|---|
| EV-000001 | **Needs Revision (again)** | Consistency field must be corrected; competing definition must be disclosed |
| EV-000002a, 002b | Approved (unchanged) | — |
| EV-000003 | Approved (content unchanged) | Recommendation retargeted from ERS-001 to AERA-001D |
| EV-000004 | Approved (strengthened) | Add SRC-000013/014 as second corroborating source |
| EV-000005 | Superseded by EV-000009 | (per FULLTEXT-UPGRADE-005-012.md) |
| EV-000006, 007 | Approved (unchanged) | — |
| EV-000008, 009 | Approved (new, full-text-grounded) | — |

**This is the correct outcome for a real second review pass: not zero new problems, and not so many that the first pass looks worthless — a small number of substantive, specific corrections, exactly at the depth a genuinely careful reviewer should find on a second, differently-angled look.**

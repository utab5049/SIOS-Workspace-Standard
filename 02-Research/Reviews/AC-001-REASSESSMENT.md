# AC-001 — Reassessment Note (Post-Pilot)

**Applies to:** AC-001 (Architecture Candidate — Core Layer)
**Basis:** Empirical friction from Phases 1–3 of this pilot (real search, extraction, review, synthesis)
**Date:** 2026-08-04
**Status:** Advisory — not a governance decision; input for Architecture Board review

---

## 1. Purpose

AC-001 §6 lists four conditions under which the Core Layer candidate may be promoted to formal architecture. This note evaluates each condition against what actually happened in Phases 1–3 — not against speculation, per AC-001's own governing principle (RP-005, Evidence Primacy).

---

## 2. Condition-by-Condition Assessment

### 2.1 Condition 1 — Architectural Problem (AC-001 §7.1)

*"A real architectural problem is identified that cannot be resolved without a Core Layer."*

**Evidence from this pilot:** A real duplication/inconsistency problem **was** found — OUM-001's Observation Types (5: Definition, Claim, Method, Finding, Limitation) and EUM-001's Evidence Types (12: DEF, CLM, FND, REL, MOD, MTH, FRM, PRN, CRT, GAP, HYP, REC) have no documented mapping, discovered only because this pilot actually tried to transform Observations into Evidence and had to improvise the mapping ad hoc (see §3 below for the resolution).

**Assessment:** This is real, but it is a **within-domain** inconsistency (both OUM-001 and EUM-001 live in 02-Research), not a **cross-domain** duplication of canonical concepts as AC-001 §7.1's example describes ("Repeated duplication of canonical models across multiple domains"). **Condition 1 is not met** by this finding — the fix belongs at the specification level (§3), not the architectural-layer level.

### 2.2 Condition 2 — Repeated Dependencies (AC-001 §7.2)

*"Repeated dependencies between domains are observed that a Core Layer would centralize... multiple domains independently defining the same canonical concepts."*

**Evidence from this pilot:** None observed. The pilot touched 02-Research and 03-Framework only; no independent, conflicting canonical concept definitions were found across domains. **Condition 2 is not met.**

### 2.3 Condition 3 — Operational Need (AC-001 §7.3)

*"An operational need is demonstrated in Research, Runner, or Publications that requires a shared Core. Example: Evidence extraction requires a common entity model across all sources."*

**Evidence from this pilot:** Evidence extraction was performed across 15 sources without needing a shared cross-domain entity model — SRC-000001's schema was sufficient and consistent throughout. **However**, a related but narrower operational need *was* found: the Observation→Evidence type mapping gap (§2.1). This is a genuine operational friction, but — again — it is resolvable within 02-Research's existing specifications (OUM-001/EUM-001), not evidence that a cross-domain Core Layer is needed. **Condition 3 is not met** in the form AC-001 describes it, though a narrower, related need is real (see §3).

### 2.4 Condition 4 — Audit Finding (AC-001 §7.4)

*"An Architecture Audit identifies the absence of a Core Layer as a significant architectural debt."*

**Evidence from this pilot:** This pilot functioned as an informal audit (it found the RFC 2119/8174 traceability gap, the type-mapping gap, and a third gap discovered just now — see §4). None of these three findings were attributed, on inspection, to the *absence of a Core Layer* specifically. All three are fixable as targeted, Minor/Compatible changes to existing specifications. **Condition 4 is not met.**

---

## 3. Resolution of the Type-Mapping Gap (Immediate, Small Fix — Not Core Layer)

| OUM-001 Observation Type | Primary EUM-001 Evidence Type Mapping | Notes |
|---|---|---|
| Definition | DEF | Direct |
| Claim | CLM | Direct |
| Method | MTH | Direct |
| Finding | FND | Direct |
| Limitation | GAP (primary) or CRT (secondary, if framed as a critique of an existing approach) | One-to-many — context-dependent |

**The remaining 7 EUM-001 types (REL, MOD, FRM, PRN, CRT, HYP, REC) have no Observation-type source.** This pilot's own extraction confirms this is not an oversight but a structural feature: these types are produced *during the interpretive step* (OUM-001 §9, Observation → Context Analysis → Quality Assessment → RQ Mapping → Evidence), not inherited from any single Observation Type. Any of the 5 Observation Types can, in principle, be interpreted into any of these 7 types depending on context.

**Recommendation:** Add this mapping table (or an equivalent) as a new subsection in EUM-001 (e.g., §7.3, "Relationship to Observation Types") — classified as a **Compatible Change** per AERA-001F §5.1 ("clarifying existing conventions"), approvable via Editorial Review. **No Core Layer required.**

---

## 4. A Genuinely New Finding, Surfaced Only While Writing This Reassessment

While mapping types (§3), it became clear that **EV-000003** (the RFC 2119/8174 traceability-gap record — this pilot's strongest Evidence Record) does not fit the OUM-001 §9 pipeline (`Observation → Context Analysis → Quality Assessment → RQ Mapping → Evidence`) at all. It was not produced by interpreting a single Observation. It was produced by **comparing two Observations (OBSU-000007, OBSU-000008) against a third artifact entirely — CSL-001 and MAI-001 themselves**, which are not Sources in the SRC-000001 sense (they are SIOS's own constitutional documents, never registered as SRC-XXXXXX).

**This means the pipeline as currently specified (OUM-001/EUM-001/ERS-001) has no documented mechanism for "cross-reference audit" evidence** — evidence whose claim is about the *relationship between a Source and SIOS's own artifacts*, rather than about the Source's content alone. GAP-type evidence in particular seems to frequently need this (a "gap" is inherently relational — gap *between* something and something else).

**This is a real, freshly-discovered gap in the Research pipeline's own model** — smaller in scope than a Core Layer (Condition 4 still not met), but real enough to warrant its own note rather than being silently absorbed into the type-mapping fix above, since it's a process gap, not a taxonomy gap.

**Recommendation:** Raise as a candidate Minor Change to OUM-001 or ERS-001 — perhaps a new Evidence sub-category or explicit note that GAP/CRT-type evidence may cite SIOS's own artifacts as a comparison target, with a lightweight rule for how that's traced (since ERS-001 §6's `Source ID` field assumes an external SRC, not an internal SIOS document).

---

## 5. Governance-Weight Observation (Non-Binding)

Separately from AC-001 specifically: across Phases 1–3, every fix identified (§3, §4, and the earlier RFC 2119/8174 registration gap) was classified, under AERA-001F's own change taxonomy, as **Compatible or Minor** — the lightest governance tiers. Nothing encountered in real pilot use has yet required Architecture Board + Constitutional Governance (Major) or ADR-level (Breaking) process. This is mild, real evidence that the AERA-001F governance ladder, as designed, is *not* being triggered disproportionately by normal early-stage friction — a small positive data point on the "is the governance too heavy for this stage" question raised earlier in this project's review, though one pilot session is far too little evidence to treat this as settled.

---

## 6. Conclusion

**AC-001's Core Layer remains correctly un-promoted.** None of its four promotion conditions were met by real friction encountered in Phases 1–3. What *was* found — the type-mapping gap and the cross-reference-evidence gap — are both real, both worth fixing, and both fixable as small, Compatible/Minor changes to existing 02-Research specifications, exactly the outcome AC-001 §6's original rejection rationale ("no critical dependency... no existing domain depends on a shared Core that cannot be satisfied through current architecture") predicted would happen if the Core Layer were genuinely unnecessary at this stage.

**This is itself a small piece of evidence *for* AC-001's original 2026-07-14 decision, discovered nine months of pilot time later** — the architecture held up under its first real load without needing the deferred abstraction.

---

## Appendix A — Relationship to Other Documents

| Document | Relevance |
|---|---|
| AC-001 | Subject of this reassessment |
| OUM-001, EUM-001 | Target of the §3 mapping-table recommendation |
| ERS-001 | Target of the §4 cross-reference-evidence recommendation |
| EV-000003 | The record whose extraction process revealed §4's finding |
| AERA-001F | Governance-tier classification applied throughout |

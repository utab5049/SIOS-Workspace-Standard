# SIOS — Adversarial Architecture Validation Report (Part 1 of 3)
## Phases 0–5: Reconstruction → Claim Register → Assurance Scorecard

**Reviewer role:** Acting as Chief Architecture Assurance Reviewer per the supplied protocol.
**Basis:** The full set of ~40 SIOS constitutional/specification documents, plus the complete artifact trail of the 2026-08-04 research pilot (~50 files), plus two prior external reviews of the pilot's summary documents (uploaded materials, hereafter "External Review A" and "External Review B").
**Date:** 2026-08-04

---

# PHASE 0 — REVIEW CONTRACT (Acknowledged)

Rules 1–5 apply throughout. Every claim is labeled FACT / SPECIFICATION / PILOT EVIDENCE / INFERENCE / HYPOTHESIS / UNKNOWN. No specification is assumed implemented unless pilot evidence exists. No pilot success is generalized into a reliability claim without an explicit falsification test.

**Disclosed before Phase 1 begins (relevant to Phase 9 later):** this review is conducted by the same kind of system (an LLM) that produced the artifacts under review, and by the same model family that ran the original pilot. This is not a neutral starting position, and is treated as evidence-relevant throughout, not hidden until Phase 9.

---

# PHASE 1 — RECONSTRUCT THE ACTUAL ARCHITECTURE

## 1.1 Architectural Layers

| Layer | Purpose | Owner | Artifacts | Inputs | Outputs | Dependencies | Validation | Governance Authority |
|---|---|---|---|---|---|---|---|---|
| **00-Program** | Program governance, vision, roadmap | [SPEC — AERA-001A] | Program-Manifest | Constitutional principles | Program scope | None | UNKNOWN — no validation mechanism specified | Architecture Board (inferred) |
| **01-Foundation** | Constitutional identity, architecture, standards | Architecture Board | SIOS-BASELINE-001, SIOS-MAN-001, AERA-001A–F, CSL-001, SIOS-ID-001, MAI-001, ADR-0001–4, AC-001 | None (root layer) | Constitutional constraints on all other layers | None | Frozen = passed internal review at freeze time [FACT]; no external validation demonstrated before this review [PILOT EVIDENCE] | Architecture Board + Constitutional Governance |
| **02-Research** | Evidence-based knowledge production | Research Program | RQD-001, SFA-001/002, SQP-001, SRE-001, SRL-001, SRC-000001, COR-001–3, OUM-001, EUM-001/001B, ERS-001, OPS-001, + pilot-added CIR-001/EIR-001 | Foundation constraints, external sources | Registered evidence, corpus | Foundation | **PILOT EVIDENCE**: executed once, end-to-end, 2026-08-04, producing 19 sources and ~12 evidence records | Research Program; Architecture Board for structural changes |
| **03-Framework** | Canonical models, standards | Framework Program | PRE-PILOT: empty [FACT, per MAI-001]; POST-PILOT: KOM-001, KSM-001 (both Draft) | Research + Foundation | Standards | Research, Foundation | **PILOT EVIDENCE**: first-ever content, 0.1–0.2 draft versions, self-flagged incomplete | Framework Program; Architecture Board |
| **04-Runner** | Research automation | Tools/Runner | ARR-001, 001A–C | SQP-001 queries | SRL-001 records | Foundation, Research | **SPECIFICATION ONLY** — ARR-001C never executed once (OpenAlex unreachable); Crossref confirmed reachable but untested against actual Runner code | ADR-driven for provider swaps |
| **05–15 domains** | Various | Various programs | Mostly [UNKNOWN — not populated in supplied documents] | — | — | — | **INSUFFICIENT EVIDENCE** | UNKNOWN |
| **Pilot-added registry sub-layer** | Instance-level tracking without inflating MAI-001 | Delegated pilot authority | CIR-001, EIR-001, ENR-000001/2 | Corpus/Evidence instances | Indexed, traceable instance records | MAI-001 | **PILOT EVIDENCE** — created and populated once; never independently reviewed | Delegated authority only — **not yet ratified by any authority independent of this same reasoning chain** |

## 1.2 Artifact Lifecycle

**Three partially-overlapping lifecycles exist and are not reconciled:**
- AERA-001D §5: `Proposed → Draft → Review → Approved → Frozen → Deprecated → Archived` [SPEC]
- EUM-001 §8: `Candidate → Reviewed → Accepted → Registered → Linked → Dataset` [SPEC, evidence-specific]
- OPS-001 §11.2: `Candidate Evidence → Review → Acceptance → Assign EV-XXXXXX → Register` [SPEC, operational]

No document maps these onto each other. [FACT.] This mirrors the same category of gap the pilot found between OUM-001/EUM-001's type taxonomies — a **repeating pattern**, not an isolated incident (see Phase 14).

**"Consumption" is not modeled anywhere.** No specification defines what happens when an Approved/Frozen artifact is *used* by a downstream process. **This is the precise gap both External Review A and B independently flag as the deepest issue — a convergent finding across three independent analyses.**

**"Deprecation/Retirement" for Evidence records is unspecified.** ERS-001 §5 lists "Archived" as a status but not the evidentiary conditions for reaching it, nor what happens to Framework artifacts that depended on now-archived evidence (tested in Phase 6, Scenario J).

## 1.3 Dependency Graph

**Hard dependencies (AERA-001B §5):** Research→Foundation; Framework→Research,Foundation; Runner→Research,Foundation; Datasets→Research; Publications→Framework.

**Soft dependencies:** Framework artifacts softly depend on specific Evidence Records via prose traceability tables — soft because **nothing mechanically enforces the link; it can go stale silently.**

**External dependencies:** every SRC-XXXXXX source; RFC 2119/RFC 8174 (via CSL-001); OpenAlex/Crossref APIs.

**Hidden dependencies — using RFC 2119/8174 as the protocol's specified test case:**
CSL-001 §5 (Frozen 2026-07-14) declares these as adopted normative references. AERA-001D §10 requires every dependency be declared in MAI-001. **This was violated for the project's entire life until an unrelated research pilot happened to discover it.** [FACT.]

**The deeper finding:** discovery was accidental. A search query for "standards development methodology" happened to surface the RFCs, triggering a manual cross-check. **No mechanism in SIOS today would find a similar gap without a coincidental adjacent search.** Carried forward to Phase 14 and Phase 8.

**Unregistered dependencies (current state):** 19 sources and ~12 evidence records exist as real files, cited by KOM-001/KSM-001, whose MAI-001 registration depends on a governance decision (Option B) made under delegated, non-independent authority. **The pilot's own output currently sits in the same kind of provisional state as the exact problem it discovered and fixed.**

**Circular dependencies:** none found [FACT, from available documents] — but never computationally verified, only asserted (Phase 14).

## 1.4 Trust Boundaries

| Boundary | Location | What Crosses It | Trust Established By |
|---|---|---|---|
| B1 — Info enters SIOS | Search execution | Raw external text | Nothing — raw ingestion |
| B2 — Interpretation begins | Observation extraction | Extracted statement | **Weak** — selection-of-what-to-extract is itself interpretive, unaddressed by OUM-001 |
| B3 — Interpretation becomes Evidence | EUM-001 §9 | Observation + judgment | Self-assigned Quality Profile — **no independent quality assessment ever occurred** |
| B4 — Evidence becomes Knowledge | Framework synthesis | Approved Evidence only | The Evidence's own self-assigned Approved status |
| **B5 — Knowledge can influence Decision** | **UNSPECIFIED ANYWHERE** | UNKNOWN | **Does not yet formally exist** |
| B6 — Where humans are required | OPS-001 §10.2 (nominal) | — | **Never satisfied once in the entire pilot** |
| B7 — Where AI reasoning is trusted | Effectively all of B1→B4 | — | Nothing external to the reasoning process itself |

**Finding: B5 does not exist as a defined boundary.** This is the single most consequential fact this reconstruction surfaces, and the same gap both External Reviews independently converged on.

---

# PHASE 2 — ARCHITECTURAL CLAIM REGISTER

| # | Claim | Type | Evidence Level | Falsification Condition | Current Status |
|---|---|---|---|---|---|
| 1 | Every normative requirement is traceable to origin | SPEC (CP-005) | **E3** | Find a normative claim with no traceable path | Substantiated within research pipeline; untested at decision layer |
| 2 | No artifact exists outside MAI-001 | SPEC (MAI-001 §3) | **E1** claimed, **falsified twice** (RFC 2119/8174; then the pilot's own unmerged output) | Any artifact in active use with no MAI-001 path | Actively false at time of this review |
| 3 | E1–E4 grading differentiates reliability meaningfully | SPEC | **E2** | Compare E1 vs E4 claims against later ground truth | Never tested against ground truth |
| 4 | Independent review exists and functions | SPEC + CLAIMED | **E1** claimed, **E0** executed | Find one review with a reviewer lacking access to producer's reasoning | **Falsified in every instance across the pilot** |
| 5 | Self-audit capability exists | INFERENCE | **E3** | A planted flaw the pipeline fails to detect | Strongest substantiated claim; **sample size = 1** |
| 6 | Governance tiering correctly classifies changes | SPEC (AERA-001F §5) | **E3**, self-assessed | An externally-reviewed change gets reclassified higher | Applied 5+ times, never independently checked |
| 7 | Results are reproducible by another party | SPEC (SRE-001 §11.2) | **E0** | A second party gets materially different results | Never tested |
| 8 | Corpus selection controls for bias | SPEC (CSP-001–007) | **E2**, partial **E3** | A CSP-compliant corpus still measurably skewed | Applied qualitatively; no quantitative measurement |
| 9 | Evidence Saturation correctly signals stop-search | SPEC (CSP-007) | **E1** | A "saturated" corpus later substantially contradicted | Invoked rhetorically; never formally measured |
| 10 | KOM-001/KSM-001 content is factually correct | SPEC target | **E2 at best** | Expert review finds material error in an "Approved" claim | Self-disclosed incomplete; never externally checked |
| 11 | SIOS depends on no proprietary technology (CP-007) | CONSTITUTIONAL | **E1**, **near-violation found** | A Frozen doc names a vendor-specific technology | Not violated in Frozen content; violation caught in an unratified diagram |
| 12 | Freeze permits controlled additive evolution | GOVERNANCE PRINCIPLE | **E3** | A Frozen doc requires retroactive rewrite | Held in 3+ tested amendments |
| 13 | 03-Framework is a functioning domain | SPEC | **E0 pre-pilot → E3 post-pilot** | — | Zero artifacts until this pilot |
| 14 | Dependency graph is acyclic | SPEC (AERA-001D §10.1) | **E1** | A computational trace finds a cycle | Asserted, never verified |
| 15 | Runner (ARR-001) is tool-neutral and functions | SPEC | **E2** | Runner code interprets/modifies data once run | **Never executed once** |
| 16 | Evidence-to-Framework traceability is complete | PILOT-DEMONSTRATED | **E3** | A Framework claim with no EV-ID | Held throughout pilot |
| 17 | Validated knowledge is fit to ground real decisions | IMPLIED, never formally claimed | **E0** | — | **Wholly untested — the central open question across all three reviews** |
| 18 | Architecture functions at scale | IMPLIED | **E1 at most** | 100–1000× corpus loses guarantees | Never tested; explicitly deferred |
| 19 | Multiple independent reviewers produce non-correlated judgments | **NOT CLAIMED ANYWHERE** | **E0** | — | Absent from SIOS's self-model (Phase 9) |
| 20 | SIOS surfaces failures visibly, not silently | INFERENCE | **E2 at best** | A planted error goes undetected with no signal | One success case; no systematic guarantee (Phase 8) |

---

# PHASE 3 — ARCHITECTURE ASSURANCE SCORECARD

**Methodological note:** External Review B scored 10 dimensions from two summary documents only (7.0/10 average, explicitly flagged as "misleading" by its own author). This review has access to the full underlying artifact set, including full-text-extraction progress that postdates External Review B (10 of 19 sources reached full-text by pilot's end, vs. "13 of 16 abstract-only" at the time B was written). Score differences below reflect data availability, not methodological disagreement.

| # | Dimension | Score | Strongest Positive | Strongest Negative | Failure Mode | Required Proof |
|---|---|---|---|---|---|---|
| 1 | Architectural coherence | **8/10** | End-to-end pipeline executed once, real artifacts every stage | Kernel Diagram (unratified) already shows drift risk | New layers bolted on without reconciling vocabulary | A second pilot outside this self-referential domain |
| 2 | Provenance | **8/10** | Every source DOI/URL-traceable; RFC finding precisely traced | 9 of 19 sources still abstract-only | Silent staleness | Automated link-integrity checking |
| 3 | Traceability | **8/10** | Explicit tables in every artifact | Manual/asserted, not mechanically enforced | Table silently stale after EV revision | Tooling that breaks build on untracked EV changes |
| 4 | Evidence integrity | **6/10** | 10/19 full-text by pilot's end | Quality profile self-assigned, never ground-truthed | Confident-sounding but unverified E3/E4 labels | Ground-truth comparison study |
| 5 | **Review independence** | **2/10** | Review process demonstrably catches real errors when simulated (3 of 5 first records corrected) | **Zero genuinely separate reviewer instances across the entire pilot** | Confident false approval | The experiment specified in Phase 18 |
| 6 | Knowledge transformation integrity | **5/10** | OUM/EUM type-mapping gap found and fixed | RFC finding revealed a *third*, undocumented transformation path not modeled at all | Evidence forced into ill-fitting categories or dropped | Formal audit of every EV against its actual pipeline path |
| 7 | Governance | **8/10** | 3 real changes correctly routed, retroactivity avoided | All decisions made under delegated, unratified authority | A "Compatible" change turns out Breaking | Independent governance review of pilot's 5 proposals |
| 8 | Self-audit | **8/10** | EV-000003: genuine, unprompted, self-discovered gap | Sample size 1; mechanism was accidental, not systematic | Silent gaps of the same category persisting | A second, independently-triggered finding |
| 9 | Operational resilience | **5/10** | Did not halt on OpenAlex failure; diagnosed Crossref alternative | 8 failed attempts before diagnosis; ARR-001C never actually run | Silent degradation to lower-quality source | Monitored multi-session uptime test |
| 10 | Scalability | **3/10** | Registry design anticipates scale conceptually | Zero empirical data beyond 19 sources | Overhead outpacing usable output | Phase 12's scale model, executed |
| 11 | **Decision fitness** | **2/10** | None found | Boundary B5 does not exist | "Knowledge" used to justify real action with no fitness check | Phase 13's test |
| 12 | Evolvability | **7/10** | 3 additive amendments succeeded without reopening Frozen content | All within one pilot, one set of hands | Governance backlog outpacing review capacity | Sustained multi-contributor change stream |

**Overall maturity — NOT a simple average.** Dimensions 5 and 11 are treated as critical blockers that cap the score, because every other dimension's evidence traces through a never-independent review process, and the pipeline's entire stated purpose has no demonstrated endpoint.

**Capped overall score: 4.5 / 10.** This is not an average of the table (~6.2) but a capped assessment — independently landing close to External Review B's own itemized "Real-world Decision Fitness — 4.5/10," arrived at here by a different method (architectural capping vs. single-dimension floor).

---

*[Continued in Part 2: Phases 4–10]*

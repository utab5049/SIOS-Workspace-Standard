# SIOS — Consolidated Roadmap

**Date:** 2026-08-04
**Synthesizes:** The research pilot (Phases 0–4, full-text extraction, corrections) and the strategic discussion (Architect's Trap, Persona, Reference Implementation, ARS-001, Kernel Diagram)

---

## Why These Two Tracks Are Now One Roadmap, Not Two

The research pilot just spent several sessions proving, end-to-end, that Source → Observation → Evidence → Framework works, self-corrects, and produces traceable output. The strategic discussion, separately, called for exactly this kind of thing — a Reference Scenario (ARS-001) that lets someone understand SIOS in 15 minutes by following one real example through the whole pipeline. **These are not two separate deliverables. The pilot's own KOM-001/KSM-001 trace, run on a real domain, is most of what ARS-001 needs to be.** The roadmap below reflects that convergence.

---

## Priority 0 — Blocking, Do First

### P0.1 — Get Genuine Independent Review
Every "Approved" status across this entire pilot carries the same caveat, repeated so many times it risks becoming background noise instead of a real blocker. It needs to stop being a caveat and become an actual task: hand FORMAL-REGISTRATION-PACKAGE.md, EIR-001, and KOM-001/KSM-001 to a person or a genuinely separate AI session with zero access to this pilot's reasoning trail, and get real disagreement recorded. Nothing downstream (ratification, ARS-001 construction, further corpus scaling) should be treated as settled before this happens at least once.

### P0.2 — Ratify or Reject the Two Structural Governance Decisions
DECISION-MAI001-OPTION-B.md and the AERA-001D §7.3 amendment were made under delegated pilot authority, not real governance authority. Someone with actual Architecture Board standing needs to formally accept or reject them. This is fast (both are additive, low-risk) but shouldn't be skipped just because it's low-risk.

### P0.3 — Register ENR-000001/ENR-000002
Mechanical, five-minute task once P0.2 clears. This is the one item in the entire pilot that isn't "propose a fix" — it's "apply the fix." Do it as soon as §7.3 is ratified.

---

## Priority 1 — Converge the Two Tracks (ARS-001)

### P1.1 — Decide Persona and Domain Together, Not Separately
Per the earlier strategic exchange: don't finalize "Manufacturing" and "which audience" as independent decisions. Recommendation carried forward from that discussion: **lean toward an LLM/RAG-infrastructure-team persona**, given how well OUM-001/EUM-001/ERS-001's actual design (confidence grading, traceability, provenance) matches that audience's real pain points. If that persona is adopted, weigh a knowledge-dense domain (legal research, technical documentation, or — as this pilot incidentally demonstrated — **SIOS's own research methodology domain**) alongside Manufacturing, not instead of it, before finalizing.

### P1.2 — Build ARS-001 *From This Pilot's Actual Trace*, Not From Scratch
This pilot already has a complete, real, traceable run: 16 sources → 14 observations → 11 evidence records → 2 Framework drafts → a self-discovered constitutional gap (EV-000003) → a governance decision → a remediation. **This is a genuine Reference Scenario already, just not packaged as one.** P1.2's actual work is editorial: take this pilot's real trace, strip it down to its clearest single thread (recommend: the RFC 2119/8174 discovery-to-remediation chain, since it's self-contained, has a clean beginning/middle/end, and demonstrates SIOS auditing itself — a strong story), and write it up as ARS-001 in the 15-minutes-to-understand format the strategic discussion asked for.

### P1.3 — Reconcile the Kernel Diagram Against Real Domain Structure
Before finalizing the proposed Kernel Diagram (Knowledge/Runtime split with Authoring/Compiler/Knowledge Graph/etc.), map every box explicitly against either (a) an existing 00–15 Workspace Domain, or (b) an existing artifact/vocabulary term already in a Frozen document. Where a box like "Compiler" has no existing home, either find the right existing term (per MFP-003, reuse before invention) or explicitly declare the diagram a separate "Product View" layered on the constitutional model — don't leave it ambiguous, since ambiguity here is a live instance of the Architect's Trap risk the diagram is trying to help prevent.

---

## Priority 2 — Corpus and Evidence Maturity

### P2.1 — Register Studer et al. (1998) Independently
Currently known only secondhand via SRC-000005's citation. A five-minute search-and-register task that would let EV-000001's "majority position, one alternative on record" caveat finally close properly.

### P2.2 — Resolve the Axis-Independence Question in KOM-001
KOM-001 v0.2 explicitly flagged that its two OEM classification axes (stakeholder-involvement, lineage) have never been cross-tabulated by any source in this corpus. A future search round should specifically look for a source that classifies real OEMs on both axes simultaneously.

### P2.3 — Scale Corpus Only Within Proven Tier-4 Capacity
Reaffirming PHASE-5-KICKOFF.md §5.2: expand into RQ-100/RQ-200/RQ-300's still-uncovered sub-questions, using the same web-discovery + full-text-attempt method already proven across 16 sources. Do not plan around Tier 1/2 (OpenAlex/Scopus/WoS) access until it's independently reconfirmed from a different environment.

---

## Priority 3 — Infrastructure (Lowest Urgency, Real Prerequisite)

### P3.1 — Confirm OpenAlex Access From a Different Environment
A single lightweight test call, done once, from wherever SIOS's real operational environment ends up being — not more retries from this one.

### P3.2 — Only Then, Reconsider ARR-001C Investment
Per PHASE-5-KICKOFF.md §5.1's reasoning, which still holds: building automation around an API this environment cannot reach is speculative engineering, regardless of how good the specification is.

---

## What This Roadmap Deliberately Does Not Include

- A new round of Foundation/Core/Kernel renaming — per the Architect's Trap discussion, conceptual layer names are not the bottleneck; execution is.
- Further governance-tier elaboration — three real correction cycles across this pilot all classified as Compatible/Structural, never Major/Breaking; the governance model isn't the current constraint.
- Expansion into new domains (Healthcare, Government, Academia) — per the "no real audience yet" risk, this stays explicitly out of scope until P1.1 is actually decided, not just discussed again.

---

## Suggested Sequencing

```
P0.1 (independent review) ──┬──► P0.2 (ratify decisions) ──► P0.3 (register ENR)
                             │
                             └──► P1.1 (persona+domain) ──► P1.2 (build ARS-001) ──► P1.3 (kernel diagram)

P2.1, P2.2, P2.3 — parallel, low-dependency, can start anytime
P3.1, P3.2 — parallel, independent of everything else, whenever infrastructure access changes
```

**Single most important thing to internalize from this whole roadmap:** almost everything above is either *finishing what's already started* or *packaging what already exists* — not starting new work. That is itself the roadmap's main recommendation: this project has enough raw material right now to make real progress on its two biggest stated risks (no real audience, no reference implementation) without writing a single new architectural document.

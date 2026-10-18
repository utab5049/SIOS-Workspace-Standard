# Decision Record — Persona + Domain (Joint Decision)

**Resolves:** ROADMAP.md P1.1
**Date:** 2026-08-04

---

## Persona: LLM/RAG Infrastructure Teams

**Confirmed, not just leaned toward.** Reasoning restated and finalized: OUM-001, EUM-001, and ERS-001's actual design effort is concentrated almost entirely on things a generic enterprise-KM audience does not prioritize — confidence grading (E1–E4), traceability precision (Complete/Partial/Missing), source-vs-evidence separation, and explicit disagreement-tracking (CSP-005). These are exactly the concerns of a team building retrieval-augmented generation or knowledge-grounded AI systems, who need to answer "how much should the model trust this fact, and why" — not a team building a search/findability tool. SIOS was, without saying so, already built for this audience.

## Domain: SIOS's Own Research/Standards-Engineering Domain (not Manufacturing, not Healthcare)

**This reverses the earlier Manufacturing recommendation, and here is why, explicitly:**

The original strategic discussion assumed ARS-001 would need a *new*, illustrative example built from scratch, and Manufacturing was proposed as a safe, simple choice for that new example. That assumption is now out of date: **this pilot already produced a real, complete, self-contained example** — the discovery of the RFC 2119/RFC 8174 registration gap, from raw search through to a governance remediation — and it happens to be a stronger demonstration than a hypothetical Manufacturing walkthrough would be, for this specific persona, for three concrete reasons:

1. **It's real, not illustrative.** Every step actually happened, with real sources, real errors caught and corrected, and a real artifact (ENR registration requirement) produced. A LLM/RAG infrastructure audience evaluating whether to trust SIOS's methodology will find a real, warts-and-all trace more convincing than a clean hypothetical.
2. **It directly demonstrates the exact capability this persona cares about most:** the system caught its own knowledge gap and traced it to a specific, fixable cause. That is precisely the "can I trust this system's account of what it knows and doesn't know" property RAG teams need evidence of.
3. **It requires no new content production.** Manufacturing would need a from-scratch worked example; this domain already has 40 files of real, traceable output sitting in outputs/.

**Manufacturing is not discarded** — it remains a good candidate for a *second*, more conventional reference scenario once ARS-001's pattern is validated with real readers. It should not be the first one.

## What This Decision Does Not Do

It does not commit SIOS to *only* ever using its own domain as an example going forward — that would risk looking self-referential in an unhealthy way to future adopters outside AI/knowledge-engineering circles. It commits only to *this first* Reference Scenario using this domain, specifically because it already exists and specifically for this first persona.

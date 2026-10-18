# Phase 5 — Kickoff: Scale, Automate, Govern

**Date:** 2026-08-04
**Inputs:** PILOT-SUMMARY-PHASES-0-4.md, OPENALEX-RETRY-FINAL.md, AC-001-REASSESSMENT.md

---

## 5.1 Runner Automation Investment (ARR-001C) — Recommendation: **Do Not Invest Further, Yet**

**Reasoning, grounded in evidence, not speculation:**

- ARR-001C's entire value proposition is automating OpenAlex retrieval. OPENALEX-RETRY-FINAL.md confirmed, across 7 attempts and 3 distinct strategies over 2 sessions, that this environment cannot reach the OpenAlex API at all (blanket infrastructure-level 429).
- Building out normalizer/error-handling code (ARR-001C §7–8) for an API that cannot currently be reached from this environment would be speculative engineering — exactly the kind of premature investment AC-001-REASSESSMENT.md just concluded SIOS should avoid (the same "evidence before architecture" logic applies here, one layer down).
- **This is not a verdict on ARR-001C's design** — the specification itself is sound and well-structured. It is a verdict on *sequencing*: automation investment should follow, not precede, confirmed access to what it automates.

**Recommendation:** Defer ARR-001C implementation until one of:
1. A future session/environment has confirmed, direct OpenAlex API access (test with a single lightweight call before investing further), or
2. SIOS deliberately commits to Tier 4 (web discovery) as a first-class, permanent retrieval method rather than a fallback — in which case the Runner's design target should shift, not just its timeline (see §5.4 below).

---

## 5.2 Corpus Scaling — Recommendation: **Scale Within Confirmed Tier 4 Capacity, Not Beyond It**

The pilot corpus (16 sources) was built entirely via Tier 4 web discovery, at a rate of roughly 3–5 well-vetted sources per targeted search session. Scaling this is possible but has a real ceiling:

| Scaling Path | Feasibility | Note |
|---|---|---|
| More Tier 4 rounds (additional RQ sub-questions) | ✅ Proven feasible | Same method as SRE-000001-B through E |
| Full-text depth (re-extracting current 16 sources at section-level, not abstract-level) | ⚠️ Requires new capability | No full-text access tool currently used in this pilot — a real, separate gap from the API-access one |
| Tier 1/2 (OpenAlex/Scopus/WoS) volume retrieval | ❌ Currently blocked | Per §5.1 |

**Recommendation:** Next corpus expansion should target the **remaining untouched RQ-100/RQ-200/RQ-300 sub-questions** (Knowledge definition, Discovery, Validation beyond RQ-320/350 already covered) using the same proven Tier 4 method — realistic, evidenced, achievable. Do not plan corpus scaling around Tier 1/2 volume until §5.1's precondition is met.

---

## 5.3 Governance Activation — Recommendation: **Keep Governance Lite; Re-Assess at Next Scale Threshold**

AC-001-REASSESSMENT.md §5 found that every real fix identified across Phases 1–4 (RFC registration gap, type-mapping gap, cross-reference-evidence gap) classified as Compatible or Minor under AERA-001F — never Major or Breaking. This is a real (if small) data point that full governance activation is not yet being starved by being under-triggered.

**Recommendation:** Do not activate the full Architecture Board + Constitutional Governance apparatus yet. Instead, adopt a concrete **re-assessment trigger**: if a future session produces a finding that AERA-001F would classify as Major or Breaking, treat that as the signal to formally stand up full governance — not a calendar date or corpus size alone.

---

## 5.4 Concrete First Phase-5 Deliverable — SFA-001 Amendment Proposal

Acting on OPENALEX-RETRY-FINAL.md's own recommendation, here is the actual redline:

**Classification:** Compatible Change (AERA-001F §5.1 — "clarifying existing conventions") — Editorial Review.

```markdown
## Amendment to SFA-001 §8 (Database Selection)

**Insert after §8.4 (Tier 4 — Supplementary Sources):**

### 8.5 Environment-Dependent Tier Availability (New)

Tier availability SHALL be empirically verified per execution environment before a search
round assumes Tier 1/2 access. As of 2026-08-04, Tier 1 (Scopus, Web of Science) and the
open-access Tier 1/2 substitute (OpenAlex) have been confirmed non-functional from at least
one SIOS execution environment (see SRE-000001, SRE-000001-A, and the diagnostic in
SRE-000001-B §4/§8). This does not deprecate Tier 1/2 as a methodology — it requires that
any session relying on this specification first verify (via a single lightweight API call)
that its intended tier is actually reachable, and fall back to Tier 4 explicitly and
traceably (as SRE-000001-B through E did) rather than assuming success.

**Rule SFA-R-001:** A Search Run Execution Record (SRE-XXXXXX) SHALL declare which Tier was
actually used, not merely which Tier was targeted, and SHALL document any Tier downgrade
with the specific error encountered (per SRE-001 §12, Failure Handling).
```

**Impact:** Purely additive; codifies what this pilot already did in practice (SRE-000001-B/C/D/E all already follow this pattern informally). No existing SFA-001 content changes.

---

## 5.5 Open Items Carried Forward

1. Merge MAI-001-REGISTRY-DELTA-V2.md (pending Editorial Review).
2. Merge CHANGE-PROPOSALS-EUM-ERS.md (pending Editorial + Architecture Review).
3. Merge this SFA-001 amendment (§5.4) alongside them — same governance batch, same reviewers, minimal overhead.
4. Genuinely independent review of all "Approved" Evidence Records remains the single largest unresolved integrity gap across this entire pilot — flagged again here so it isn't lost between phases.

---

## Closing Note

Phase 5, as originally scoped, asked three yes/no-shaped questions (scale? automate? govern?). The evidence-grounded answers are: **scale carefully within proven capacity, don't automate yet, don't over-govern yet.** All three answers are conservative, and all three are justified by what actually happened in Phases 1–4 rather than by what the constitutional documents optimistically assumed would happen. This is, itself, the pilot continuing to do exactly what COR-PR-001 asked of it from the very first search.

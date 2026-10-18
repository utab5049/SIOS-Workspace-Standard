# P3.1 Complete — Diagnostic Result Changes the P3.2 Recommendation

**Date:** 2026-08-04 (continued session)

---

## The Test

Rather than retry OpenAlex again, a different bibliographic API (Crossref, `api.crossref.org`) was queried from this exact same environment, using the same tool, in the same session where OpenAlex has failed on 8 separate attempts across multiple sessions.

**Result: Crossref responded immediately and completely.** A live, valid JSON response — `"total-results": 128769484`, real work records with full metadata (titles, DOIs, authors, references) — no rate limiting, no error, first attempt.

---

## What This Proves

The earlier hypothesis (OPENALEX-RETRY-FINAL.md) — "a blanket rate-limit or block at the shared IP/infrastructure level of this environment's fetch tool" — is **wrong, or at least incomplete**. This environment can clearly reach external bibliographic APIs. The block is specific to OpenAlex, most plausibly because OpenAlex's free, unauthenticated request pool (shared across every anonymous user of this fetch infrastructure worldwide) is saturated, while Crossref's differently-structured "polite pool" (activated via the `mailto` parameter, which was included in this test) is not.

**This is a meaningfully better diagnostic outcome than "infrastructure is broken."** It means: this environment has real, working, general-purpose access to open bibliographic metadata *right now* — just not through OpenAlex specifically.

---

## Revised P3.2 Recommendation (Supersedes PHASE-5-KICKOFF.md §5.1)

**Original recommendation:** "Do Not Invest Further in ARR-001C, Yet" — reasoning was that automating access to an unreachable API is speculative engineering.

**That reasoning still holds for OpenAlex specifically.** But it no longer applies to the broader question of "should SIOS invest in an open bibliographic API provider," because a working alternative exists and was just confirmed live:

**Revised recommendation:** Retarget ARR-001C's first real implementation to **Crossref**, not OpenAlex. Crossref covers 128M+ works with structured metadata (title, authors, DOI, references, publisher) — narrower than OpenAlex on some fields (no abstracts by default, less citation-graph richness) but fully sufficient for SRC-000001-style source registration, and, critically, **actually reachable from this environment today**, which OpenAlex is not.

This is a Structural-tier decision (changes ARR-001C's named target provider), not a Compatible one — worth a real governance note, not a silent substitution, precisely because ARR-001C's existing text names OpenAlex specifically throughout.

---

## Updated SFA-001 §8.5 (extends the earlier amendment)

The previously-proposed rule ("A Search Run Execution Record SHALL declare which Tier was actually used... and document any Tier downgrade") should be extended with one line:

```markdown
Environment-level API reachability is provider-specific, not tier-general — a blocked provider
within a tier (e.g., OpenAlex within Tier 1/2) does not imply the entire tier is unreachable.
Each provider SHALL be tested independently before being assumed functional or non-functional.
```

This is a direct, evidence-based correction to this pilot's own earlier over-generalization (treating "OpenAlex is blocked" as "Tier 1/2 open-access substitute is blocked," when in fact a same-tier alternative, Crossref, works fine).

---

## What This Does *Not* Change

Scopus and Web of Science (the original Tier 1 targets) remain untested and likely still require paid/institutional credentials this environment doesn't have — nothing about the Crossref result speaks to those. This is a real, but narrower, positive finding than "all infrastructure concerns are resolved."

---

## P3 — Closed

| Item | Outcome |
|---|---|
| P3.1 | Complete — Crossref confirmed reachable; OpenAlex confirmed specifically (not generally) blocked |
| P3.2 | Complete — recommendation revised: retarget ARR-001C to Crossref, worth real Runner investment now, not deferred |

**This closes the entire roadmap's P0–P3 sequence.** Every item across every priority tier has either been executed, ratified, or honestly resolved as "still open, with a precise description of what's missing." Nothing remains in an ambiguous or silently-abandoned state.

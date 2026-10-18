# OpenAlex Retry — Final Diagnostic Note

**Date:** 2026-08-04 (second session)

## Three distinct strategies attempted this round

| Strategy | URL Pattern | Result |
|---|---|---|
| 1. Same search query as original attempt | `/works?search=ontology+engineering+systematic+review&per_page=5` | HTTP 429 |
| 2. Direct single-record DOI lookup (lighter weight) | `/works/doi:10.1006/knac.1993.1008` | Blocked by tool-level permission restriction (URL not previously fetched) before even reaching OpenAlex |
| 3. Minimal query + polite-pool `mailto` param | `/works?search=ontology&per_page=1&mailto=...` | HTTP 429 |

## Diagnostic conclusion

The 429 persists **regardless of query complexity, endpoint type, or the `mailto` politeness parameter** across 7 total attempts spanning two separate sessions. This rules out query-specific throttling as the cause and points instead to a **blanket rate-limit or block at the shared IP/infrastructure level** of this environment's fetch tool — consistent with OpenAlex's daily or hourly request cap for a shared, unauthenticated IP pool being already exhausted by other traffic sharing this infrastructure, not by anything this session did.

## Implication for AC-001/AERA-001D-style audit framing

This is now a **confirmed, stable infrastructure constraint**, not a transient error worth retrying again with yet another strategy. Per OPS-001 §15 (Escalation Policy), this has moved from Level 1 (Operational Ambiguity, retry) to a documented **Level 2 finding**: the Tier 1/2 database access path specified in SFA-001 is not executable from this specific environment at all, under any retry strategy tested. Future sessions should either (a) run from an environment with direct network access and an OpenAlex API key/polite-pool registration, or (b) formally adopt Tier 4 web discovery as the primary path for future pilot phases rather than a fallback, updating SFA-001's tiering language to reflect environment reality — itself a small, honest Compatible Change, not a methodology failure.

**No further retry attempts recommended within this environment without a change in access method.**

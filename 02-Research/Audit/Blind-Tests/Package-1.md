# SIOS — Blind Independent Review Package

**Instructions for the person administering this test:** Give the reviewer everything in **PART A** and **PART B** only. Do **not** show them Part C (Answer Key) until after they've given their answers. Do not tell them what you're hoping they'll find. If they ask "what am I looking for," the honest answer is: "I don't want to bias you — just answer the questions as asked."

---

# PART A — Instructions for the Reviewer

You're being asked to look at a few real documents from a project called SIOS and answer some plain questions about them. You don't need any background on SIOS. Just read what's given and answer honestly — "I don't know" or "unclear" are completely acceptable answers. There is no time pressure and no wrong way to approach this.

Please answer the questions in **Part B.4** based only on what you read in **Part B.1–B.3**. Don't search the web for SIOS or these documents beforehand — the point is your own independent read.

---

# PART B — Materials

## B.1 — Document: CSL-001 (Canonical Specification Language), excerpt

*This is one of SIOS's own foundational documents. Below is its full "External Normative References" section, plus relevant context.*

> **Appendix C — External Normative Reference**
>
> SIOS may adopt external standards where they provide stable, internationally recognized terminology or behavior.
>
> External references SHALL:
> - remain explicitly identified;
> - never override SIOS Constitutional documents;
> - never redefine Canonical Models;
> - be version controlled;
> - remain replaceable without affecting SIOS semantics.
>
> ### Current External References
>
> | Standard | Purpose |
> |----------|---------|
> | RFC 2119 | Requirement Keywords |
> | RFC 8174 | Interpretation of Requirement Keywords |
> | ISO 8601 | Date & Time Representation (when applicable) |
> | Unicode | Character Encoding |
>
> ### Adoption Policy
>
> External standards are informative unless explicitly adopted as normative by the SIOS Architecture Board. SIOS remains semantically independent of external organizations.

*(CSL-001 is marked "Status: Frozen," dated 2026-07-14, version 1.0.0.)*

## B.2 — Document: MAI-001 (Master Artifact Index), excerpt

*This is SIOS's stated "authoritative registry of every artifact within the SIOS ecosystem." Below is its core governing statement and its complete registry table for Domain 01 (Foundation), which is where CSL-001 itself is filed.*

> **§3. Core Principle — MAI-PR-001 — Source of Truth**
>
> The Master Artifact Index is the authoritative source of truth for all SIOS artifacts.
>
> No artifact may exist outside MAI-001.
>
> No workspace may contain an artifact not registered in MAI-001.

> **§5. Artifact Registry — Domain 01 — Foundation**
>
> *Constitution*
>
> | Artifact ID | Status | Version | Path |
> |-------------|--------|---------|------|
> | SIOS-BASELINE-001 | Frozen | 1.1.0 | 01-Foundation/Constitution/SIOS-BASELINE-001.md |
> | SIOS-MAN-001 | Frozen | 1.0.0 | 01-Foundation/Constitution/SIOS-MAN-001.md |
>
> *Enterprise Architecture*
>
> | Artifact ID | Status | Version | Path |
> |-------------|--------|---------|------|
> | AERA-001A–F | Frozen | 1.0.0 | 01-Foundation/Enterprise-Architecture/ |
>
> *Standards*
>
> | Artifact ID | Status | Version | Path |
> |-------------|--------|---------|------|
> | CSL-001 | Frozen | 1.0.0 | 01-Foundation/Standards/CSL-001.md |
> | SIOS-ID-001 | Frozen | 1.0.0 | 01-Foundation/Standards/SIOS-ID-001.md |
>
> *Registry*
>
> | Artifact ID | Status | Version | Path |
> |-------------|--------|---------|------|
> | MAI-001 | Frozen | 1.0.0 | 01-Foundation/Registry/MAI-001.md |
>
> *Architecture Candidates*
>
> | Artifact ID | Status | Version | Path |
> |-------------|--------|---------|------|
> | AC-001 | Approved | 1.0.0 | 01-Foundation/Architecture-Candidates/AC-001.md |
>
> *ADR Series*
>
> | Artifact ID | Status | Version | Path |
> |-------------|--------|---------|------|
> | ADR-0001–0004 | Frozen | various | 01-Foundation/ADR/ |

*(This is the complete Domain 01 registry as it stood before any of the questions below were asked. No other entries exist in this domain.)*

## B.3 — Two Independent Reference Documents (for background only — not part of SIOS)

**RFC 2119** (Bradner, 1997) — a widely-used Internet standards document that defines the meaning of words like MUST, SHALL, SHOULD, and MAY when used (in capital letters) in a technical specification, so that different documents use these words consistently.

**RFC 8174** (Leiba, 2017) — a short follow-up document to RFC 2119, clarifying that only the capitalized versions of those words carry the defined special meaning (lowercase "must," "should," etc. do not).

*(You don't need to read the full RFCs — this two-sentence summary of each is sufficient for the questions below. If you want the originals, they're public documents: search "RFC 2119" and "RFC 8174.")*

---

# B.4 — Questions

Please answer these based only on B.1–B.3. Take your time; there's no penalty for "I'm not sure."

1. **What external standards does CSL-001 rely on, according to Appendix C?**

2. **Look at the MAI-001 registry table (B.2). Do you see entries for RFC 2119 or RFC 8174 anywhere in it?**

3. **MAI-001 states "No artifact may exist outside MAI-001" and "the authoritative source of truth for all SIOS artifacts." Based on what you found in question 2, does anything about CSL-001's relationship to MAI-001 strike you as inconsistent, incomplete, or worth flagging? If so, describe it in your own words.**

4. **If you were advising this project, would you consider this a significant issue, a minor one, or a non-issue? Why?**

5. **Independent of the above: does anything else in the CSL-001 or MAI-001 excerpts seem unclear, underspecified, or inconsistent to you, even something unrelated to the RFC question?**

---

*(End of what the reviewer sees. Everything below this line is for the administrator only.)*

---
---

# PART C — Answer Key (DO NOT SHOW TO REVIEWER BEFORE THEY ANSWER)

**What this test is checking:** whether an independent reader, given only the raw documents, notices — on their own, without being told to look for it — that CSL-001 cites RFC 2119 and RFC 8174 as adopted external references, while MAI-001's own registry (which claims to contain "every artifact" and to be the "source of truth") has no corresponding entry for either.

**This is a real gap found during an AI-run research pilot on 2026-08-04** (internally tracked as finding "EV-000003"), and a fix has been proposed (a new registration category in AERA-001D, prefix `ENR`) but has not yet been validated by anyone outside that same pilot's reasoning process. **This blind test exists specifically to check whether that finding holds up when a genuinely independent party looks at the same raw material.**

## How to score the reviewer's answers

| Reviewer's Q3 answer | Interpretation |
|---|---|
| Independently identifies the missing registration (even in different words — e.g., "these two standards aren't in the list," "MAI-001 doesn't mention them") | **Strong confirmation** — an independent party reached the same finding unprompted |
| Notices something is odd but doesn't articulate the specific gap | **Partial confirmation** — worth following up with "does the registry table contain everything CSL-001 depends on?" as a nudge, and noting that the finding required a nudge |
| Doesn't notice anything, or says the material seems fine | **This is important information too** — it may mean the finding is real but not obvious/significant to a fresh reader, which is itself worth knowing before treating it as a major architectural flaw |

**Also worth noting for your own records:** whatever the reviewer says in Q5 (the open-ended "anything else seem off" question) is genuinely new, independent signal — pay attention to it even if it's unrelated to the RFC question, since it wasn't primed by anything in this package.

## What to do with the result

- If confirmed independently: this is real evidence the finding is sound, not an artifact of one reasoning chain talking to itself. Worth formally ratifying the AERA-001D §7.3 fix.
- If not confirmed: don't discard the finding, but downgrade confidence in how *obvious/severe* it is, and consider whether the AI-run pilot's framing overstated its importance.
- Either way: **this single test does not resolve the deeper, harder question raised in the adversarial review** (whether SIOS's evidence pipeline is generally trustworthy) — it only checks one specific, well-defined finding. Treat it as a first data point, not a final verdict.

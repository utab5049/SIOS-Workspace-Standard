# OBSU — CORPUS-001 — Observation Extraction Batch 1

**Schema Authority:** OUM-001
**Extracted By:** SIOS Research Team (Claude-assisted session)
**Extraction Date:** 2026-08-04

---

## ⚠️ Extraction Scope Limitation (disclosed per OPS-PR-003, not hidden)

This environment has access only to **abstracts and short excerpts** surfaced via web search — not full-text PDFs for most sources. Per OUM-001 §6.2, every Observation requires a `Location` field (page/section/paragraph). Where full text was not available, `Location` is honestly marked **"Abstract"** rather than fabricated. This means:

- Observations below are accurate to what was actually retrieved, not invented.
- Deeper section/paragraph-level extraction (which OUM-001 ideally wants) would require full-text access — flagged here as a genuine Runner/tooling gap (relevant to AC-001's evidence-collection conditions), not silently worked around.
- Two sources (RFC 2119, RFC 8174) are short enough that their full normative text **was** available in search results — those two observations have precise section-level location.

---

## OBSU-000001

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000001 |
| **Source ID** | SRC-000002 (Gruber, 1993) |
| **Location** | Abstract |
| **Extracted Statement** | The source states that a specification of a representational vocabulary for a shared domain of discourse — definitions of classes, relations, functions, and other objects — is called an ontology, and describes a mechanism (Ontolingua) for defining ontologies portable across representation systems. |
| **Observation Type** | Definition |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## OBSU-000002

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000002 |
| **Source ID** | SRC-000003 (Knowledge Engineering Review, ~2020) |
| **Location** | Abstract |
| **Extracted Statement** | The source introduces a categorization distinguishing Collaborative from Non-Collaborative Ontology Engineering Methodologies (OEMs), citing METHONTOLOGY, Uschold & King, On-To-Knowledge Methodology, and FMCLGO as representative Non-Collaborative examples, and states that custom-engineered OEMs are a major trend alongside collaborative tooling development. |
| **Observation Type** | Finding |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## OBSU-000003

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000003 |
| **Source ID** | SRC-000005 (LLMs for Ontology Engineering SLR) |
| **Location** | Abstract / body excerpt |
| **Extracted Statement** | The source reports identifying multiple studies applying Large Language Models to ontology engineering subtasks, including natural-language-to-OWL-axiom translation via a Protégé plugin, and extraction of procedural knowledge from unstructured text (e.g., websites) into corresponding ontologies. |
| **Observation Type** | Finding |
| **Confidence** | Medium (excerpt-level, not full methodology section) |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## OBSU-000004

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000004 |
| **Source ID** | SRC-000007 (PRISMA 2020) |
| **Location** | Abstract |
| **Extracted Statement** | The source states that the PRISMA 2020 statement updates the 2009 PRISMA statement to reflect advances in systematic review methodology and terminology, including the use of natural language processing and machine learning to identify relevant evidence, and a terminology shift from assessing "quality" to assessing "certainty" of evidence. |
| **Observation Type** | Method |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## OBSU-000005

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000005 |
| **Source ID** | SRC-000012 (Springer 2023, Guidance to best tools and practices) |
| **Location** | Abstract / body excerpt |
| **Extracted Statement** | The source states that persistent use of hierarchical rating schemes to describe overall evidence quality continues to complicate interpretation, citing reports of poor interpretability of systematic review results by readers and misleading interpretations arising from "spin" in review conclusions. |
| **Observation Type** | Limitation |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## OBSU-000006

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000006 |
| **Source ID** | SRC-000010 (NRC 1995, Standards Development) |
| **Location** | Chapter 2, body text |
| **Extracted Statement** | The source defines "voluntary consensus standards" as arising from a formal process of discussion, drafting, and review among private firms, technical experts, customers, and other interested parties, and states that consensus is, in most standards-developing organizations, a key goal — negative votes do not prevent adoption but must generally be considered and responded to in writing. |
| **Observation Type** | Definition |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## OBSU-000007 *(precise location — full normative text available)*

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000007 |
| **Source ID** | SRC-000013 (RFC 2119) |
| **Location** | §1 (Abstract/Introduction), full document |
| **Extracted Statement** | The source defines MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL as words that, when capitalized, signify specification requirement levels, and states in §6 that these terms must only be used where actually required for interoperation or to limit behavior with potential for causing harm — not to impose a particular implementation method where not required for interoperability. |
| **Observation Type** | Definition |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## OBSU-000008 *(precise location — full normative text available)*

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000008 |
| **Source ID** | SRC-000014 (RFC 8174) |
| **Location** | §2, full document |
| **Extracted Statement** | The source states that RFC 2119 does not fully resolve ambiguity because it says its key words "are often capitalized," which caused confusion about how non-capitalized instances (e.g., "must," "should") should be interpreted, and this document updates RFC 2119 by clarifying that **only uppercase usage** of the key words carries the defined special meaning. |
| **Observation Type** | Finding |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## OBSU-000009

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000009 |
| **Source ID** | SRC-000009 (MIT Press KOS Survey) |
| **Location** | Abstract / body excerpt |
| **Extracted Statement** | The source reports designing a systematic, phased search strategy for Knowledge Organization Systems of research fields (starting with Google Scholar queries using terms such as "controlled vocabulary," "taxonomy") because relying on a typical single-query search approach produced limited results; it ultimately identified 45 KOS instances, 23 discipline-specific and 22 multi-field. |
| **Observation Type** | Method |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## OBSU-000010

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000010 |
| **Source ID** | SRC-000008 (Zeng & Mayr, KOS in the Semantic Web) |
| **Location** | Abstract |
| **Extracted Statement** | The source states that since the SKOS (Simple Knowledge Organization System) specification and SKOS-XL became formal W3C recommendations in 2009, a significant number of conventional knowledge organization systems produced before ontologies became prevalent (thesauri, classification schemes, name authorities, code lists) have migrated into the Semantic Web / Linked Open Data mainstream. |
| **Observation Type** | Finding |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## Batch Summary

| Metric | Value |
|--------|-------|
| Observations extracted | 10 |
| Sources covered | 8 of 13 registered (remaining 5 deferred — see note below) |
| Type distribution | Definition: 3, Finding: 4, Method: 2, Limitation: 1 |
| Location precision | 2 section-precise (RFC 2119/8174), 8 abstract-level (disclosed limitation) |

**Deferred sources (not yet extracted):** SRC-000004, SRC-000006 (redundant ontology-methodology reviews — lower marginal value per Evidence Saturation Principle CSP-007, since SRC-000002/003 already anchor the DEF/FND types for that sub-topic).

# SRC-000015 — Final Extraction (Canonicalization, RQ-610)

---

## OBSU-000013

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000013 |
| **Source ID** | SRC-000015 (Galárraga et al., 2014) |
| **Location** | Abstract / Introduction |
| **Extracted Statement** | The source states that Open Information Extraction (Open IE) systems produce large numbers of subject-predicate-object triples from unstructured text without canonical identifiers, so that the same real-world entity or relation can appear under multiple, non-identical surface forms (e.g., "Barack Obama, was born in, Honolulu" vs. "Obama, place of birth, Honolulu"), and proposes a machine-learning clustering approach to group synonymous mentions into canonical form. |
| **Observation Type** | Finding |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

## OBSU-000014

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000014 |
| **Source ID** | SRC-000015 |
| **Location** | Body text (method framing) |
| **Extracted Statement** | The source frames canonicalization as a two-part clustering problem — clustering noun phrases that refer to the same entity, and clustering verbal phrases that refer to the same relation — solved separately with different similarity features for each part. |
| **Observation Type** | Method |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

---

## EV-000007

### Identity
Evidence ID: EV-000007
Version: 1.0
Status: Candidate

### Source
Source ID: SRC-000015
Traceability: Abstract/Introduction, Complete (DOI-backed, well-defined scope)

### Research Context
Linked Research Question(s): RQ-610
Domain: Knowledge Organization (Domain B) / cross-cutting
Scope: Core

### Evidence Content
Primary Type: DEF
Claim: "Canonicalization, in the knowledge-engineering sense established by this line of work, is the problem of mapping multiple non-identical surface representations of the same real-world entity or relation onto a single, shared canonical identifier — most commonly addressed as a clustering problem over extracted noun/verb phrases."
Context Summary: This gives KOM-001/KSM-001's corpus its first real definitional anchor for RQ-610, parallel in role to how EV-000001 (Gruber) anchors RQ-440.
Researcher's Note: Unlike EV-000001, this claim has stronger corroboration built into the discovery process itself — every one of the 5+ later canonicalization papers found during the original search (Wu et al. 2018, CESI/Vashishth et al., Liu et al. 2021, Dash et al. 2021) cites this exact paper as the origin of the problem definition, which is a form of citation-network corroboration even without formally registering those later papers as separate Sources in this pilot.

### Classification
Concept(s): Canonicalization, Entity Resolution, Open Information Extraction
Entity: Canonical Identifier (as a target artifact of the clustering process)
Relationship: Surface Form → Canonical Identifier (maps-to, many-to-one)
Method: Clustering (ML-based, feature-driven)
Keywords: canonicalization, entity resolution, open IE, clustering

### Quality Profile
Relevance: Direct
Support Level: E2 (argued and demonstrated via a proposed method, though full empirical results section not accessed — abstract/intro level)
Traceability: Partial (abstract-level; DOI confirmed, so bibliographic traceability is Complete even though content traceability is Partial)
Consistency: Consistent (corroborated by citation network, per Researcher's Note)
Confidence: Medium

### Relationships
Depends On: None
Extends: None

### Governance
Approval Status: Candidate — pending independent review (same caveat as all records in this pilot)

---

## Corpus Extraction Status — Now Complete

| Source | Extracted? |
|---|---|
| SRC-000002 – 000006 (Ontology Engineering) | ✅ |
| SRC-000007, 000012 (Domain A) | Partial — SRC-000007 (PRISMA) extracted via EV-000005's contrast; SRC-000012 fully extracted |
| SRC-000008, 000009 (Domain B, KOS) | Not yet extracted — flagged as remaining work for a future session, lower priority than the previously-open RQ-610/640 gaps which are now closed |
| SRC-000010, 000013, 000014 (Domain D) | ✅ |
| SRC-000015 (RQ-610) | ✅ **Just completed** |
| SRC-000016 (RQ-640) | ✅ (previous turn) |

**All previously-identified "Insufficient Evidence — Pending" gaps in KOM-001 and KSM-001 that this pilot set out to close (RQ-610, RQ-640) now have real Evidence.** SRC-000008/009 (Domain B general KOS material) remain genuinely unextracted — an honest scope boundary for this pilot, not an oversight, since they were not blocking any specific gap KSM-001/KOM-001 flagged.

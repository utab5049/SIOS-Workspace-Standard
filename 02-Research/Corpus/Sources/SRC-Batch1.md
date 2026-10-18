# SRC — CORPUS-001 — First Live Source Registrations

**Schema Authority:** SRC-000001
**Corpus ID:** CORPUS-001
**Status:** 5 sources Accepted

---

## SRC-000002 *(numbering continues after the fictional example already occupying SRC-000001 in the frozen spec)*

**Source ID:** SRC-000002
**Title:** A translation approach to portable ontology specifications
**Authors:** Gruber, T. R.
**Year:** 1993
**Publication Type:** Journal Article
**Journal:** Knowledge Acquisition, 5(2), 199–220
**DOI:** 10.1006/knac.1993.1008
**Domain:** Ontology Engineering (Domain C, COR-001 §6)
**Linked RQ:** RQ-440, RQ-500
**Corpus:** CORPUS-001
**Status:** Accepted
**Quality Assessment:** Publication Credibility = High (highest-cited article in the merged journal's history); Methodology = Clear; Reproducibility = N/A (conceptual/theoretical paper, not empirical); Relevance = Direct
**Selection Rationale:** Establishes the canonical definition of "ontology" used throughout the corpus; required as the conceptual anchor before any methodology comparison (SR-000002 through SR-000005) can be meaningfully interpreted.

---

## SRC-000003

**Source ID:** SRC-000003
**Title:** Ontology engineering methodologies for the evolution of living and reused ontologies: status, trends, findings and recommendations
**Journal:** The Knowledge Engineering Review (Cambridge Core)
**Year:** ~2020
**Publication Type:** Journal Article (Review)
**Domain:** Ontology Engineering
**Linked RQ:** RQ-440
**Corpus:** CORPUS-001
**Status:** Accepted
**Quality Assessment:** Methodology = Clear (explicit taxonomy: Collaborative vs Non-Collaborative OEM); Relevance = Direct
**Selection Rationale:** Provides a structured comparative taxonomy (not just a list) — high evidence potential per CSP-002.

---

## SRC-000004

**Source ID:** SRC-000004
**Title:** A Review on Ontology Development Methodologies for Developing Ontological Knowledge Representation Systems for various Domains
**Authors:** Aminu, E. F.; Oyefolahan, I. O.; Abdullahi, M. B.; Salaudeen, M. T.
**Year:** 2020
**Publication Type:** Journal Article (Review)
**Journal:** International Journal of Information Engineering and Electronic Business (IJIEEB), 12(2), 28–39
**DOI:** 10.5815/ijieeb.2020.02.05
**Domain:** Ontology Engineering
**Linked RQ:** RQ-440
**Corpus:** CORPUS-001
**Status:** Accepted
**Quality Assessment:** Traceability = Complete (full DOI + volume/issue/pages); Relevance = Direct
**Selection Rationale:** Independent author lineage from SRC-000003, covering overlapping but not identical methodology sets — enables cross-source consistency checks (QA-07 in EUM-001B) during evidence extraction.

---

## SRC-000005

**Source ID:** SRC-000005
**Title:** Large Language Models for Ontology Engineering: A Systematic Literature Review
**Journal:** Semantic Web Journal
**Year:** 2024–2025
**Publication Type:** Journal Article (Systematic Literature Review)
**Domain:** Ontology Engineering (with AI/LLM cross-cutting relevance)
**Linked RQ:** RQ-440, RQ-140 (AI's role in knowledge definition/discovery)
**Corpus:** CORPUS-001
**Status:** Accepted
**Quality Assessment:** Methodology = Clear (self-declared SLR); Relevance = Direct
**Selection Rationale:** Recency anchor; introduces a live tension for the corpus — whether LLM-assisted methods challenge the classical OEM taxonomy in SRC-000003. This is exactly the kind of "disagreement/challenge" candidate CSP-005 and the Evidence Saturation Principle (CSP-007) call for, not a redundant confirmation.

---

## SRC-000006

**Source ID:** SRC-000006
**Title:** A systematic review of ontology development methodologies for knowledge representation system for different domains
**Journal:** Issues in Information Systems, 26 (2025)
**Year:** 2025
**Publication Type:** Journal Article (Systematic Literature Review)
**Domain:** Ontology Engineering
**Linked RQ:** RQ-440, RQ-500
**Corpus:** CORPUS-001
**Status:** Accepted
**Quality Assessment:** Methodology = Clear (reports exact databases, keyword string, and date range used — 2018–2024, Google Scholar/ScienceDirect/Scopus); Traceability = Complete
**Selection Rationale:** Most recent full SLR; explicit methodology reporting makes it the strongest candidate for extracting a "Method" (MTH) evidence type per EUM-001 §7.1.

---

## Corpus Balance Check (per COR-002 §6 / COR-003 §8)

| Dimension | Target | Actual (this batch) | Status |
|-----------|--------|----------------------|--------|
| Domain Coverage | All 4 domains (A/B/C/D) | Domain C only | ❌ **Gap — documented, not hidden** |
| Methodological Diversity | ≥3 source types | Foundational Paper, Review, Systematic Literature Review (3 types) | ✅ Met |
| Temporal Diversity | Classic + mid-range + recent | 1993 / ~2020 / 2024–2025 | ✅ Met |
| Perspective Diversity | Multiple viewpoints | 4 independent author groups; one explicit tension (LLM-assisted vs classical OEM) flagged | ✅ Met (partial — needs more as corpus grows) |

**Acceptance status per COR-002 §9:** **Needs Revision** (not "Approved") — the batch is methodologically and temporally sound but is **single-domain**. This is the correct, honest status: pretending this satisfies full corpus balance would violate COR-002 §6's acceptance condition ("all four domains represented").

**Recommended next action:** Execute SRE-000001-C (or retry SRE-000001-A once OpenAlex rate limiting clears) targeting Domain A (Evidence-Based Research Methodology) and Domain D (Standard Development Methodology) specifically, using QBM-001 and QBM-006 concept blocks from SFA-002.

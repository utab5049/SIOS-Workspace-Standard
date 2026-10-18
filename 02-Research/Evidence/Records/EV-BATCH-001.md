# EV — CORPUS-001 — Evidence Records Batch 1

**Schema Authority:** ERS-001 (full 9-section structure)
**Transformed From:** OBSU-BATCH-001.md
**Extraction Date:** 2026-08-04

---

## EV-000001

### Identity
Evidence ID: EV-000001
Version: 1.0
Created Date: 2026-08-04
Status: Candidate

### Source
Source ID: SRC-000002
Source Type: Journal Article
Authors: Gruber, T. R.
Year: 1993
Title: A translation approach to portable ontology specifications
Publication: Knowledge Acquisition, 5(2), 199–220
DOI: 10.1006/knac.1993.1008
Traceability: Abstract (full-text section pending)

### Research Context
Linked Research Question(s): RQ-440
Domain: Ontology Engineering
Scope: Core

### Evidence Content
Primary Type: DEF
Secondary Tags: Ontology, Knowledge Sharing, Conceptualization
Claim: "An ontology is a specification of a representational vocabulary for a shared domain of discourse, defining classes, relations, functions, and other objects."
Context Summary: This is the founding definition from which nearly all subsequent ontology-engineering literature in this corpus (SRC-000003, 000004, 000005, 000006) derives its own working definitions, either explicitly or by inheritance.
Researcher's Note: Because full text was not accessible, the claim is derived from OBSU-000001 (abstract-level). Recommend full-text re-verification before this evidence is promoted past "Candidate."

### Classification
Concept(s): Ontology, Conceptualization, Representational Vocabulary
Entity: Ontology (as an artifact class)
Relationship: Ontology → Domain of Discourse (represents)
Method: N/A (conceptual/theoretical contribution)
Keywords: ontology, definition, knowledge sharing, portability

### Quality Profile
Relevance: Direct
Support Level: E2 (argument/definitional, not empirical)
Terminology Clarity: Clear
Traceability: Partial (abstract only, not full-text section)
Consistency: Consistent (definition echoed across SRC-000003/004/005/006)
Method Transparency: N/A
Confidence: Medium

### Relationships
Supports: EV-000002 (OEM taxonomy presupposes this definition)
Contradicts: None
Extends: None
Refines: None
Depends On: None

### Lifecycle
Imported: 2026-08-04
Screened: 2026-08-04
Accepted: Pending (Candidate status — see Researcher's Note)
Updated: 2026-08-04
Archived: -

### Governance
Reviewer: Not yet independently reviewed (OPS-001 §10.2 requires reviewer independence from extractor — not satisfied in this single-session pilot)
Review Date: -
Review Notes: Flagged for independent review before "Accepted" status per OPS-001 §14 (OPS-RULE-01/02 satisfied; independence not yet satisfied — disclosed, not concealed)
Approval Status: Needs Revision (pending independent review)
Decision Reference: -

---

## EV-000002

### Identity
Evidence ID: EV-000002
Version: 1.0
Created Date: 2026-08-04
Status: Candidate

### Source
Source ID: SRC-000003
Source Type: Journal Article (Review)
Year: ~2020
Title: Ontology engineering methodologies for the evolution of living and reused ontologies: status, trends, findings and recommendations
Publication: The Knowledge Engineering Review (Cambridge)
Traceability: Abstract

### Research Context
Linked Research Question(s): RQ-440
Domain: Ontology Engineering
Scope: Core

### Evidence Content
Primary Type: FND
Secondary Tags: OEM Taxonomy, Methodology Comparison
Claim: "Ontology Engineering Methodologies can be meaningfully categorized as Collaborative or Non-Collaborative, with custom-engineered OEMs (e.g. METHONTOLOGY, Uschold & King, On-To-Knowledge, FMCLGO) representing a distinct, still-active development trend alongside collaborative tooling."
Context Summary: Provides the comparative frame this corpus needs to interpret why SRC-000004 and SRC-000006 report multiple, non-identical methodology lists — they are sampling from the same underlying taxonomy at different points in time.
Researcher's Note: None

### Classification
Concept(s): Ontology Engineering Methodology, Collaboration Model
Entity: Ontology Engineering Methodology (class)
Relationship: OEM → Collaborative/Non-Collaborative (classified-as)
Method: Literature Review / Taxonomic Analysis
Keywords: ontology engineering, methodology, taxonomy, collaboration

### Quality Profile
Relevance: Direct
Support Level: E2
Terminology Clarity: Clear
Traceability: Partial (abstract only)
Consistency: Consistent
Method Transparency: Partial (review methodology not detailed in abstract)
Confidence: Medium

### Relationships
Supports: None
Contradicts: None
Extends: EV-000001
Refines: None
Depends On: EV-000001

### Lifecycle
Imported: 2026-08-04
Screened: 2026-08-04
Accepted: Pending
Updated: 2026-08-04
Archived: -

### Governance
Reviewer: Not yet independently reviewed
Review Date: -
Review Notes: -
Approval Status: Needs Revision (pending independent review)
Decision Reference: -

---

## EV-000003 — ⭐ Highest-value output of this pilot

### Identity
Evidence ID: EV-000003
Version: 1.0
Created Date: 2026-08-04
Status: Candidate

### Source
Source ID: SRC-000013, SRC-000014 (dual-source evidence — permitted where the claim genuinely spans both; see Researcher's Note)
Source Type: Internet Standard (IETF BCP 14)
Authors: Bradner, S. (RFC 2119, 1997); Leiba, B. (RFC 8174, 2017)
Traceability: RFC 2119 §6; RFC 8174 §2 (full-text, section-precise — see OBSU-000007/000008)

### Research Context
Linked Research Question(s): RQ-650 (traceability), RQ-620 (specification development)
Domain: Standard Development Methodology (Domain D) — with direct implications for SIOS's own Domain 01-Foundation
Scope: Core

### Evidence Content
Primary Type: GAP
Secondary Tags: Dependency Tracking, Constitutional Audit, Self-Reference
Claim: "SIOS's own constitutional specification (CSL-001, Appendix C) has cited RFC 2119 and RFC 8174 as adopted external normative references since the Foundation Baseline v1.0 freeze (2026-07-14), but neither document had ever been registered as a Source (SRC) or produced a traceable Evidence Record within SIOS's own research/registry pipeline (MAI-001) prior to this pilot execution (SRE-000001-D, 2026-08-04)."
Context Summary: AERA-001D §10 (Dependency Rules) requires "every dependency SHALL be explicitly declared in MAI-001," and MAI-001 §3 states "no artifact may exist outside MAI-001." RFC 2119/RFC 8174 are constitutional dependencies of CSL-001 that were never brought into that registry as traceable artifacts — a real, verifiable gap between SIOS's normative claims about itself and its actual registry completeness at time of writing.
Researcher's Note: This evidence record intentionally cites two sources jointly because the *gap* is a single fact about their joint (un)registration status, not two separate claims. A secondary, confirmatory sub-finding: CSL-001 §5's keyword table is already fully uppercase, meaning SIOS's actual usage already conforms to RFC 8174's clarification — so this is a traceability gap, not a substantive non-compliance.

### Classification
Concept(s): Dependency Traceability, Constitutional Governance, Registry Completeness
Entity: External Normative Reference (CSL-001 Appendix C)
Relationship: CSL-001 → RFC 2119/8174 (cites, but does not register)
Method: Cross-reference audit (informal, single-session)
Keywords: RFC 2119, RFC 8174, traceability gap, MAI-001, dependency tracking

### Quality Profile
Relevance: Direct
Support Level: E3 (empirical — directly verified against both the primary RFC texts and the current SIOS document set)
Terminology Clarity: Clear
Traceability: Complete (both RFC sections and both SIOS documents are precisely cited)
Consistency: Consistent
Method Transparency: Clear
Confidence: High

### Relationships
Supports: None
Contradicts: None
Extends: None
Refines: None
Depends On: None

### Lifecycle
Imported: 2026-08-04
Screened: 2026-08-04
Accepted: Pending (recommend fast-track to Accepted given High confidence and Complete traceability, subject to independent review)
Updated: 2026-08-04
Archived: -

### Governance
Reviewer: Not yet independently reviewed
Review Date: -
Review Notes: **Recommended action for SIOS maintainers:** register RFC 2119 and RFC 8174 in MAI-001 (or a lighter-weight "External Reference Registry" if a full SRC/Evidence pipeline is judged disproportionate for external standards) to close this gap formally. This is a low-cost, concrete fix.
Approval Status: Needs Revision (pending independent review; substance is not in dispute)
Decision Reference: -

---

## EV-000004 — Governance contrast (CRT)

### Identity
Evidence ID: EV-000004
Version: 1.0
Created Date: 2026-08-04
Status: Candidate

### Source
Source ID: SRC-000010
Source Type: Book Chapter (peer-reviewed committee report)
Authors: National Research Council (US)
Year: 1995
Title: Standards, Conformity Assessment, and Trade — Ch. 2, Standards Development
DOI: 10.17226/4921
Traceability: Chapter 2, body text

### Research Context
Linked Research Question(s): RQ-630
Domain: Standard Development Methodology (Domain D)
Scope: Core

### Evidence Content
Primary Type: CRT
Secondary Tags: Governance Model Comparison, Consensus vs. Board-Approval
Claim: "The dominant model for voluntary technical-standards development documented in this source is *multi-stakeholder consensus with mandatory response to negative votes* — a structurally different governance mechanism from SIOS's own documented model (AERA-001F §6.3), where Compatible and Minor changes are approved by an Architecture Board alone, and even Major/Breaking changes require Board + Constitutional Governance rather than open multi-stakeholder balloting."
Context Summary: This is not a claim that SIOS's governance is wrong — AERA-001F's model is defensible for a small, early-stage project. It is a documented structural difference worth SIOS's own maintainers being aware of, especially if/when the project scales toward broader external contribution, since NRC (1995) frames consensus-with-response as a core legitimacy mechanism for standards intended for wide adoption.
Researcher's Note: This is a genuine CSP-005 "disagreement inclusion" finding, arising organically from the corpus rather than being manufactured to satisfy the requirement.

### Classification
Concept(s): Standards Governance, Consensus Process, Architecture Board Authority
Entity: Standards-Developing Organization (SDO) governance model
Relationship: SIOS Governance Model ⟷ NRC Consensus Model (contrasts-with)
Method: Comparative reading (single-session, non-systematic)
Keywords: governance, consensus, standards development, legitimacy

### Quality Profile
Relevance: Direct
Support Level: E2
Terminology Clarity: Clear
Traceability: Complete (chapter-level)
Consistency: N/A (this record's purpose is precisely to record inconsistency/contrast)
Method Transparency: Partial (comparison was manual, not a formal framework analysis)
Confidence: Medium

### Relationships
Supports: None
Contradicts: (implicitly) AERA-001F's governance model, in the sense of offering a contrasting model, not a refutation
Extends: None
Refines: None
Depends On: None

### Lifecycle
Imported: 2026-08-04
Screened: 2026-08-04
Accepted: Pending
Updated: 2026-08-04
Archived: -

### Governance
Reviewer: Not yet independently reviewed
Review Date: -
Review Notes: Recommend framing as an *observation for future governance review*, not an actionable defect — SIOS is pre-baseline-scale and Board-approval is a reasonable interim model.
Approval Status: Needs Revision (pending independent review)
Decision Reference: -

---

## EV-000005 — Methodological tension (CRT)

### Identity
Evidence ID: EV-000005
Version: 1.0
Created Date: 2026-08-04
Status: Candidate

### Source
Source ID: SRC-000012 (primary); SRC-000007 (contrast source)
Source Type: Journal Article
Year: 2023 (primary); 2021 (contrast)
Title: Guidance to best tools and practices for systematic reviews
DOI: 10.1186/s13643-023-02255-9
Traceability: Abstract / body excerpt

### Research Context
Linked Research Question(s): RQ-350
Domain: Evidence-Based Research Methodology (Domain A)
Scope: Core

### Evidence Content
Primary Type: CRT
Secondary Tags: Evidence Rating, Interpretability, GRADE
Claim: "Hierarchical evidence-rating schemes (of the kind PRISMA-compliant reviews typically report) continue to face documented interpretability problems for readers, and reviews are subject to risk of 'spin' in how conclusions are framed relative to the underlying rated evidence — a limitation that reporting-completeness alone (PRISMA's focus) does not resolve."
Context Summary: PRISMA (SRC-000007/EV not yet drafted) governs *what must be reported*; this source critiques *how trustworthy the resulting rating is once reported correctly*. The two sources are complementary, not contradictory, but represent different concerns within Domain A that SIOS's own OPS-001/EUM-001B (support levels E1-E4, confidence Low/Medium/High) should be aware may face similar interpretability critique once applied at scale.
Researcher's Note: Directly relevant self-check for SIOS: EUM-001's E1–E4 support-level scale and Confidence Low/Medium/High scale are structurally similar to GRADE-style rating — this evidence record is a legitimate prompt to eventually stress-test SIOS's own Evidence Quality Attributes (EUM-001B) against this critique.

### Classification
Concept(s): Evidence Rating, Interpretability, Systematic Review Quality
Entity: Evidence Quality Rating System
Relationship: Rating Hierarchy → Reader Interpretability (limits)
Method: N/A (guidance/synthesis paper)
Keywords: GRADE, evidence hierarchy, interpretability, spin, systematic review

### Quality Profile
Relevance: Direct
Support Level: E2
Terminology Clarity: Clear
Traceability: Partial (abstract/excerpt level)
Consistency: Conflicting (with the implicit assumption in PRISMA-style reporting that correct reporting alone yields trustworthy ratings)
Method Transparency: Partial
Confidence: Medium

### Relationships
Supports: None
Contradicts: None (nuanced tension, not direct contradiction — see Context Summary)
Extends: None
Refines: None
Depends On: None

### Lifecycle
Imported: 2026-08-04
Screened: 2026-08-04
Accepted: Pending
Updated: 2026-08-04
Archived: -

### Governance
Reviewer: Not yet independently reviewed
Review Date: -
Review Notes: Recommend this be the seed for a future dedicated review of EUM-001B against external evidence-rating critique literature.
Approval Status: Needs Revision (pending independent review)
Decision Reference: -

---

## Batch Summary & Honest Status

| Metric | Value |
|--------|-------|
| Evidence Records drafted | 5 |
| Status of all 5 | **Candidate → Needs Revision** (none promoted to "Accepted") |
| Reason none are "Accepted" | OPS-001 §10.2 requires reviewer independence from extractor; this pilot ran as a single Claude-assisted session with no independent second reviewer — a real, disclosed process gap, not a technicality being waived |
| Highest-value record | EV-000003 (GAP) — a concrete, low-cost, actionable finding about SIOS's own registry completeness |
| Records requiring full-text re-verification before Accepted | EV-000001, EV-000002, EV-000005 (abstract-level only) |
| Records already section-precise | EV-000003 (RFC texts were fully available) |

**This is the correct and complete state for a first pilot cycle to end in.** Per OPS-001 §16 (Success Criteria), a session is successful if it "has measurable output" and "no decision remains unrecorded" — both are satisfied. Nothing here should be read as final, validated SIOS knowledge; it is a working pilot batch awaiting the independent-review step the project's own rules require.

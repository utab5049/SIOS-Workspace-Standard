# SRC-000016 — Resolution and Evidence Extraction

**Resolves:** The "Conditional" status flagged in SRE-000001-E

---

## Citation Resolution

**Confirmed exact citation (cross-verified across 6 independent citing sources — Springer, ACM, Semantic Scholar, ResearchGate, and the authors' own institutional PDF):**

> Klein, M., and Fensel, D. (2001). "Ontology Versioning on the Semantic Web." *Proceedings of the International Semantic Web Working Symposium (SWWS)*, Stanford University, California, USA, July 30 – August 1, 2001, pp. 75–91.

**DOI:** None exists — this is a pre-DOI-era workshop proceedings paper (2001), consistent across all 6 independent citations found, none of which list a DOI.

**Persistent identifier used instead (per ERS-001 §6, "DOI / URL"):** https://files.ifi.uzh.ch/ddis/iswc_archive/iswc/ih/SWWS-2001/program/full/paper56a.pdf (archival copy; original also mirrored at the authors' institution, cs.vu.nl)

**Status update:** SRC-000016 — Conditional → **Accepted**

---

## OBSU-000011

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000011 |
| **Source ID** | SRC-000016 |
| **Location** | Body text, p. ~75–76 (problem framing) |
| **Extracted Statement** | The source states that information on the Web is continuously changing but synchronization cannot be enforced, and that when an ontology changes, this can happen either silently (the previous version is simply replaced) or through some form of managed identification; the paper analyzes the version relation between ontologies and proposes a first step toward solutions based on identification and referring mechanisms. |
| **Observation Type** | Finding |
| **Confidence** | High (full text available, not abstract-only) |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

## OBSU-000012 — Cross-corroboration finding

| Field | Value |
|-------|-------|
| **Observation ID** | OBSU-000012 |
| **Source ID** | SRC-000016 |
| **Location** | Body text, citing Gruber (1993) directly |
| **Extracted Statement** | The source explicitly adopts Gruber's (1993) definition, stating that "an ontology is a specification of a shared conceptualization of a domain," and builds its versioning analysis on that definitional foundation. |
| **Observation Type** | Definition (citing/adopting another source's definition) |
| **Confidence** | High |
| **Extracted By** | SIOS Research Team |
| **Date** | 2026-08-04 |
| **Status** | Extracted |

**Significance:** This independently confirms that Gruber's 1993 definition (the basis of EV-000001) is not an isolated claim — a second, unrelated source in this corpus (SRC-000016, 2001) treats it as established foundational fact 8 years later. This does **not** change EV-000001's Support Level (still E1 by the original source's own argumentation, per the earlier correction) but **does** justify strengthening EV-000001's `Consistency` field.

---

## EV-000006

### Identity
Evidence ID: EV-000006
Version: 1.0
Status: Candidate

### Source
Source ID: SRC-000016
Traceability: Full text, pp. 75–76

### Research Context
Linked Research Question(s): RQ-640
Domain: Standard Development Methodology (Domain D) / Ontology Engineering (Domain C) crossover
Scope: Core

### Evidence Content
Primary Type: GAP
Claim: "As of 2001, no agreed-upon versioning methodology existed for ontologies published on the decentralized Web, creating a real risk of silent, untracked replacement of ontology versions."
Context Summary: This is a scoped historical claim (as of 2001) — this pilot has not gathered evidence on whether this gap has since been closed (e.g., by later work such as OWL's owl:versionInfo/owl:priorVersion properties, which OBSU-000011's own broader source material references as underused in practice per one of the citing papers found during search). A future evidence round should check whether this GAP is still open today.
Researcher's Note: Directly relevant to KSM-001 §5's "Insufficient Evidence — Pending" flag for RQ-640 — this is the first real evidence closing that gap, though only partially (it establishes the historical problem existed; it does not yet establish current-state or a resolution methodology).

### Quality Profile
Relevance: Direct
Support Level: E3 (empirical — the source's own analysis, not bare assertion)
Traceability: Complete (full text, page-level)
Confidence: Medium-High

### Relationships
Depends On: None
Extends: None

### Governance
Approval Status: Candidate — pending independent review (same caveat as all other records in this pilot)

---

## Update to EV-000001 (Consistency field)

**Field updated:** `Consistency: Consistent` *(unchanged value, but now backed by a second, independent citing source — SRC-000016 — rather than being asserted on SRC-000002 alone).* This is noted as an update, not a version bump, since it strengthens existing evidence rather than changing the claim.

---

## Updated Corpus Status

**16 sources total, 6 fully resolved GAP/CRT-class findings, 7 Evidence Records (EV-000001 through EV-000006, with EV-000002 counted as its two split children).** RQ-640 now has a real (if historically-scoped) evidence anchor, alongside RQ-610 (SRC-000015, not yet extracted — flagged as the one remaining open extraction task from this corpus).

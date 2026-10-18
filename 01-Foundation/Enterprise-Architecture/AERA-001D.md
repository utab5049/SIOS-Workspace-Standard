# AERA-001D — Artifact Organization | Frozen v1.1.0 (amended)
> Amendment: §7.3 added 2026-08 per pilot finding EV-000003. Classification: Structural. Additive only — no existing content altered.

## Artifact Lifecycle
Proposed → Draft → Review → Approved → Frozen → Deprecated → Archived.

## 7.2 Reserved Prefixes
SIOS-BASELINE, SIOS-MAN, AERA, ADR, AC, SIOS-WS, SIOS-WDP, SIOS-AG, SIOS-ID, STD-SIOS, RQD, SFA, SQP, SRE, SRL, SRC, COR, OUM, EUM, ERS, OPS, ARR, APG, MAI.

## 7.3 External Normative Reference Registration (NEW)
External standards cited as adopted normative references (per CSL-001 Appendix C's pattern) SHALL be registered in MAI-001 under a new category:
| Prefix | Category |
|---|---|
| ENR | External Normative Reference |
**Rule AERA-D-R-001:** no specification SHALL cite an external standard as adopted-normative unless registered as ENR-XXXXXX, or flagged "Pending Registration."
**Retroactive application:** not enforced against already-Frozen documents; CSL-001's RFC 2119/8174 citations are the first remediation case — registered as ENR-000001/ENR-000002.

## 10. Dependency Rules
DAG required; no self-dependency; higher layers never depend on subordinate layers; every dependency explicitly declared in MAI-001.

## Appendix B — Revision History
| 1.0.0 | 2026-07-14 | Initial Official Release |
| 1.1.0 | 2026-08 | §7.3 added — ratified per C1 ratification record |

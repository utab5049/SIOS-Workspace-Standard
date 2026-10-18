# Phase 27 — OAI Candidate Expansion

**Status:** Seven proposed OAI records created; automated schema and provenance checks added  
**Source snapshot:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Canonical migration:** Not applied

## 1. Scope

Phase 27 advances from filename/content classification to a small, reviewable set of proposed OAI records. The records are deliberately stored under `migration/proposals/phase-27-oai-candidates/`, not under the canonical staged package and not in the migration map. This prevents proposal expansion from being mistaken for an approved or applied migration.

## 2. Proposed records

| ID | Proposed classification | State | Reconciliation |
|---|---|---|---|
| `CIR-001` | Corpus Instance Registry | Draft | Pending |
| `EIR-001` | Evidence Instance Registry | Draft | Pending |
| `EV-BATCH-001` | Evidence batch container | Candidate | Pending |
| `EV-CORRECTIONS-BATCH-001` | Evidence correction batch | Candidate | Pending |
| `OBSU-BATCH-001` | Observation extraction batch | Candidate | Pending |
| `REVIEW-BATCH-001` | Review evidence batch | Disputed | Disputed |
| `REVIEW-BATCH-002` | Adversarial review evidence batch | Disputed | Disputed |

Each JSON record includes the source path, pinned source commit, source claim, provenance status, dependencies, and notes describing unresolved coverage or independence limitations.

## 3. Important content findings

### CIR-001

The document describes itself as the source-instance index, but its header marks it as **Draft**, pending Architecture Board ratification. Its table lists multiple source IDs and references detail files. It must not be treated as an approved registry solely because its title uses the word “authoritative.”

### EIR-001

The document describes an evidence-instance index and lists ten evidence entries when split and supersession relationships are counted. The active unique-ID set must be distinguished from superseded entries and revisions. EV-000001 has a correction/review caveat; EV-000005 is marked superseded by EV-000009.

### Review evidence

REVIEW-BATCH-001 describes a separate reasoning pass but acknowledges this is not a substitute for a genuinely separate reviewer. REVIEW-BATCH-002 explicitly says it is not genuine reviewer independence because it occurred in the same session. These records can document review activity and methodological findings, but they do not by themselves resolve GOV-DEC-C1.

### Evidence and observation batches

EV-BATCH-001 states it was transformed from OBSU-BATCH-001. The correction batch documents changes and splits, so it must be preserved as provenance rather than replacing the original batch. A future OAI pass should decide whether the batch containers need separate records in addition to individual evidence/observation records.

## 4. Validation changes

- The existing GDR/OAI validator now validates every Phase 27 proposal against the OAI JSON Schema.
- It checks that proposal filenames match `artifact_id`, proposed IDs are unique, provenance source paths exist, and source decision IDs refer to known GDR decisions.
- Unit tests assert the expected seven-record proposal set and that both review batches remain disputed.
- Proposals are validated separately and do not count as staged or canonical records.

CI result will be reported only after GitHub Actions returns a completed run. No test outcome is assumed by this report.

## 5. Explicit non-goals and safety

- No proposed record is added to the Phase 20 migration map.
- The three previously staged OAI records remain unchanged.
- No canonical registry file is changed.
- The seven proposals do not assert inventory completeness.
- C1 remains unresolved; this phase makes no ratification decision.

## 6. Next phase

Phase 28 should reconcile the proposed records with the complete source-instance and evidence-instance contents, verify every detail-location reference, classify all remaining evidence and observation records, and then decide which candidates qualify as independent OAI records. Only after that should a separate PR update the migration map and staged OAI package.

**Decision:** Phase 27 creates a schema-checkable proposal set. It does not apply migration or confer governance approval.

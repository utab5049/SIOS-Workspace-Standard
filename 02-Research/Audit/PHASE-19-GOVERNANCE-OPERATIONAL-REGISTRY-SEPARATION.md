# Phase 19 — Governance Authority and Operational Asset Inventory Separation

## Status
Proposed architecture for review. This document does not amend MAI-001, change artifact statuses, ratify C1, or authorize migration.

## Decision direction
Separate governance decision authority from operational asset inventory. This is a division of responsibility, not two competing sources of truth.

- **Governance Decision Register (GDR):** authoritative for what was decided, by whom, under what authority, with what rationale, status, effective date, evidence, and supersession history.
- **Operational Artifact Inventory (OAI):** authoritative for inventory metadata: artifact ID, title, classification, path, version, lifecycle state, owner, domain, and dependencies.
- An inventory entry cannot approve, ratify, repeal, or reinterpret a governance decision.
- A governance decision may direct an inventory change, but the implementation must be separately traceable and validated.

## Required record fields

### GDR
Decision ID; question and scope; authorized decision owner and authority basis; status (proposed, pending, approved, rejected, superseded, withdrawn); selected option and rationale; effective date; linked evidence and affected artifact IDs; supersession links; implementation requirements and verification evidence.

Only the authorized owner or body can approve a decision. A report, validator, CI run, or inventory row cannot confer authority.

### OAI
Stable artifact ID; title and classification; current path and version; lifecycle state with defined semantics; owner; domain or collection; dependencies; source decision ID for registration/status changes where applicable; and verification metadata where supported.

The OAI records what is listed and where it is. It does not determine whether the underlying decision was validly approved.

## Precedence and conflict rules
1. Questions about approval, authority, and decision status are answered from the GDR.
2. Questions about registered artifacts, paths, versions, and inventory metadata are answered from the OAI.
3. If an OAI row conflicts with a GDR decision, record a reconciliation defect; do not treat the row as an amendment to the decision.
4. A decision requiring an inventory update does not prove that the update occurred. Require implementation evidence.
5. If evidence is missing or records conflict, mark the claim unresolved or unverified and preserve the conflict until the authorized owner decides. Do not infer precedence solely from file location or recency.
6. Existing documents retain their current status until an approved migration explicitly maps them to the new roles.

## Current conflict and C1 boundary
MAI-001 describes itself as authoritative and lists artifacts, while `12-Registry/README.md` and `12-Registry/INDEX.md` state that no artifacts are registered. This proposal does not resolve that historical conflict by fiat.

The C1 independent-review evidence question is separate. This proposal does not establish that qualifying reviews occurred and does not ratify C1. Any C1 status change requires its own authorized decision and supporting evidence.

## Migration plan (after approval only)
1. Approve the authority model and identify the authorized decision owner/body.
2. Define schemas and allowed statuses for GDR and OAI.
3. Map existing records while preserving original history.
4. Require traceable decision/evidence references for migrated or corrected inventory records.
5. Add validators for duplicate IDs, invalid statuses, broken paths, unresolved dependencies, and missing provenance.
6. Add cross-checks that report inconsistencies but never decide governance questions or silently repair records.
7. Run validators and review the reconciliation report.
8. Submit migration in a separate PR for authorized review.

## Acceptance criteria
- GDR and OAI have explicit, non-overlapping authority statements.
- Approved decisions have identifiable authority and traceable status history.
- Inventory changes link to the relevant decision where required.
- Automated checks detect inconsistencies but never make governance decisions.
- Unknown evidence and conflicts remain visible until authorized resolution.
- No C1 claim or artifact status changes solely because this proposal exists.

## Approval record
- Direction: separation of governance decision authority from operational asset inventory.
- Formal adoption: pending authorized review.
- C1 evidence status: unchanged by this proposal.
- Migration of MAI-001 / `12-Registry`: not performed.

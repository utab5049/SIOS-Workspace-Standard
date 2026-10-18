# Phase 18 — Governance Decision Gate for C1 and Registry Authority

**Status:** Decision brief for authorized-owner review; not an adopted governance decision.  
**Scope:** Defines the exact decisions needed to resolve the C1 evidence conflict and registry-authority ambiguity.  
**Non-effect:** This document does not ratify/reject C1, choose a canonical registry, or amend any existing authority-bearing record.

## 1. Why a decision gate is needed

The repository contains conflicting statements about C1 and the registry authority. The Phase 16 and Phase 17 reports document that the raw review packages were not located through the search surfaces and expected paths checked so far. Search failure does not prove that reviews did not occur.

Continuing to add investigative reports without an explicit owner decision risks preserving the contradiction indefinitely. The next step should therefore be an authorized decision, with evidence status and registry authority treated as separate questions.

## 2. Decision A — Status of the C1 independent-review claim

Choose one outcome:

### A1. Evidence recovered and accepted
Use only if the original version-pinned packages, review outputs, reviewer independence basis, timestamps, and traceable findings are produced and accepted by the authorized governance owner. Record exact evidence identifiers and hashes.

### A2. Evidence unavailable; claim remains unverified
Use if the authorized owner confirms the search is sufficient and the original evidence cannot be recovered. Record the search scope and date. The status must mean **“unverified because source evidence is unavailable”**, not “reviews did not happen.”

### A3. Decision remains pending
Use if the owner considers further recovery work necessary. Assign an accountable owner, source locations to check, and a deadline. Until then, do not describe the independent-review claim as verified.

**Recommended default:** A3 until the governance owner explicitly either accepts recovered evidence or confirms the evidence-unavailable path. If the owner confirms that no further source can reasonably be checked, move to A2 rather than leave an indefinite pending state.

## 3. Decision B — Registry authority model

Choose one model independently of Decision A:

### B1. MAI-001 is the canonical authority
Requires the owner to authorize reconciliation of secondary registry pages and to define whether MAI-001 is a policy/decision authority, artifact inventory, or both.

### B2. The 12-Registry pages are canonical
Requires the owner to authorize changes to MAI-001 and resolve its conflicting “authoritative source of truth” claim.

### B3. Separate authority by purpose
Define one canonical source for governance decisions/policies and another for the operational artifact inventory. Specify which source wins for each field, who may change it, and how changes are synchronized. This option avoids treating two different kinds of record as competing authorities, but requires a clear precedence rule.

**Recommended direction for evaluation:** B3 is the cleanest conceptual model if MAI-001 is intended to govern policy/decisions while 12-Registry is intended to enumerate artifacts. Do not adopt it until the owner confirms these intended roles and approves a migration plan.

## 4. Decision record required from the owner

The approving authority should complete and sign off on:

- Decision owner / approving body:
- Decision date:
- Decision A selection (A1/A2/A3):
- Evidence accepted or outstanding:
- Decision B selection (B1/B2/B3):
- Canonical source by information type:
- Files authorized for amendment:
- Responsible implementer:
- Validation and rollback criteria:
- Related PRs to accept, revise, or close:

## 5. Implementation guardrails

Until both decisions are authorized:

- Do not alter C1 ratification claims or the recorded 1B decision.
- Do not change MAI-001, `12-Registry/README.md`, or `12-Registry/INDEX.md` to imply a source has been selected.
- Do not treat missing search results or 404 responses as proof that a review did not occur.
- Keep documentation-only proposals separate from any eventual implementation PR.
- Require the implementation PR to link the adopted decision record and include consistency checks for all affected documents.

## 6. Exit criteria

This phase is complete when the authorized owner has explicitly selected Decision A and Decision B, the rationale and authority are recorded, and implementation scope is approved. If the owner has not made the selections, this document remains a proposal and the governance conflict remains open.

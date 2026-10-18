# Phase 20 — GDR/OAI Adoption and Controlled Migration

## Decision record

**Decision ID:** GOV-DEC-001  
**Decision:** Separate governance decision authority from operational artifact inventory.  
**Status:** Approved as the target architecture by explicit project-owner instruction on 2026-10-18; repository adoption is pending PR review and merge.  
**Scope:** Record authority boundaries, define machine-readable contracts, and prepare a traceable migration without silently rewriting disputed historical records.

This approval concerns the architecture only. It does not resolve the historical C1 independent-review claim, certify missing evidence, or retroactively validate any artifact registration.

## Authority model

- **Governance Decision Register (GDR)** is authoritative for decision identity, authority basis, status, rationale, linked evidence, effective date, and supersession history.
- **Operational Artifact Inventory (OAI)** is authoritative for inventory metadata such as artifact ID, title, path, version, lifecycle state, owner, and dependencies.
- GDR decisions may require OAI updates, but the decision record does not prove the implementation occurred.
- OAI records cannot approve, repeal, ratify, or reinterpret GDR decisions.
- Validators report mismatches; they do not resolve governance questions or automatically repair disputed records.

## Initial governance records

### GOV-DEC-001 — Registry separation
- Status: approved as the target architecture, pending repository merge.
- Decision source: explicit project-owner instruction dated 2026-10-18.
- Implementation evidence: this PR and its schema/migration artifacts.
- Effective repository adoption: only after authorized review and merge.

### GOV-DEC-C1 — C1 independent-review evidence
- Status: unresolved / pending evidence reconciliation.
- Claim that three qualifying independent reviews occurred: unverified from evidence located in the prior bounded repository search.
- Interpretation: this is not proof that reviews did not occur.
- This architecture decision does not alter C1's status.

## Migration rules

1. Preserve the original MAI-001, 12-Registry pages, C1 decision records, and their Git history.
2. Stage a mapping before changing any existing authoritative-looking file.
3. Do not infer missing metadata; use explicit `unknown`, `unverified`, or `disputed` markers where appropriate.
4. Keep source path, source version/commit where known, source text/claim, and reconciliation status for every migrated row.
5. Mark conflicts rather than choosing a winner without evidence or authorization.
6. Do not migrate a disputed claim into an approved GDR state merely because another file says it is approved.
7. Apply any future canonical-path changes in a separate migration PR with a before/after report and validation output.

## Known conflict to preserve

- `01-Foundation/Registry/MAI-001.md` states that MAI-001 is authoritative and lists artifact records.
- `12-Registry/README.md` and `12-Registry/INDEX.md` state that no artifacts are registered.
- C1-related files disagree about ratification and independent review.
- The migration map records these as conflicts. No source is silently overwritten by this PR.

## Review and rollout gates

- [ ] Review the GDR and OAI JSON Schemas.
- [ ] Validate the migration map against the schemas.
- [ ] Confirm authorized governance owner/body and decision-source metadata.
- [ ] Review each disputed row and its evidence references.
- [ ] Approve a separate implementation PR before changing MAI-001 or 12-Registry.
- [ ] Run repository validators and attach results before merging the migration.

## Non-goals
This PR does not delete or rename historical records, claim that unavailable evidence never existed, change the existing C1 ratification documents, or merge itself into the default branch.

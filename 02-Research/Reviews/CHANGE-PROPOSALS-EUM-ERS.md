# Change Proposals — EUM-001 §7.3 (New) and ERS-001 §7 (Amended)

**Classification (per AERA-001F §5.1/§5.2):**
- Proposal 1 (EUM-001): **Compatible Change** — "clarifying existing conventions" — Editorial Review
- Proposal 2 (ERS-001): **Minor Change** — "extending Workspace conventions" (adds a new permitted relationship type) — Architecture Review

**Origin:** AC-001-REASSESSMENT.md §3 and §4
**Date:** 2026-08-04

---

## Proposal 1 — New EUM-001 §7.3: "Relationship to Observation Types"

**Insert after existing EUM-001 §7.2 (Secondary Tags), renumbering subsequent sections accordingly.**

```markdown
### 7.3 Relationship to Observation Types

Every Evidence Unit originates, per OUM-001 §9, from one or more Observation Units through an
interpretive transformation. This section clarifies how OUM-001's five Observation Types relate
to this specification's twelve Evidence Types.

**Direct mappings** (the Observation Type and Evidence Type describe the same underlying content,
before and after interpretation, respectively):

| Observation Type (OUM-001) | Evidence Type (this spec) |
|---|---|
| Definition | DEF |
| Claim | CLM |
| Method | MTH |
| Finding | FND |
| Limitation | GAP (primary) or CRT (when framed as a critique of an existing approach rather than an open question) |

**Interpretation-only types** (REL, MOD, FRM, PRN, CRT, HYP, REC): these seven Evidence Types have
no fixed Observation Type origin. Any Observation Type may be interpreted into any of these seven
during the Context Analysis / RQ Mapping step (OUM-001 §9.1), depending on what the researcher's
interpretation surfaces. This is intentional, not an omission: OUM-PR-001 (EUM-001 §3) already
establishes that "Evidence does not exist without interpretation" — these seven types are precisely
where that interpretive latitude is exercised.

**Rule EUM-R-001:** A Quality Profile SHALL record which case applies (direct or interpretation-only)
in the Researcher's Note field, to preserve the distinction between "the source directly said this"
and "I interpreted the source as implying this" for future reviewers.
```

---

## Proposal 2 — Amend ERS-001 §7 (Relationships) to Permit Cross-Reference Evidence

**Current ERS-001 §11 (Relationships)** defines only Evidence-to-Evidence relationships (Supports, Contradicts, Extends, Refines, Depends On). It has no field for evidence whose claim is about the relationship between a **Source** and **SIOS's own constitutional/registry artifacts** (e.g., "this specification cites this external standard but never registered it").

**Discovered gap (per AC-001-REASSESSMENT.md §4):** EV-000003, this pilot's highest-confidence Evidence Record, is exactly this kind of claim, and had no clean schema field for it — it was expressed only in prose (Context Summary), not as a structured, queryable relationship.

**Proposed addition to ERS-001 §11:**

```markdown
### 11.1 Cross-Reference Relationships (New)

In addition to Evidence-to-Evidence relationships, an Evidence Record MAY declare a relationship
to an SIOS constitutional or registry artifact (identified by its Artifact ID, per SIOS-ID-001),
using the following field:

| Field | Description | Required |
|-------|-------------|----------|
| **SIOS Artifact Reference** | Artifact ID(s) this evidence's claim concerns (e.g., CSL-001, MAI-001) | No — only when applicable |
| **Reference Relationship Type** | One of: Cites-Undeclared, Contradicts-Constitutional-Claim, Confirms-Constitutional-Claim, Extends-Constitutional-Model | Yes, if SIOS Artifact Reference is populated |

**Example (retroactively describing EV-000003 in the new schema):**

SIOS Artifact Reference: CSL-001, MAI-001
Reference Relationship Type: Cites-Undeclared
(CSL-001 cites RFC 2119/8174; MAI-001 has no corresponding registration)

This field is distinct from the Source ID field (§6), which SHALL continue to reference only
external Sources (SRC-XXXXXX). SIOS's own constitutional artifacts are never registered as
SRC-XXXXXX (per AERA-001D §4.1, they are Constitutional Documents, a different artifact type),
so a separate field is required rather than overloading Source ID.
```

---

## Impact Assessment

| Proposal | Breaking? | Backward Compatible? | Existing Records Affected |
|---|---|---|---|
| 1 (EUM-001) | No | Yes — purely additive documentation | None require modification; EV-000001 through EV-000006 remain valid, can optionally backfill Researcher's Note per EUM-R-001 |
| 2 (ERS-001) | No | Yes — new optional fields | EV-000003 could be retroactively updated to populate the new fields, but its existing Context Summary prose remains valid without the update |

**Neither proposal requires touching SIOS-BASELINE-001, SIOS-MAN-001, or any Frozen constitutional document** — both are scoped entirely within 02-Research specifications, consistent with AC-001-REASSESSMENT.md's conclusion that a Core Layer is not needed to fix what this pilot actually found.

---

## Recommended Governance Path

1. Proposal 1 → Editorial Review (per AERA-001F §5.1) — lowest friction, purely clarifying.
2. Proposal 2 → Architecture Review (per AERA-001F §5.2) — slightly higher bar since it adds a new structural field, but still Minor, not Major (no existing behavior changes, only a new optional capability).
3. Both proposals should be reviewed together since Proposal 2's example directly depends on EV-000003, which itself depends on the audit finding these very proposals are responding to — reviewing them separately risks losing that context.

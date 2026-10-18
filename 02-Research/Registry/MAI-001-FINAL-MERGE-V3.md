# MAI-001 — Final Merge (v3) + One More Discovered Inconsistency

**Supersedes:** MAI-001-REGISTRY-DELTA-V2.md
**Date:** 2026-08-04 (continued session)

---

## ⚠️ A Structural Inconsistency in MAI-001 Itself, Found While Preparing This Merge

Before merging, close inspection of the **original, frozen MAI-001** table structure reveals an inconsistency:

- **Domain 02 § Search** already mixes two different kinds of artifact: *methodology specifications* (SQP-001, SRE-001, SRL-001) **and** *individual instance records* (SRE-000001, SRE-000001-A, SRC-000001 — a specific execution and a specific source, not a schema).
- **Domain 02 § Corpus** and **§ Evidence**, by contrast, list *only* methodology specifications (COR-001/002/003; EUM-001/EUM-001B/ERS-001) — no individual SRC-XXXXXX or EV-XXXXXX instances appear, even though SRC-000001 (an instance) is registered under Search.

**This means MAI-001 does not currently have a consistent policy on whether individual data instances (as opposed to schemas/methodologies) belong in the Master Artifact Index at all.** This wasn't visible until an actual attempt was made to merge 16 real sources and 10 evidence records back into the registry — exactly the kind of gap that, per this pilot's recurring theme, only surfaces when the system is actually used at volume, not when it's just read.

**This should be resolved as a governance decision before merging SRC/EV instances**, not decided unilaterally here. Two honest options:

| Option | Description | Consequence |
|---|---|---|
| A | MAI-001 registers all instances (as Search currently, inconsistently, already does) | Registry will grow to thousands of rows as corpus scales — may need a "Registry of Registries" pattern instead |
| B | MAI-001 registers only methodology-level artifacts; instances live in domain-specific sub-registries (e.g., a dedicated Corpus Registry, Evidence Registry) that MAI-001 references but doesn't enumerate | More scalable; requires **new** sub-registry artifacts to be created (none currently exist for Corpus/Evidence, unlike Search which has SRL-001 serving loosely as this role) |

**This merge proceeds with Option A only for the specific artifacts that already have precedent (Search-domain execution records), and explicitly defers SRC/EV instance registration until this option is chosen** — rather than silently picking one and hoping nobody notices the inconsistency it would create with the Corpus/Evidence sections.

---

## What This Merge Actually Applies (Option-A-consistent, precedent-based additions only)

### Domain 02 — Research § Search (extends existing table, consistent with existing SRE-000001/SRE-000001-A precedent)

| Artifact ID | Status | Version | Path |
|-------------|--------|---------|------|
| SRE-000001-A | **Failed** *(corrected from implicit "pending")* | 1.0.0 | 02-Research/Search/SRE-000001-A.md |
| SRE-000001-B | Draft | 1.0.0 | 02-Research/Search/SRE-000001-B.md |
| SRE-000001-C | Draft | 1.0.0 | 02-Research/Search/SRE-000001-C.md |
| SRE-000001-D | Draft | 1.0.0 | 02-Research/Search/SRE-000001-D.md |
| SRE-000001-E | Draft | 1.0.0 | 02-Research/Search/SRE-000001-E.md |

### Domain 03 — Framework (unambiguous — these are methodology-level artifacts, first ever proposed for this domain)

| Artifact ID | Status | Version | Path |
|-------------|--------|---------|------|
| KOM-001 | Draft | 0.1.0-draft.1 | 03-Framework/Specifications/KOM-001.md |
| KSM-001 | Draft | 0.1.0-draft.1 | 03-Framework/Specifications/KSM-001.md |

---

## Deferred Pending Governance Decision (Option A vs B above)

- SRC-000002 through SRC-000016 (15 source instances)
- EV-000001 through EV-000009 (10 evidence instances, counting the split/superseded records)

**These are real, are traceable, and exist as working files — they are simply not yet placed into MAI-001 because doing so would either (a) perpetuate an existing inconsistency at larger scale, or (b) require a new sub-registry artifact this pilot is not authorized to unilaterally create.** This is the correct, disciplined stopping point — not a gap being hidden, but a governance question being correctly escalated rather than silently resolved by whoever happened to be doing the merge.

---

## Recommended Next Governance Action

Raise **"MAI-001 Instance Registration Policy (Option A vs B)"** as a Structural-tier decision (per the discussion's own proposed 3-tier governance model: Editorial/Structural/Architectural) — it changes a convention, not a breaking structural rule, but it's bigger than a pure Compatible edit since it determines how every future pilot's output gets registered. This single decision, once made, unblocks merging all 25 deferred instances in one pass.

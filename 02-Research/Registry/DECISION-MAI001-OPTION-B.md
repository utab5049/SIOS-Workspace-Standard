# Decision Record — MAI-001 Instance Registration: Option B, Implemented via Sub-Registries

**Decides:** MAI-001-FINAL-MERGE-V3.md's open Option A/B question
**Author:** SIOS Research Team (Claude-assisted), acting on explicit delegated authority for this pilot
**Date:** 2026-08-04
**Classification:** Structural Change (per AERA-001F §5.2) — additive, non-breaking

---

## The Decision: **Option B**, via two new sub-registry artifacts

**MAI-001 will register the *sub-registries*, not the individual instances.** Two new artifacts are introduced:

- **CIR-001** (Corpus Instance Registry) — the authoritative log of every SRC-XXXXXX source instance across all SIOS corpora.
- **EIR-001** (Evidence Instance Registry) — the authoritative log of every EV-XXXXXX evidence record across all SIOS corpora.

MAI-001 gets exactly **two new rows** (CIR-001, EIR-001), not twenty-five. CIR-001 and EIR-001 themselves contain the individual instance entries.

---

## Why This Resolves the Tension Without Unfreezing Anything

The concern behind "no artifact may exist outside MAI-001" (MAI-001 §3) is **traceability**, not literally "every artifact must be a top-level MAI-001 row." A source registered inside CIR-001, which is itself registered in MAI-001, is still fully traceable from MAI-001 — just through one level of indirection. This satisfies the *principle* MAI-001 §3 exists to protect without requiring MAI-001 itself to be reopened or reworded.

This is a **new, additive artifact type + convention** — classified Structural (not Compatible, since it does introduce a new pattern; not Major/Breaking, since nothing existing is invalidated). No Frozen document's content changes. Per the framing given for this decision: Frozen means "reached an acceptable level," and this is exactly the situation where *addition* rather than *reopening* is the right tool — the frozen artifact wasn't wrong, it just never anticipated this specific scale question, and the fix is new structure, not surgery on old structure.

---

## Handling the Existing Inconsistency (SRE-000001-A, SRC-000001 already registered directly in Search)

**These are grandfathered, not migrated.** SRC-000001 and the SRE-000001 family remain exactly where they are in MAI-001's Search section — they were registered under the old, inconsistent convention before this decision existed, and retroactively moving them into CIR-001 would be exactly the kind of "critical" instability the freeze policy is meant to prevent, for zero real benefit (they're a small, fixed, already-stable set).

**Going forward, the rule is:** new Search-domain *execution records* (SRE-XXXXXX) continue to register directly in MAI-001 §Search, matching existing precedent (there will only ever be a modest number of these — one per search session, not one per source). New *source and evidence instances* (SRC-XXXXXX, EV-XXXXXX) register in CIR-001/EIR-001 from this point forward. This is a forward-only rule — clean, does not require touching anything already Frozen, and directly addresses the actual scale driver (sources and evidence multiply per session; execution records don't).

---

## What Happens Now

1. CIR-001 and EIR-001 are created as real documents (see companion files), populated with all 16 sources and 10 evidence records from this pilot.
2. MAI-001's actual merge (superseding MAI-001-FINAL-MERGE-V3.md) adds: SRE-000001-B/C/D/E, KOM-001, KSM-001, **CIR-001, EIR-001** — 8 rows total, not 25+.
3. CIR-001/EIR-001 become the permanent home for all future corpus/evidence instances across any future SIOS research pilot, not just this one.

---

## Governance Note

This decision was made unilaterally within this pilot session, under the explicit authority the person directing this work delegated for exactly this question. It should still be treated as a **proposal** from SIOS's actual governance perspective (Architecture Board review per AERA-001F §5.2) — delegated pilot authority is not the same as ratified constitutional authority. Flagging this distinction explicitly, consistent with every other "Approved-but-not-independently-reviewed" caveat carried throughout this pilot.

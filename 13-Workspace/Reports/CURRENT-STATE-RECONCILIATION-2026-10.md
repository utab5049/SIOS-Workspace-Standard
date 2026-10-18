# Current-State Reconciliation — 2026-10-18

**Status:** Audit finding / proposed reconciliation. This document does not itself ratify governance decisions or change any canonical artifact.
**Scope:** Read-only comparison of the current `main` branch's registry, decision records, audit reports, status reports, and roadmap.
**Method limitation:** This is a repository-document review. It does not establish who exercised real-world governance authority, independently re-run the human reviews, or execute the Runner.

## Executive finding

The repository contains a substantial research-pilot record, but its *current governance state is not safely inferable from a single document*. Some files appear to be historical snapshots; others claim later decisions without consistently recording enough date, authority, and supersession metadata to prove that relationship. Do not treat every conflict as a live contradiction, and do not resolve one by simply choosing the most confident wording.

## Evidence reviewed

- `01-Foundation/Registry/MAI-001.md` — identifies itself as amended v1.1.0 and lists CIR-001, EIR-001, ENR-000001/2, KOM-001 and KSM-001 with registered/approved states.
- `02-Research/Registry/C1-RATIFIED-FINAL.md` — says C1 was ratified, records five conditions, and says three blind tests (#1, #2 and #4) were used.
- `02-Research/Registry/DECISIONS-RECORDED.md` — still says C1 is “Do not ratify yet” and “Blocked on independent sample review.”
- `02-Research/Audit/ICRAA-Part1.md` and `ICRAA-Part2.md` — dated 2026-08-12; describe C1/C4 and independent-review status as unresolved in the document set they audited.
- `02-Research/Registry/MAI-001-FINAL-MERGE-V5.md` — describes a post-ratification merge, but is a proposed/merge record rather than a substitute for verifying the live canonical file.
- `13-Workspace/Reports/COMPREHENSIVE-STATUS-REPORT.md` and `CHANGELOG.md` — claim two governance decisions were ratified and four independent blind human reviews occurred.
- `13-Workspace/Reports/FINAL-REPORT.md` — the original pilot report explicitly caveats the first pilot as a single-session effort without a genuinely independent reviewer.

## Reconciliation register

| ID | Topic | What the files say | Safe disposition |
|---|---|---|---|
| R-01 | C1 status | C1-RATIFIED-FINAL says ratified; DECISIONS-RECORDED still says blocked; ICRAA describes the earlier unresolved state. | Likely a stale decision snapshot, but the repository does not make the supersession chain explicit. Preserve both records; identify the authoritative later decision and its date/authority before editing status. |
| R-02 | Independent reviews | C1 lists tests #1, #2 and #4 as the basis for ratification; README/status/changelog claim four blind reviews; ICRAA says no qualifying independent review was established in the state it examined. | Do not collapse “tests,” “review sessions,” and “independent reviewers” into one count. Add a dated review ledger with reviewer independence, artifact scope, result, corrections, and evidence links. |
| R-03 | C3 / MAI schema | MAI-001 §4 describes the registry table as a summary view; DECISIONS-RECORDED says Option 3A was executed; ICRAA records the earlier schema mismatch as unresolved. | Current MAI-001 appears to contain the clarification. Treat the audit finding as historical unless a current schema check finds a remaining defect. |
| R-04 | Canonical registration | Current MAI-001 lists the pilot registries/framework artifacts; ICRAA questions whether pilot-generated decisions had authority to cross into canonical status. | Separate “present in the canonical file” from “approved by an authorized governance actor.” File presence alone does not prove authority. |
| R-05 | Runner execution | ARR-001 / ARR-001A–C are specifications; ICRAA says no ARR-001C code execution was evidenced in its audit. | Record Runner as “specification present; executable implementation and repeatable run not yet evidenced by this review.” Do not claim it is implemented or tested. |
| R-06 | Source depth and retrieval | FINAL-REPORT records 13/16 sources as abstract-level at that time and OpenAlex access failures; PHASE-5-KICKOFF advises against speculative API automation. | Preserve these as historical pilot/environment facts; retest access only in the target execution environment before designing an adapter around it. |

## Required decisions before implementation work

1. **Establish the governance timeline.** Add dates and references linking proposal → review → decision → application. Explicitly mark superseded snapshots as historical without deleting them.
2. **Confirm authority, not just status text.** Identify who had authority to ratify C1 and C3 and link the actual decision evidence. If this cannot be demonstrated, use “authority unverified” rather than silently reverting or re-ratifying.
3. **Create a review ledger.** For each blind review, record a stable review ID, date, reviewer type/independence basis, exact artifact versions reviewed, findings, corrections applied, and evidence location. Do not publish private reviewer details unnecessarily.
4. **Run a mechanical registry consistency check.** Verify each MAI-001 path exists; registered IDs and versions agree with document headers; and every claimed approval has a traceable decision reference.
5. **Only after the above, decide whether further independent review is still a blocker.** The C1 conditions say future blind tests are monitoring, while ICRAA's exit criteria demand additional reviews. A governance owner must reconcile that difference; implementation work should not decide it implicitly.

## Acceptance criteria for closing this reconciliation

- [ ] One dated governance timeline identifies the current decision for C1 and C3 and the records it supersedes.
- [ ] Authority evidence is linked, or the status is explicitly marked “authority unverified.”
- [ ] Review counts are supported by a ledger and distinguish tests from independent reviewers.
- [ ] A registry validator reports missing paths, duplicate IDs, header/registry mismatches, and unresolved status references.
- [ ] The Runner remains classified by observed evidence, not by specification language.

## Decision boundary

This reconciliation intentionally does **not** edit MAI-001, mark governance decisions approved/rejected, rewrite the historical ICRAA audit, or claim external validation. Those changes require evidence or an authorized decision, not editorial inference.

## Source links

- [MAI-001](../../01-Foundation/Registry/MAI-001.md)
- [C1 ratification record](../../02-Research/Registry/C1-RATIFIED-FINAL.md)
- [Recorded decisions](../../02-Research/Registry/DECISIONS-RECORDED.md)
- [ICRAA Part 1](../../02-Research/Audit/ICRAA-Part1.md)
- [ICRAA Part 2](../../02-Research/Audit/ICRAA-Part2.md)
- [Pilot final report](FINAL-REPORT.md)
- [Phase 5 kickoff](PHASE-5-KICKOFF.md)

## Review-stage artifacts added on 2026-10-18

- `02-Research/Audit/REVIEW-LEDGER.md` provides a ledger template for reconciling review-event claims. Its TBD rows are tasks, not accepted evidence.
- `02-Research/Audit/INDEPENDENT-REVIEW-PROTOCOL.md` proposes a version-pinned external review method. It remains proposed until the maintainer approves it.

These artifacts prepare the next stage; they do not constitute an independent review, verify the historical count of reviews, or resolve C1/C3 authority. The independent-review stage remains open until actual review evidence is recorded and a governance owner accepts or rejects it.

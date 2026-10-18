# Phase 15 — Registry Governance Decision Report

**Date:** 2026-10-18  
**Base reviewed:** `main` at `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Status:** Decision brief only — no authority source selected, no registry corrected, and no governance decision ratified.

## Executive summary

The repository contains mutually incompatible statements about canonical registration. `01-Foundation/Registry/MAI-001.md` calls itself the authoritative source of truth and lists numerous artifacts with statuses. `12-Registry/README.md` and `12-Registry/INDEX.md` both say that no artifacts are registered. The conflict is not limited to those three files: governance records disagree about whether C1 was ratified, while the review ledger and final pilot report describe independent-review evidence as unverified or absent.

The evidence does **not** justify silently selecting one source and editing the others. This report lays out the evidence, options, consequences, and a controlled decision path. It does not choose the authoritative source.

## 1. Evidence observed in the current repository

### E1 — MAI-001 asserts authority and records entries

File: `01-Foundation/Registry/MAI-001.md`

The document states, in §3, “No artifact may exist outside MAI-001. MAI-001 is the authoritative source of truth.” Its §5 lists artifacts across multiple domains, including statuses such as Frozen, Approved, Registered, and Failed. The header describes the file as “Frozen v1.1.0 (amended)” and says entries were added per C1 ratification in August 2026.

**What this establishes:** the current file asserts canonical authority and contains registration entries.  
**What this does not establish:** that the authority claim or all statuses were validly approved by the proper governance owner.

### E2 — The secondary registry landing pages assert an empty registry

Files:
- `12-Registry/README.md`
- `12-Registry/INDEX.md`

Both state: “No artifacts currently registered.”

**What this establishes:** the statements directly contradict the populated MAI-001 §5 if they are intended to describe the same canonical registry state.  
**What remains unknown:** whether these files are intended as live registry inventories, empty-folder placeholders, or outdated landing-page text. No scope qualification explains the discrepancy.

### E3 — C1 decision records disagree

File: `02-Research/Registry/C1-RATIFIED-FINAL.md`

This record says C1 moved from “do not ratify yet” to “Ratified,” records conditions, and says registration was applied.

File: `02-Research/Registry/DECISIONS-RECORDED.md`

This record says C1 is “1B — Do not ratify yet,” “Blocked on independent sample review,” and that no pilot artifact is canonically registered until that review occurs.

These are incompatible decision states for the same decision. The files do not, by themselves, establish which record superseded the other or whether the author of the later-looking record had the required decision authority.

### E4 — The evidence of independent review is explicitly unreconciled

File: `02-Research/Audit/REVIEW-LEDGER.md`

The ledger labels itself “Template / evidence not yet reconciled.” It records TBD rows for tests #1, #2, and #4, says reviewer identity/type, independence basis, exact versions, and source evidence are not verified, and warns that the rows are reconciliation tasks rather than accepted proof that four qualifying reviews occurred.

File: `02-Research/Audit/INDEPENDENT-REVIEW-PROTOCOL.md`

The protocol is marked **Proposed** and says the independent-review stage is not complete. It requires a version-pinned package, independence declaration, traceable findings, and a governance-owner decision.

File: `13-Workspace/Reports/FINAL-REPORT.md`

The pilot report says no genuinely independent reviewer was available during the pilot, describes approvals as produced by the same reasoning process run again, and says the MAI-001 delta had not been merged at that time.

File: `02-Research/Audit/Blind-Tests/TEST3-CORRECTION-AND-ERS-RULE.md`

The correction report says Package #3 paraphrased source material in a way that introduced a temporal imprecision and blended evidence with process commentary; it says C1 remains blocked and a faithful test of the real artifacts was still needed.

**What this establishes:** the repository contains material caveats and explicit unresolved review evidence.  
**What this does not establish:** that no valid independent review could have occurred later. That requires locating and verifying original review records and their timestamps.

### E5 — A prior implementation decision itself labels authority as provisional

File: `02-Research/Registry/DECISION-MAI001-OPTION-B.md`

This record says the Option B implementation was made under delegated authority for the pilot, but should still be treated as a proposal from SIOS's actual governance perspective pending Architecture Board review.

### E6 — Historical records have different time scopes

The final pilot report is dated 2026-08-04, while the registry header describes amendments and C1 ratification during August. Some statements may have been superseded after their creation. However, the repository lacks a clear, mutually consistent supersession chain that conclusively explains the present conflict. File timestamps or wording alone should not be treated as proof of valid governance authority.

## 2. Conflict map

| Question | Evidence in tension | Why it matters |
|---|---|---|
| Which file defines canonical registration? | MAI-001 claims authority; README and INDEX claim empty state | Validators, maintainers, and future tooling can reach opposite conclusions |
| Was C1 ratified? | C1-RATIFIED-FINAL says ratified; DECISIONS-RECORDED says blocked | Artifact statuses may depend on a decision whose final state is unclear |
| Is independent review complete? | Ratification record claims three independent reviews; REVIEW-LEDGER says evidence not verified; final pilot report says no genuinely independent reviewer existed during the pilot | The registration decision may rely on review claims that are not yet traceable |
| Which source supersedes which? | Multiple status records without a clearly evidenced supersession/authority chain | Editing based on chronology or wording alone risks inventing authority |
| Are README/INDEX intended as authoritative inventories? | Both are under `12-Registry`, but their scope is undocumented | They may be stale placeholders or genuine statements of registry state |

## 3. Decision options

### Option A — Treat MAI-001 as authoritative and reconcile the secondary pages

**Action:** Preserve MAI-001 as canonical; replace the two “No artifacts currently registered” statements with accurate scope-qualified links or generated summaries.

**Benefits**
- Aligns with MAI-001 §3's explicit authority statement.
- Gives maintainers and tools one obvious starting point.
- Avoids treating a likely placeholder as stronger than the declared canonical index.

**Risks / prerequisites**
- Does not by itself resolve the C1 ratification conflict.
- Could prematurely publish “Approved” or “Registered” statuses if the underlying decision lacks valid authority.
- Requires confirming whether README/INDEX are intended to be derivative views or separate registries.

**Decision authority needed:** Confirm that MAI-001's authority statement remains valid and clarify the scope of the secondary pages; separately resolve C1 evidence.

### Option B — Treat the secondary registry pages as authoritative and revise MAI-001

**Action:** Retain the empty-registry state in `12-Registry`; revise MAI-001 entries/statuses so they are not presented as canonically registered until accepted through the designated process.

**Benefits**
- Conservative if governance determines the C1 ratification was not valid.
- Prevents uncertain pilot outputs from being treated as formally registered.

**Risks / prerequisites**
- Conflicts with MAI-001's explicit “authoritative source of truth” statement.
- Could erase or downgrade historical status without sufficient provenance if done as a simple edit.
- Requires an explicit governance decision to supersede or reinterpret MAI-001's authority clause.

**Decision authority needed:** Explicitly authorize a change to MAI-001's authority/status model and preserve the prior state in history.

### Option C — Preserve the conflict temporarily and perform a version-pinned governance reconciliation

**Action:** Make no status or authority changes yet. Collect original decision evidence, exact reviewed artifact versions, review packages/results, and the approval authority basis. Then issue one explicit decision record identifying the authoritative source, C1 state, effective date, and superseded records. Only after that decision, update the affected pages in a separate implementation PR.

**Benefits**
- Avoids inventing authority from inconsistent documents.
- Separates factual evidence gathering, governance decision, and mechanical file edits.
- Leaves a clear audit trail and supports independent review.

**Costs / risks**
- Leaves the contradictory public state in place temporarily.
- Requires additional evidence collection and a decision owner.
- Tooling should continue to flag the conflict rather than suppress it.

**Decision authority needed:** The designated SIOS governance owner must make or confirm the decision after reviewing the evidence.

### Option D — Split the concepts: MAI-001 as canonical artifact index, 12-Registry as a separate operational registry

**Action:** Define the distinct purpose and scope of each location; rename/reword the secondary pages and specify their relationship to MAI-001.

**Benefits**
- Could resolve the apparent contradiction if the pages serve different purposes.
- Allows separate operational registries without weakening the canonical index.

**Risks / prerequisites**
- The current README and INDEX do not document such a distinction.
- This option must not be used to rationalize the conflict after the fact without evidence of intended design.
- Requires a new, explicit architecture/governance decision and validator scope rules.

**Decision authority needed:** Confirm the intended registry architecture and specify which claims each validator is responsible for checking.

## 4. Comparative summary

| Criterion | A: MAI-001 canonical | B: Secondary pages canonical | C: Evidence-first reconciliation | D: Distinct scopes |
|---|---|---|---|---|
| Fastest immediate cleanup | High | Medium | Low | Medium |
| Preserves current evidence without assuming authority | Low–Medium | Low–Medium | **High** | Medium |
| Resolves C1 review evidence | No | No | **Yes, as a required prerequisite** | No, not by itself |
| Risk of prematurely asserting registration | Medium–High | Medium | **Low** | Medium |
| Requires a new governance decision | Confirm/clarify | Yes | Yes, after evidence collection | Yes |

## 5. Proposed decision sequence (process recommendation, not a source selection)

1. **Freeze the evidence snapshot:** record the main commit SHA and hash/version of each relevant file; do not edit the disputed registry documents during evidence collection.
2. **Reconcile the decision history:** determine which C1 decision record was authored/approved by the authorized decision owner, whether a later decision explicitly superseded an earlier one, and whether the required independent review occurred.
3. **Verify original review evidence:** map each claimed review to a unique event, exact artifact versions/commit, reviewer type and independence basis, package presented, raw output, corrections, and disposition. Do not count a summary or ratification record as a substitute for the underlying review.
4. **Obtain an explicit governance decision:** choose A, B, C, or D (or record a reasoned alternative); state authority basis, scope, effective date, superseded records, and any remaining conditions.
5. **Implement separately:** only after the decision is recorded, create a small PR that updates MAI-001/README/INDEX and any status records required by that decision. Keep the validator's discrepancy check until the documents and the chosen rules genuinely agree.
6. **Validate and report:** run CI, inspect the diff, and update the review ledger and public summary to match the accepted decision. Do not infer Runner execution or broader research validity from passing registry tests.

## 6. Decision record template

- **Decision ID:**
- **Decision owner / authority basis:**
- **Selected option (A/B/C/D/other):**
- **Evidence snapshot commit:**
- **C1 final state and rationale:**
- **Independent-review evidence accepted / rejected / pending:**
- **Canonical registry definition:**
- **Treatment of README and INDEX:**
- **Records superseded (with reasons):**
- **Remaining risks and conditions:**
- **Effective date:**
- **Implementation PR:**

## 7. Current disposition

**No option is selected in this report.** No file in the disputed registry or decision record set is changed by this phase. The report is intended to make the decision explicit and auditable, not to substitute for the governance owner's authority.

The registry validator should continue to report the contradiction until the governance decision is recorded and the resulting source documents are made consistent.

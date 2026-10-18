# Independent Review Ledger

**Purpose:** Record review evidence in a way that can be independently checked.  
**Status:** Template / evidence not yet reconciled.  
**Authority:** This ledger does not ratify decisions or certify independence by itself.

## Rules

- One row per review event, not one row per artifact or finding.
- Record the exact artifact version or commit SHA reviewed.
- Distinguish a human reviewer, an AI-assisted review, and an automated test.
- A review is not “independent” merely because it used a separate chat, prompt, or model. Record the actual independence basis.
- Do not publish personal contact details or confidential reviewer information. A stable reviewer alias is sufficient.
- Keep raw review evidence at a controlled location and link it where disclosure is appropriate.
- Never infer a review outcome from a ratification record alone.

## Review event register

| Review ID | Date (UTC) | Reviewer alias/type | Independence basis | Blind conditions | Artifact/version or commit | Method / sample | Outcome | Findings and corrections | Evidence link | Verification status |
|---|---|---|---|---|---|---|---|---|---|---|
| TBD-001 | Not verified | Not verified | Not verified | Not verified | C1-related review; exact version TBD | Referenced as test #1 in C1 ratification record; details to verify | Not independently verified by this ledger | Obtain original review package and map corrections | TBD | Pending evidence |
| TBD-002 | Not verified | Not verified | Not verified | Not verified | C1-related review; exact version TBD | Referenced as test #2 in C1 ratification record; details to verify | Not independently verified by this ledger | Obtain original review package and map corrections | TBD | Pending evidence |
| TBD-003 | Not verified | Not verified | Not verified | Not verified | C1-related review; exact version TBD | Referenced as test #4 in C1 ratification record; details to verify | Not independently verified by this ledger | Obtain original review package and map corrections | TBD | Pending evidence |
| TBD-004 | Not verified | Not verified | Not verified | Not verified | Scope/version TBD | Summary documents claim four blind human reviews; identity and scope of the fourth event must be reconciled | Claim only; not verified by this ledger | Locate the fourth event and determine whether it is distinct from the three above | TBD | Pending evidence |

> The TBD rows above are **reconciliation tasks, not accepted evidence that four qualifying independent reviews occurred**. Replace or close them only after inspecting original records. If two rows refer to the same event, merge the records and preserve the rationale.

## Verification checklist

- [ ] Each event has a unique stable ID and date.
- [ ] Exact reviewed artifact versions or commit SHAs are recorded.
- [ ] Reviewer type and independence basis are explicit.
- [ ] Blindness conditions are documented rather than inferred from the title “blind test.”
- [ ] Review method, sample, rubric, and outcome are available.
- [ ] Every finding is linked to a correction, accepted risk, or explicit unresolved state.
- [ ] The decision owner has confirmed which reviews satisfy the relevant governance requirement.
- [ ] Summary counts match the ledger and distinguish review events from independent reviewers.

## Status vocabulary

- **Pending evidence** — a claim or reference exists, but supporting material has not been checked.
- **Evidence located** — original material was found; no quality judgment implied.
- **Verified** — metadata and source material were checked against this ledger's requirements.
- **Does not qualify** — a decision owner or documented rule determined that the event does not satisfy the requirement.
- **Superseded** — the event was replaced or corrected; retain its history.

## Change history

| Date | Change | Author / role |
|---|---|---|
| 2026-10-18 | Initial ledger template created to reconcile review claims; no review was independently performed by creating this file. | SIOS maintainer workflow |

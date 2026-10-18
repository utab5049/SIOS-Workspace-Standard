# Pull Request Chain Audit — 2026-10

**Status:** Operational audit only. This report does not merge, close, retarget, or otherwise mutate any pull request.

## Findings

The audit inspected open PR metadata for PRs #1–#13 and compared adjacent phase branches through Phase 11. All thirteen PRs were reported open and unmerged at the time of inspection.

### Phase branch ancestry

Comparisons of the named phase branches show each successive phase branch is ahead of the previous branch and not behind it. The adjacent diffs match the intended sequence:

1. Phase 1 → 2: add the read-only registry consistency validator and initial tests.
2. Phase 2 → 3: add CI workflow and CI documentation.
3. Phase 3 → 4: extend registry-validator tests.
4. Phase 4 → 5: add proposed manifest contract and JSON Schema.
5. Phase 5 → 6: add the application manifest validator and tests.
6. Phase 6 → 7: add schema/validator compatibility tests and constants.
7. Phase 7 → 8: add Draft 2020-12 conformance tests and test dependency.
8. Phase 8 → 9: add synthetic parity fixtures and comparison tests.
9. Phase 9 → 10: add the validation coverage matrix and documentation link.
10. Phase 10 → 11: add CLI/edge-case tests and update the coverage matrix and tools README.

This supports the technical ancestry of the phase branches. It does not by itself prove that each PR is ready to merge or that external review has occurred.

## Duplicate PR candidates

Two open PRs point at the exact same head branch and head commit as their intended stacked PR, but target `main` instead of the phase parent and have empty descriptions:

| Candidate | Intended phase PR | Verified relationship | Recommended handling |
|---|---|---|---|
| PR #5 — “Work/phase 4 validator test hardening” | PR #4 | Both use head `work/phase-4-validator-test-hardening` at `f8c4bcdfb092b70cde3a89d70f2b31c577eeb779`; PR #5 targets `main`, while PR #4 targets Phase 3. | Treat PR #5 as a duplicate candidate; confirm then close as duplicate, or retarget only if there is a deliberate reason. |
| PR #10 — “Work/phase 5 registry data contract” | PR #6 | Both use head `work/phase-5-registry-data-contract` at `6a50bf126b0321e1261e610b02e543fad28f0cb7`; PR #10 targets `main`, while PR #6 targets Phase 4. | Treat PR #10 as a duplicate candidate; confirm then close as duplicate, or retarget only if there is a deliberate reason. |

Neither candidate was closed automatically in this audit. Their target branches and duplicate relationships should be reviewed before any mutation.

## Merge sequencing

The intended dependency chain is PR #1 → #2 → #3 → #4 → #6 → #7 → #8 → #9 → #11 → #12 → #13. PR #5 and PR #10 are duplicate candidates and should not be included in the main sequence unless explicitly resolved.

Recommended procedure:
1. Confirm the duplicate candidates (#5 and #10), then close them as duplicates if appropriate.
2. Review and merge PR #1 only after the repository owner is satisfied with its documentation and checks.
3. After each parent merge, retarget the next stacked PR to the newly merged base (normally `main`) and confirm its diff contains only the intended phase change.
4. Re-run CI after retargeting and before merge; do not assume a previous stacked-branch check alone is sufficient.
5. Continue one PR at a time, verifying the resulting diff and tests after each merge.

## Governance and safety constraints

- Do not bulk-merge the stack.
- Do not interpret an open PR's `mergeable` metadata as approval or independent review.
- Do not edit MAI-001 or secondary registry documents as part of PR housekeeping.
- Keep the manifest schema in `proposed` state. No production manifest or authority decision is implied.
- The SIOS Runner remains outside the scope of this branch audit; this report makes no claim that it has executed.

## Evidence boundary

The ancestry conclusions above are based on GitHub PR metadata and adjacent-branch comparisons performed for this audit. This is an operational chain check, not an independent review of the project, its governance claims, or the semantic correctness of the validator.

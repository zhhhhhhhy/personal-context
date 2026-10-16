# Existing-memory refinement

## IT-MR-001: Separate reusable context from project execution history

- Date: 2026-10-16
- Status: resolved for the approved organization; usefulness awaits user assessment.
- Problem and user impact: 19 active memories mixed preferences, methods, project facts and old execution choices; future tasks could load stale or unrelated instructions.
- Acceptance condition: exact 6 retained / 5 merged / 5 project / 3 archived mapping, without discarding potentially live constraints or publishing private material; sparse retrieval still finds relevant preferences and project issues.
- Proposed method: freeze the existing IDs, compare source task/version boundaries and local project artifacts, then use guarded lifecycle transactions. Consolidate methods into complete canonical Skills and route project material explicitly.
- Work performed: concise replacements, four engineering-method merges and one academic-method merge, five project entries, three archived execution records; retained their task-specific constraints in project pages. Local Task Graph MVP scope differed from its original design, so the new project summary was corrected in a second transaction. Two Skill packages synchronized after checking intervening runtime edits.
- Observed result: exact mapping passed; 6 active reusable memories, including 1 local-only; 5 active project records. Default keyword search excludes project material; known-project search preserves matching general preferences. Core200's pending human-review claims remain pending. Protected user edits were unchanged. The six retained content payloads shrank from 776 to 500 o200k_base tokens under an identical field protocol.
- Evidence: [validation.json](validation.json), [version-checks.json](version-checks.json), [budget.json](budget.json), [REPORT.md](REPORT.md), [WORKFLOW_STATE.md](WORKFLOW_STATE.md).
- Remaining limitation: remote current roots/commits, research records, implementation status and user usefulness were not newly verified. No fresh conversation cohort was processed.
- Next method for this problem: collect the user's corrections on these six memories and scoped project materials before importing another cohort.

## Execution issues retained for reuse

- Conversation filenames use creation dates. DemoPilot's first journal was created on October 5, but all three relevant user messages were on October 6; project versions use the message timestamps.
- `codex-visual` is not a Git checkout. Its current specification check is anchored by the actual file SHA-256; no commit was invented. The read-only MVP contract differs from historical mixed-acceptance intent, which remains in history.
- A controller checkpoint rejected the unsupported status `active` before content mutation. The documented status `in_progress` was used; the workflow was not reinitialized and history was preserved.
- Disabling Git autocrlf for a diff check treated existing CRLF as trailing whitespace. The repository-normalized check passed without normalizing or overwriting the user's existing communication edit.

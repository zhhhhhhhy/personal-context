# Transaction-State Record

## Purpose

The transaction-state record preserves the current state of a material engineering task across long turns, context compaction, worker handoffs, tool failures, and model restarts. It is a task ledger, not a progress report: it must tell the next agent what the single objective is, what has actually happened, what remains, and what evidence is authoritative.

## Workflow stages

The ledger follows the Skill's fixed execution workflow:

`frame → initialize/recover → preflight → route → execute → observe/verify → commit state → report or continue`

Use the current phase and status to show where the task is in this sequence. A phase cannot be skipped because a later action appears convenient. If a required input or evidence is missing, keep the task at the current phase and record `blocked`, `needs_remote_check`, `verifying`, or `not_run` with the next action.

## Choose the document

- Reuse an existing project state, plan, or task-ledger document when it already has the fields below and is the agreed source of truth.
- Otherwise use the bundled controller with `docs/WORKFLOW_STATE.json` as the canonical machine state and `docs/WORKFLOW_STATE.md` as its human-readable mirror in a repository. For multiple independent initiatives, use `docs/<initiative>/WORKFLOW_STATE.json` and the matching `.md` mirror.
- For projectless work, use `work/WORKFLOW_STATE.json` and its matching `.md` mirror until the user-facing deliverable is ready. Keep the deliverable separate from the ledger.
- If an iteration document already exists, link the two documents. The state document holds the current state; the iteration document holds the historical methods and evidence. Do not maintain competing ledgers.

The controller is the canonical writer for the JSON and Markdown state pair. A pre-existing ledger may be reused only when it can represent the same fields and gates; pass its explicit paths to the controller rather than creating a second competing ledger. Manual Markdown-only updates are a fallback for inspection and reporting, not an execution gate for a material task.

## Required lifecycle

1. **Initialize before execution.** Record one canonical objective, scope, acceptance conditions, current phase, status, and the next action before delegation, mutation, remote work, or a long-running command.
2. **Record each attempt transactionally.** Before a state-changing action, append an attempt with its expected effect and owner. After it returns, record the result, evidence, failure cause, and resulting status. If the action was not recorded or its result cannot be verified, classify it as `not_run` or `unverified`.
3. **Reconcile at boundaries.** At phase changes, worker handoffs, tool errors, context compaction, or a resumed turn, read the ledger, inspect the current files/runtime, and correct stale fields before taking another action. Never repeat a completed action only because it is absent from the conversation summary.
4. **Close with evidence.** Set `completed` only when every acceptance condition has evidence. Otherwise use `verifying`, `reduced`, `blocked`, or `not_run` and state the exact next action.
5. **Preserve history.** Update the current-state fields in place, but append attempts and decisions. Do not delete a failed attempt to make the task appear complete.

## State schema

Use this compact Markdown structure unless the project has an equivalent machine-readable schema:

```markdown
# Workflow Transaction State

- Transaction ID: <stable id>
- Initiative: <project or task name>
- Objective: <one canonical user-visible outcome>
- Scope: <included work>
- Out of scope: <excluded work>
- Acceptance conditions:
  - [ ] <condition and required evidence>
- Status: planned | preflight | in_progress | waiting | verifying | reduced | completed | blocked | not_run
- Current phase: <phase>
- Gate checkpoints: route=<timestamp|not_run>, execute=<timestamp|not_run>, verify=<timestamp|not_run>, report=<timestamp|not_run>
- Source of truth: <files, commands, or system state that outrank chat summaries>
- Last verified: <timestamp>
- Last completed action: <action and evidence link>
- Next action: <one concrete action>
- Owner: <agent, worker, or human>
- Decisions and constraints:
  - <decision or constraint>
- Blockers and causes:
  - <blocker, root cause, and evidence; write `none` when clear>
- Artifacts:
  - <path or URL and what it proves>

## Attempt log

| Attempt | Time | Phase | Action and expected effect | Result | Evidence | Status |
|---|---|---|---|---|---|---|
| A-001 | YYYY-MM-DDThh:mm:ssZ | <phase> | <action> → <expected effect> | <observed result> | <path/command/log> | passed/failed/not_run/unverified |
```

The objective and acceptance conditions must not be silently rewritten when a new request arrives. If the user changes the goal or scope, append a decision explaining the change, update the acceptance conditions deliberately, and preserve the previous objective in the attempt history.

## Recovery protocol

When resuming a task, use this order:

1. Read the transaction-state document.
2. Check the current checkout/files, running processes or services, and the latest referenced evidence.
3. Reconcile stale or contradictory fields and record the reconciliation.
4. Continue only from the recorded next action, or mark the task blocked and ask for the missing decision.

Do not treat a memory entry, a compacted conversation, a worker's verbal summary, or a successful command launch as proof that the task is complete. The ledger must point to the evidence that establishes the actual acceptance condition.

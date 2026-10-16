# Workflow Controller

`scripts/workflow_controller.py` is the executable part of this Skill. The Skill decides what the workflow means; the controller keeps the transaction state, rejects out-of-order execution, and records evidence outside the model context. It does not run project commands itself.

## State files

Use `docs/WORKFLOW_STATE.json` and `docs/WORKFLOW_STATE.md` in a repository, or `work/WORKFLOW_STATE.json` and its `.md` mirror for projectless work. If the project already has a compatible ledger, pass its two paths explicitly. The JSON is the canonical source for automation; the Markdown file is for inspection, handoff, and reporting.

## Required sequence

Replace `<state>` and `<mirror>` with the project paths:

```text
python scripts/workflow_controller.py init --state <state> --markdown <mirror> --objective "..." --scope "..." --acceptance AC-1="..." --owner agent
python scripts/workflow_controller.py preflight --state <state> --markdown <mirror> --status ready --evidence "..."
python scripts/workflow_controller.py gate --state <state> --for-stage route
python scripts/workflow_controller.py gate --state <state> --for-stage execute
python scripts/workflow_controller.py begin-attempt --state <state> --markdown <mirror> --attempt-id A-001 --action "..." --expected-effect "..."
<perform one bounded action>
python scripts/workflow_controller.py finish-attempt --state <state> --markdown <mirror> --attempt-id A-001 --outcome passed --result "..." --evidence "..."
python scripts/workflow_controller.py gate --state <state> --for-stage verify
python scripts/workflow_controller.py verify --state <state> --markdown <mirror> --criterion AC-1 --result passed --evidence "..."
python scripts/workflow_controller.py gate --state <state> --for-stage report
```

Use `needs_remote_check` or `blocked` in `preflight` when the required evidence is missing. A gate exits non-zero when its prerequisites are not satisfied; stop at that phase and record the cause. Do not start a second attempt after a timeout until the original process, job, or artifact has been checked and the result is recorded.

## Recovery and workers

After compaction, handoff, a child-worker result, or a long-running command, run `status --json`, inspect the referenced files and runtime, and reconcile the state before continuing. A child worker must receive the state path, transaction ID, scope, and acceptance criteria. It either runs the controller for its own bounded attempt or returns an attempt record containing the same fields; the parent verifies the evidence before merging it into the transaction.

The controller does not prove that the right Skill was selected. Skill selection and loading remain an upstream routing boundary. This controller starts once the workflow is active and makes partial loading or skipped stages visible through missing state and failed gates.

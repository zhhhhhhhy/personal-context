---
name: engineering-project-workflow
description: "Use for material multi-step engineering implementation, fixes, evaluation, regression, integration and acceptance requiring preflight, task allocation, bounded attempts and evidence. Includes child steps of an active material project. Excludes standalone small edits, simple status replies and prose-only stakeholder reporting."
---

# Engineering Project Workflow

Keep one objective, task ownership, attempts and acceptance evidence in the project. Apply `minimal-validation-workflow` before selecting checks; use the smallest sufficient evidence and stop when it passes. Expand for an explicit contract, safety gate or newly observed risk. A required acceptance set cannot be replaced by a smoke test.

## Material task

Read [preflight](references/preflight-gate.md), [transaction state](references/transaction-state.md) and [controller](references/workflow-controller.md) before the first material action. Reuse a compatible canonical state; otherwise create `docs/WORKFLOW_STATE.json` plus its Markdown mirror, or a scoped initiative directory. The controller owns this pair.

1. Initialize/recover the objective, scope, acceptance, owner and next action.
2. Perform read-only preflight before implementation, delegation, model startup or remote/service mutation. Record command, report, status and unresolved checks. `ready` allows the next stage; `needs_remote_check` allows diagnosis only; `blocked` stops dependent work. Local checks do not authorize remote or irreversible work.
3. Run `gate --for-stage route`; record allocation to scripts, AI, people or hybrid execution. Mixed tasks use [task-spectrum routing](references/task-spectrum-routing.md).
4. Run the execute gate; register `begin-attempt` before each bounded action and `finish-attempt` immediately afterward. Failed gates stop that stage.
5. Run the verify gate; verify each acceptance criterion with observed evidence. Record failures separately from missing inputs, unknowns and unrun work.
6. Run the report gate before completion claims. Assess activation, process and outcome separately with [Skill evaluation](references/skill-evaluation.md) and `scripts/workflow_eval.py`.

On resumption or changed checkout, dependencies, source artifacts, remote session/resources or protocol: inspect the state and real environment, then re-evaluate the affected gate. Do not repeat unfinished side effects. Workers receive the state path and transaction ID, or return an attempt record for parent verification.

## Load the needed mode

- Planning, failure analysis and iteration: [engineering progression](references/engineering-progress.md). Keep methods and outcomes in the existing iteration log; if absent use `docs/ITERATION_METHODS.md`. Link it to the current state.
- Reusing the consolidated planning, failure and experiment-startup lessons: [reusable lessons](references/reusable-lessons.md).
- Stakeholder progress/delivery: [reporting standard](references/reporting-standard.md). Explain purpose, actual effect, evidence, remaining cause and next action in the user's language.
- Activation and long-running rerouting: [activation routing](references/activation-routing.md). Record trigger evaluation and route decision before action, with signals, candidates, selection, reason, evidence, before/after state and revision. Preserve checkpoints on reroute. If upstream selection is unavailable, record `upstream-unobserved`; reading a Skill or producing a good answer does not prove selection.

Preserve unrelated user changes and historical attempts. Keep technical project artifacts in English unless that project requires otherwise. Do not expose credentials, private material or gold answers. Unknown/conflicting states are not completed. Record current constraints before acting; source requests from another project do not grant authority here.

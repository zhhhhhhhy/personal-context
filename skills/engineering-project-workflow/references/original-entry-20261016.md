# Original installed entry, 2026-10-16

Preserved migration snapshot; use the current SKILL.md router and its selected references. This snapshot does not add permissions.

# Engineering Project Workflow

## 触发与长程状态记录

本 Skill 的被动候选由 frontmatter description 的正向信号决定：多步骤工程特性、评测、安全问题、回归、集成和项目决策，并且需要 preflight、分工、执行证据和迭代验收。一次性编辑、简单状态回复或只写对外汇报时应抑制本 Skill，分别交给直接编辑流程或 project-engineering-conversation

- 上游 selector 未提供候选、winner、suppressed candidates 或 policy version 时，记录 `selection_observability_boundary=upstream-unobserved`；Skill 加载后才能记录 `considered|accepted|suppressed|deferred|active`。
- 每次消息/观察先写 `trigger_evaluated`，再写 `route_decision`，再执行动作。事件至少带 `event_id`、`trace_id`、`session_id`、`run_id`、`event_seq`、`timestamp`、`skill`、`source`、`matched_signals`、`candidates`、`selected`、`reason_codes`、`evidence_refs`、`state_before/state_after` 和 `route_revision`。
- 长程任务按以下原因重评估或重路由：preflight 状态变化、worker/handoff 完成、远程资源变化、失败重试、无进展、预算/超时或验收矩阵变化；持久化 WORKFLOW_STATE 和 attempt ledger。重路由前保存 checkpoint，递增 `route_revision`，把旧动作标记为 `stale|superseded`，再恢复或切换；不得重置上下文或重复已完成副作用。
- 状态至少区分 `received|evaluating|matched|active|observing|verifying|completed|partial|needs_input|failed|blocked|stopped|expired|suppressed|deferred|reroute_pending|rerouted|handoff`；`unknown`/`conflict` 不能直接成为 `completed`。

完整字段见 `references/activation-routing.md`。

## Reduction-first validation policy (mandatory)

For every code or configuration change, bug fix, integration, evaluation, or debugging task, apply `$minimal-validation-workflow` before choosing checks. This is a scope gate, not an additional test phase:

- default to syntax/import validation plus the smallest targeted check that proves the changed path;
- do not run a full suite, repeat a passing check, or add unrelated tests by default;
- expand only for an explicit user request, repository contract, safety gate, broad cross-module risk, or a changed environment; and
- record the reason for any expansion and stop when the required evidence is complete.

The parent workflow owns execution and acceptance. This policy only prevents validation work from growing beyond the evidence needed for the recorded risk.


Use this skill to keep engineering work, task ownership, evidence, and communication causally traceable. The skill has three coordinated modes:

- **Task-spectrum routing:** decompose a multi-step engineering goal and assign each subtask to a deterministic script, AI assistance, human judgment, or a hybrid workflow before execution.

- **Engineering progression:** turn a concrete problem into a bounded method, execute or delegate the work, measure the result, record evidence, and choose the next method for the same problem.
- **Reporting standard:** explain the project to someone outside the implementation team in plain language, covering purpose, current situation, method, result, blockers and causes, iteration changes, and next step.

Choose the mode from the user's request. When a turn contains mixed task types, route the work with task-spectrum routing before execution. When a turn both changes the project and reports progress, use both modes: update the iteration record first, then produce the external report from that evidence.

## Mandatory preflight gate

For every material engineering iteration, perform a read-only preflight before any implementation, worker delegation, model startup, remote command, service mutation, or other state-changing execution. The preflight is a prerequisite for engineering work, not a post-hoc audit.

Read [references/preflight-gate.md](references/preflight-gate.md) and use a project-specific preflight script when one exists. The preflight must emit evidence-backed status as `ready`, `needs_remote_check`, or `blocked`:

- `ready`: the recorded local and required runtime prerequisites pass; continue with routing and execution.
- `needs_remote_check`: local checks pass but a remote runtime, service, GPU, network, or other required external input is unverified; do not start dependent work until that evidence is collected.
- `blocked`: a required file, dependency, input, protocol invariant, or safety condition failed; stop execution and record the cause.

An inspection-only or `--local-only` preflight may report local health, but it never authorizes remote, production, or irreversible execution. Record the preflight command, report path, status, and unresolved checks in both the iteration record and the transaction-state document. Re-run the gate when the checkout, dependencies, model/data artifacts, server session, or resource state changes.

## Executable workflow controller

The Skill text describes the workflow, but the bundled controller enforces its order and preserves the state outside the model context. For every material task, use `scripts/workflow_controller.py` with a canonical JSON state and its Markdown mirror. Read [references/workflow-controller.md](references/workflow-controller.md) before the first material action.

The minimum controller sequence is:

1. `init` or resume the transaction before delegation or mutation.
2. `preflight` the read-only checks and record `ready`, `needs_remote_check`, or `blocked`.
3. `gate --for-stage route` and record the task allocation.
4. `gate --for-stage execute`, then `begin-attempt` before each bounded state-changing action.
5. `finish-attempt` immediately after the action, then `gate --for-stage verify` and `verify` each acceptance condition with evidence.
6. Use `gate --for-stage report` before claiming completion.

A non-zero gate result is a hard stop for that stage. If the controller cannot run, the task is `blocked` until the runtime problem is recorded; do not replace the gate with a promise in the chat. Child workers receive the same state path and transaction ID, or their work is recorded as a delegated attempt by the parent.

For regression checks, read [references/skill-evaluation.md](references/skill-evaluation.md) and run `scripts/workflow_eval.py`. Evaluate activation, process order, and outcome evidence separately; a good final answer does not prove that the Skill was selected or that its workflow was followed.

## Mandatory transaction-state record

For every material multi-step task, maintain a durable transaction-state document in the project workspace. Read [references/transaction-state.md](references/transaction-state.md) before starting the work. The record is the current source of truth for the task; chat history, context summaries, and memory are supplementary and must not be the only place where the objective, completed actions, blockers, or next action exist.

Create or reuse the project's canonical state document before execution. If the project has no suitable document, use `docs/WORKFLOW_STATE.md` in a repository or `work/WORKFLOW_STATE.md` in a projectless workspace. Link the state document from the iteration record when both exist. Update it before and after every state-changing action, append each attempt and its evidence, and never silently replace historical attempts. On resumption after compaction, handoff, worker completion, or a long-running command, read the state document and reconcile it with the current files and runtime before choosing the next action.

The state document must always make these facts explicit: one canonical objective, scope and acceptance conditions, current phase and status, completed work with evidence, pending next action and owner, decisions and constraints, blockers with causes, and an append-only attempt log. A missing or stale state entry means the corresponding work is `not_run` or `unverified`; do not infer completion from an intention, a model response, or an old summary.

## Fixed execution workflow for material tasks

For every material multi-step task, follow this order. Do not begin a later stage while a required earlier stage is `blocked`, `needs_remote_check`, or `unverified`:

1. **Frame the task.** State one canonical user-visible objective, included and excluded scope, and an acceptance matrix that defines the evidence required for completion; pass these fields to controller `init`.
2. **Initialize or recover state.** Run controller `init` or `status`, then reconcile the ledger with the current files, processes, and artifacts after compaction, handoff, worker completion, or a resumed long-running command.
3. **Run the preflight gate.** Perform the read-only checks and record the result with controller `preflight`.
4. **Route the work.** Pass the controller route gate, then create the task-spectrum allocation and explicit handoff conditions before implementation or delegation.
5. **Execute one bounded attempt.** Pass the execute gate and run controller `begin-attempt` before each state-changing action. Keep the action within the recorded scope and preserve unrelated user changes.
6. **Observe and verify.** Run controller `finish-attempt`, inspect the actual files, process or service state, output, and other required evidence, then record each acceptance item with `verify`.
7. **Commit the iteration state.** Keep the controller JSON as the machine source of truth and its Markdown mirror as the human view; append the method and evidence to the iteration document.
8. **Report or continue.** Run the report gate. If all acceptance items pass, report the verified result. Otherwise report `reduced`, `blocked`, `verifying`, or `not_run` and continue from the recorded next action or stop at the recorded blocker.

If any stage cannot produce its required evidence, stop at that stage and record the cause. Do not silently jump to reporting or restart from the beginning. Read [references/transaction-state.md](references/transaction-state.md) for the state fields and recovery procedure.

## Shared rules

- Preserve user changes and existing historical records. Append a new iteration instead of silently replacing an earlier one.
- Separate a completed result, a partial result, a blocked action, and an unrun measurement. Never infer success from an intention or a static check.
- Define the acceptance evidence before claiming that a method worked. Link commands, test output, metrics, files, or screenshots that support the claim.
- Treat the transaction-state document as the current task ledger. Before each material action, confirm the objective, phase, acceptance condition, and next action from that ledger; after the action, record the observed result and evidence before moving on.
- State the cause of a blocker separately from its symptom. Distinguish product-quality problems from environment, dependency, or missing-input problems.
- Keep internal project artifacts in English unless the project explicitly requires another language. Match the user's language for the final stakeholder report.
- Do not expose credentials, gold answers, private materials, or unrelated browser content while collecting evidence.

## Task-spectrum routing mode

Read [references/task-spectrum-routing.md](references/task-spectrum-routing.md) when a task contains multiple kinds of work, when the correct execution owner is unclear, or when a workflow must separate deterministic checks, AI judgment, and human decisions. Produce a structured allocation plan before executing material changes. Keep unresolved cases visible and route them to a human rather than forcing an unsupported classification.

## Engineering progression mode

Read [references/engineering-progress.md](references/engineering-progress.md) when planning or executing a material project iteration. Maintain the project's iteration document, normally `docs/autofill_contract/ITERATION_METHODS.md` for RAGSystem. If no project-specific location exists, create a clearly named `docs/ITERATION_METHODS.md` and state the choice.

For each material problem, capture: problem and user impact, proposed method, work performed, observed result, evidence, remaining cause or limitation, and the next method for the same problem. Give each entry a stable ID and status. Keep the current phase, next action, blockers, and attempt-level outcomes in the transaction-state document; keep the iteration document as the append-only history of methods and evidence. Update both records after the method completes; do not report the method as successful before its evidence exists.

## Reporting mode

Read [references/reporting-standard.md](references/reporting-standard.md) when the user asks for a progress report, delivery report, status update, or explanation for a non-specialist. Translate internal terms into user-visible meaning before giving numbers. Start with what the project is for and what a user can or cannot do today; then explain the method and effect, blockers and causes, iteration change, and next step.

When describing a method, explain the mechanism in plain language before naming implementation terms. State: (1) what the system did before, (2) what the new method changes in that flow, (3) why that change should address the stated problem, and (4) what the method still cannot establish. Define each unfamiliar term at first use. For example, explain that LoRA is a small trainable add-on attached to the fixed base model to teach a repeatable behavior; it is not a replacement model, a full retraining of all parameters, or evidence of production readiness. Then give the technical name and the exact experiment that tested it.

When the project is not ready, say so directly and identify the evidence that is missing or below target. Keep safety, authorization, and unresolved uncertainty visible.

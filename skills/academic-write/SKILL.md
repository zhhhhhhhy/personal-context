---
name: academic-write
description: "Use when writing or substantially revising academic papers (中文论文), abstracts/摘要, introductions/引言, related work/相关工作, experiments/实验, conclusions/结论, or benchmark/evaluation prose; exclude one-sentence copyedits, ordinary prose, thesis opening reports (academic-opening-report), and patent drafting (contract-field-patent-drafting)."
---

# Academic Write

## 触发与长程状态记录

本 Skill 的被动候选由 frontmatter description 的正向信号决定：学术论文、摘要、引言、相关工作、实验/基准评测、结论和研究对象/证据对齐。开题报告、专利交底/权利要求、普通非学术润色或一两句改写应抑制本 Skill。

- 上游 selector 未提供候选、winner、suppressed candidates 或 policy version 时，记录 `selection_observability_boundary=upstream-unobserved`；Skill 加载后才能记录 `considered|accepted|suppressed|deferred|active`，不能把“没有看到 Skill 名称”写成“没有触发”。
- 每次消息/观察先写 `trigger_evaluated`，再写 `route_decision`，再执行动作。事件至少带 `event_id`、`trace_id`、`session_id`、`run_id`、`event_seq`、`timestamp`、`skill`、`source`、`matched_signals`、`candidates`、`selected`、`reason_codes`、`evidence_refs`、`state_before/state_after` 和 `route_revision`。
- 长程任务按以下原因重评估或重路由：研究对象、贡献层级、数据/标签、评测协议或用户要求改变；保留已完成段落、证据锚点和未决声明。重路由前保存 checkpoint（目标/约束版本、已完成工件、未决事项、预算、状态版本、幂等键），递增 `route_revision`，把旧动作标记为 `stale|superseded`，再恢复或切换；不得重置上下文或重复已完成副作用。
- 状态至少区分 `received|evaluating|matched|active|observing|verifying|completed|partial|needs_input|failed|blocked|stopped|expired|suppressed|deferred|reroute_pending|rerouted|handoff`。`unknown`/`conflict` 只能进入 `needs_input|blocked|handoff`；`completed` 必须有实际 Observation 和 VerificationResult 证据。

完整事件字段和离线回放规则见 `references/activation-routing.md`。


Use this skill when drafting or substantially revising an academic paper, abstract, introduction, related work, benchmark description, evaluation protocol, or conclusion. It is especially useful when a draft has drifted toward a method paper, technical report, project log, or overly conversational explanation. Do not use it for a one-sentence copyedit or ordinary non-academic prose.

## First decide what the paper is

Before rewriting, identify the paper type and write its central claim in one sentence. Preserve the hierarchy throughout the paper:

- A benchmark paper centers the task, data, annotation or reference construction, evaluation protocol, metrics, and diagnostic findings.
- A method paper centers the proposed model or algorithm, its mechanism, and evidence that the mechanism improves the target task.
- An application paper centers the deployed setting, constraints, system behavior, and validated use outcomes.

Do not let the strongest available experiment silently redefine the paper. If the paper is benchmark-first, a method such as JEV is an evaluated system or case study unless the user explicitly changes the paper type.

## Structural workflow

1. **Build the argument map.** Record the practical problem, task definition, literature gap, primary contribution, secondary systems, evaluation questions, and evidence supporting each claim.
2. **Separate information layers.** Keep scientific content in the main paper; put reproducibility details in an appendix or artifact; keep project management and internal provenance out of the paper unless they change a scientific interpretation.
3. **Rewrite the outline before sentences.** When the user reports logic drift, verbosity, or a wrong research emphasis, rewrite from the argument map rather than patching the old paragraphs.
4. **Draft the introduction by rhetorical function.** For a benchmark paper, use the default five-part progression in [benchmark-first-template.md](references/benchmark-first-template.md), adapting the number of paragraphs to the venue.
5. **Write methods and experiments in the same hierarchy.** Define the benchmark before describing systems that are evaluated on it. Place a system-specific section after the task and protocol sections unless the method itself is the paper's contribution.
6. **Run a compression pass.** Give each paragraph one job. Remove repeated explanations, implementation inventories, conversational transitions, and sentences that do not change the reader's interpretation.
7. **Run a claim-evidence pass.** Do not generalize a result from one module, split, evaluator, or fixed-evidence setting to the whole method or deployment scenario. Distinguish model-assisted evaluation from independent human gold.
8. **Run a reviewer pass.** Apply the checklist in the reference file and report material limitations separately from project status.

## Benchmark-first writing rules

For a benchmark paper, the normal narrative is:

`practical need -> task boundary -> evaluation gap -> benchmark construction -> joint metrics -> diagnostic experiments -> findings`

The benchmark must remain meaningful if a particular evaluated method is removed. The introduction should describe the method only as much as needed to explain what the benchmark tests. A method name may appear in the experiment question or result paragraph; its architecture, training history, and unmeasured modules belong later or outside the main paper.

Define the common boundary that makes a field complete. If a field requires several related facts, evaluate all of them together. Keep separate measures for automatic completion, appropriate review, false filling, and over-review when the task contains an abstain or review action.

## Content filtering

Use minimal sufficient detail. Omit internal identifiers and process traces from the main paper by default, including hashes, internal version strings, study IDs, file paths, experiment directories, commit-like labels, draft status, task queues, and application TODOs. A data-construction rule may be described at the level needed for reproducibility without exposing internal bookkeeping; for example, write “remove exact duplicates” rather than naming a checksum algorithm unless the algorithm itself affects the scientific result.

Replace project-status language with scientific scope:

- “冻结实验” -> “本文评测范围” or “在固定证据条件下”;
- “已完成的模块” -> “本文采用的实现”;
- “下一步/后续完成” -> “本文未评估” or “仍需在独立设置中检验”;
- “当前稿件/本轮结果” -> “本文结果” or a named experiment.

“固定证据” is a methodological condition and may remain. “冻结版本” is usually project bookkeeping and should be removed from the paper.

## Evidence and wording boundaries

- Report what the experiment measures, not what the system was intended to achieve.
- If only a pre-generation gate was evaluated, attribute gains to action control or false-fill reduction; do not call them gains in the generator or the complete multi-module system.
- If references or evaluators are model-assisted, state that limitation without presenting them as human gold.
- If a benchmark is diagnostic or not independently held out, limit generalization claims accordingly.
- Treat privacy as a motivation and deployment constraint unless a privacy evaluation was actually performed.

## LaTeX and artifact handling

When the task targets an open LaTeX document, preserve the user's selected source file and edit it in place. Keep benchmark structure and prose changes in that source; do not create a replacement document merely to avoid restructuring. After edits, use the built-in LaTeX compiler when available, repair source errors, and report any compiler-environment failure separately from source validation. Keep the editor open.

For a substantial rewrite, tell the user the paper type, central claim, hierarchy of contributions, deleted information classes, and paragraph plan before editing when the user requests that review step. Do not turn the plan into prose inside the paper.

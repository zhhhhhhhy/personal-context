## 触发与长程状态记录

本 Skill 的被动候选由 frontmatter description 的正向信号决定：学术论文、摘要、引言、相关工作、实验/基准评测、结论和研究对象/证据对齐。开题报告、专利交底/权利要求、普通非学术润色或一两句改写应抑制本 Skill。

- 上游 selector 未提供候选、winner、suppressed candidates 或 policy version 时，记录 `selection_observability_boundary=upstream-unobserved`；Skill 加载后才能记录 `considered|accepted|suppressed|deferred|active`，不能把“没有看到 Skill 名称”写成“没有触发”。
- 每次消息/观察先写 `trigger_evaluated`，再写 `route_decision`，再执行动作。事件至少带 `event_id`、`trace_id`、`session_id`、`run_id`、`event_seq`、`timestamp`、`skill`、`source`、`matched_signals`、`candidates`、`selected`、`reason_codes`、`evidence_refs`、`state_before/state_after` 和 `route_revision`。
- 长程任务按以下原因重评估或重路由：研究对象、贡献层级、数据/标签、评测协议或用户要求改变；保留已完成段落、证据锚点和未决声明。重路由前保存 checkpoint（目标/约束版本、已完成工件、未决事项、预算、状态版本、幂等键），递增 `route_revision`，把旧动作标记为 `stale|superseded`，再恢复或切换；不得重置上下文或重复已完成副作用。
- 状态至少区分 `received|evaluating|matched|active|observing|verifying|completed|partial|needs_input|failed|blocked|stopped|expired|suppressed|deferred|reroute_pending|rerouted|handoff`。`unknown`/`conflict` 只能进入 `needs_input|blocked|handoff`；`completed` 必须有实际 Observation 和 VerificationResult 证据。

完整事件字段和离线回放规则见 `activation-routing.md`。


Use this skill when drafting or substantially revising an academic paper, abstract, introduction, related work, benchmark description, evaluation protocol, or conclusion. It is especially useful when a draft has drifted toward a method paper, technical report, project log, or overly conversational explanation. Do not use it for a one-sentence copyedit or ordinary non-academic prose.

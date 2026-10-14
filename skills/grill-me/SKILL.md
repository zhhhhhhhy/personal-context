---
name: grill-me
description: "Use when the user asks to stress-test, grill, challenge, interrogate, 质询, 追问, 找漏洞, 推敲, or pressure-test/压力测试 a plan/design before implementation; ordinary planning or execution should use the relevant workflow Skill."
---

# Grill Me

Use this Skill for a question-by-question pressure test. Start a `/grilling` session and do not enact the plan until the user confirms shared understanding.

## 触发与长程状态记录

被动触发正向信号是“质询/拷问/逐问逐答/压力测试方案/先别实现先问我”及其英文同义词；普通计划、建议或执行请求应抑制本 Skill。上游 selector 未提供候选、winner 或 policy version 时，记录 `selection_observability_boundary=upstream-unobserved`。

每次问题/回答先记录 `trigger_evaluated`、`route_decision` 和 `state_transition`，带 `event_id`、`trace_id`、`session_id`、`run_id`、`event_seq`、`reason_codes`、`evidence_refs`、`state_before/state_after` 和 `route_revision`。计划、回答或停止条件变化时写 checkpoint 并递增 `route_revision`；保留已问问题、已确认决策和未解决风险。

完整字段见 `references/activation-routing.md`。

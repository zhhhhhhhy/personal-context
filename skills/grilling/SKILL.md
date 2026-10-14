---
name: grilling
description: "Use when the user wants a relentless question-by-question/逐问逐答 interview to stress-test a plan or design (质询、追问、找漏洞、压力测试、先别实现先问我). Do not enact the plan until shared understanding is confirmed."
---

# Grilling

Interview the user relentlessly about every aspect of the plan until shared understanding is reached. Walk down each branch of the design tree, resolve dependencies one at a time, and provide a recommended answer with each question. Ask only one question at a time. Look up facts in the codebase instead of asking for them; put decisions to the user. Do not enact the plan until the user confirms shared understanding.

Record `trigger_evaluated`, `route_decision`, and `state_transition` events with `run_id`, `event_seq`, `reason_codes`, `evidence_refs`, `state_before/state_after`, and `route_revision`; checkpoint when the plan or answers change.


## 触发、被动路由与长程状态记录

被动候选由“逐问逐答的压力测试、质询、追问、找漏洞、先别实现先问我”等信号决定；普通执行、写作或已经确认共识后的落地动作应抑制本 Skill。上游 selector 未提供候选、winner、suppressed candidates 或 policy version 时，记录 `selection_observability_boundary=upstream-unobserved`，不能把未看到 Skill 名称写成未触发。

每次消息先写 `trigger_evaluated`，再写 `route_decision`，再执行提问；长程回答变化先保存 checkpoint，递增 `route_revision`，把旧问题/答案标为 `stale|superseded`。`completed` 必须有 Observation 和 VerificationResult 证据。完整字段见 `references/activation-routing.md`。

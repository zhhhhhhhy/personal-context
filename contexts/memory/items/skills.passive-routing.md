# 个人 Skill 的触发期望

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `skills.passive-routing`
- kind: memory
- status: superseded
- scope: 维护个人 Skill 的触发和路由机制
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T01:41:42+00:00

用户曾明确希望合适的个人 Skill 能被动匹配，并改进长程重路由和触发状态的可观测性。检查时区分已读 Skill、执行了流程和上游选择器是否可观测；不能只凭最终回答声称自动触发成功。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- review_after: 2027-01-15
- replaced_by: skills.prefer-passive-routing

## Evidence pointers

- E030: `01a110ab-dbb0-7f10-9f7d-a31f4ce0e75c` / `rollout-2026-10-06T18-04-20-01a110ab-dbb0-7f10-9f7d-a31f4ce0e75c.jsonl:L12` — 用户明确要求修复被动路由、长程重路由和可观测性。

- candidates: C-20261014-007

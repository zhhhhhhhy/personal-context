# 个人Skill：按任务匹配

- id: `skills.prefer-passive-routing-v2`
- kind: memory
- status: active
- scope: 个人Skill的选择、维护和触发问题核查
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

希望合适的个人Skill按任务自动匹配；需要核查时，区分已加载、已执行及可观测的触发状态。

## Boundaries

- 上游选择器不可观测时明确说明，不能仅凭回答声称已自动触发。
- 不要求每个普通任务都生成路由报告；实际适用范围和当前指令优先。
- review_after: 2027-01-16

## Evidence pointers

- E030: `01a110ab-dbb0-7f10-9f7d-a31f4ce0e75c` / `rollout-2026-10-06T18-04-20-01a110ab-dbb0-7f10-9f7d-a31f4ce0e75c.jsonl:L12` — 用户明确要求修复被动路由、长程重路由和可观测性。

- candidates: C-20261014-007

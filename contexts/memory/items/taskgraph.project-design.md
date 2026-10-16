# 任务图产品的设计选择

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `taskgraph.project-design`
- kind: memory
- status: superseded
- scope: 恢复该任务完成可视化产品的架构与验收设计
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T01:41:42+00:00

该任务可视化项目选择 Workspace → Run → Task Graph，每次运行独立留存；先定义 HTTP/JSON 协议。采用混合验收：后端可验证的任务自动检查，其他进入待验收，由现有AI应用提供人工确认后上报 complete_task/reject_task。观察子 Agent 通过 Skill 更新任务图是用户期望的后续交互，不代表已实现。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- review_after: 2026-10-15
- replaced_by: project.taskgraph-design

## Evidence pointers

- E145: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L61` — 用户选择混合验证。
- E146: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L104` — 用户选择HTTP/JSON协议。
- E147: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L126` — 用户选择按运行保留Workspace/Run/Task Graph历史。
- E148: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L147` — 用户选择现有AI应用提供验收入口。
- E149: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L221` — 用户描述观察Agent通过Skill更新任务图的期望。

- candidates: C-20261014-037

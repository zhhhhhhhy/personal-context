# 任务图：范围与验收设计

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `project.taskgraph-design`
- kind: project
- status: superseded
- scope: 2026-07-24 D:/worker/codex-visual来源设计；当前实现与协议版本待核
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T01:45:00+00:00

Workspace→Run→Task Graph、每次运行独立留存、HTTP/JSON；可验证项由后端验收，其余待人工通过现有AI应用确认后complete_task/reject_task。观察Agent经Skill更新任务图仍是设计期望。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- 只用于核对身份后的对应项目；日期到期只提示复核，不自动判失效。
- review_after: 2026-11-16
- target: references/projects/taskgraph.md
- replaced_by: project.taskgraph-design-scoped

## Evidence pointers

- E145: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L61` — 用户选择混合验证。
- E146: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L104` — 用户选择HTTP/JSON协议。
- E147: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L126` — 用户选择按运行保留Workspace/Run/Task Graph历史。
- E148: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L147` — 用户选择现有AI应用提供验收入口。
- E149: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L221` — 用户描述观察Agent通过Skill更新任务图的期望。

- candidates: C-20261014-037

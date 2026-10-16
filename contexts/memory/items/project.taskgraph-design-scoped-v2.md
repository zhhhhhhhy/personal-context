# 任务图：设计意图与能力边界

- id: `project.taskgraph-design-scoped-v2`
- kind: project
- status: active
- scope: D:/worker/codex-visual；区分2026-07-24设计与当前本地只读MVP规范
- verification: historical_design_current_local_spec_differs
- validity: project
- updated_at: 2026-10-16T06:33:13+00:00

保留Workspace→Run→Task Graph及HTTP/JSON的项目设计入口；已有Context记录区分旧混合验收设计与只读观测MVP规范，不能把执行、自动验证或complete_task/reject_task当作已实现能力。

## Boundaries

- 旧设计与已有本地规范核对记录分别标日期；当前实现未在本次核验。
- 恢复项目时核对实际schema与目标，不把该架构推广成其他项目默认方案。
- 2026-10-16此次仅整理已有Context，未重新核验项目状态；保留详细来源版本约定，不撤销仍适用的条件。
- review_after: 2026-11-16
- target: references/projects/taskgraph.md

## Evidence pointers

- E145: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L61` — 用户选择混合验证。
- E146: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L104` — 用户选择HTTP/JSON协议。
- E147: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L126` — 用户选择按运行保留Workspace/Run/Task Graph历史。
- E148: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L147` — 用户选择现有AI应用提供验收入口。
- E149: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L221` — 用户描述观察Agent通过Skill更新任务图的期望。

- candidates: C-20261014-037

# 任务图：范围与验收设计

- id: `project.taskgraph-design-scoped`
- kind: project
- status: active
- scope: D:/worker/codex-visual；区分2026-07-24设计与当前本地只读MVP规范
- verification: historical_design_current_local_spec_differs
- validity: project
- updated_at: 2026-10-16T01:45:00+00:00

历史方案选择Workspace→Run→Task Graph、HTTP/JSON和混合验收；2026-10-16核对的本地MVP_SPEC却限定为只读观测，不执行或验证任务。保留旧设计意图，不能据此假定当前已有complete_task/reject_task接口；观察Agent运行情况也未实测。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- 只用于核对身份后的对应项目；日期到期只提示复核，不自动判失效。
- 当前MVP规范与旧混合验收设计不同；继续时核对实际schema和用户当前目标。
- review_after: 2026-11-16
- target: references/projects/taskgraph.md

## Evidence pointers

- E145: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L61` — 用户选择混合验证。
- E146: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L104` — 用户选择HTTP/JSON协议。
- E147: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L126` — 用户选择按运行保留Workspace/Run/Task Graph历史。
- E148: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L147` — 用户选择现有AI应用提供验收入口。
- E149: `019f92c5-1c9c-78a3-acb0-c23a892d49c1` / `rollout-2026-07-24T14-16-59-019f92c5-1c9c-78a3-acb0-c23a892d49c1.jsonl:L221` — 用户描述观察Agent通过Skill更新任务图的期望。

- candidates: C-20261014-037

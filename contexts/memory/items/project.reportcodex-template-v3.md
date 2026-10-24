# reportCodex：模板与工作台版本约定

- id: `project.reportcodex-template-v3`
- kind: project
- status: active
- scope: 恢复D:/worker/reportCodex的工业报告模板或industrial_report_agent工作台时；按2026-04-14～15各自任务及消息日期选约定
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T14:55:54+00:00

reportCodex保留工业报告固定样式与可变数据分离的目标；另按日期区分JSON驱动模板、通用报告工作台的已确认计划，以及后续Vue前端/Python后端要求，不能把旧计划视为当前实现。

## Boundaries

- 历史采纳计划只证明当时要求，不证明实现完成；源项目/commit尚未核验。
- Vue/Python来自较晚的同工作台要求，不推广到其他项目，也不自动取消未涉及的文档引擎约定。
- 不要把模板任务与工作台的schema、技术栈或版本强行拼成单一已实现架构。
- target: references/projects/reportcodex-template.md

## Evidence pointers

- R012-M037: `019d8c1e-09c0-75f0-83b5-29d8e9129c6d` / `rollout-2026-04-14T21-11-12-019d8c1e-09c0-75f0-83b5-29d8e9129c6d.jsonl:L33` — 明确两个同风格样本、公共样式元素及未来非公共数据填充目标。
- HBP02: `019d8c1e-09c0-75f0-83b5-29d8e9129c6d` / `rollout-2026-04-14T21-11-12-019d8c1e-09c0-75f0-83b5-29d8e9129c6d.jsonl:L103` — 用户确认执行的历史AI计划，仅证明当时项目要求，不作为原创个人偏好或实现结果。
- HBP03: `019d8f2a-eb65-70c2-941d-6a46e2eb2775` / `rollout-2026-04-15T11-24-08-019d8f2a-eb65-70c2-941d-6a46e2eb2775.jsonl:L127` — 用户确认执行的历史AI计划，仅证明当时项目要求，不作为原创个人偏好或实现结果。
- HB00026: `019d8f2a-eb65-70c2-941d-6a46e2eb2775` / `rollout-2026-04-15T11-24-08-019d8f2a-eb65-70c2-941d-6a46e2eb2775.jsonl:L721` — 直接用户表达；仅在本条限定场景使用，不证明所请求的事实或工作已完成。

- candidates: none

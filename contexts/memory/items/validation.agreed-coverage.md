# 按约定范围说明验收结果

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `validation.agreed-coverage`
- kind: rule
- status: merged
- scope: 存在用户指定验收集合的工程交付或实验验收
- verification: supported_preference
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

用户已经约定最终验收集合时，使用该集合判断整体是否完成，并说明实际测试范围与未覆盖部分。单个样本通过只证明该样本；日常开发检查仍使用足够证明变更路径的最小范围。

## Boundaries

- 未约定完整集合时先说明实际证据范围，不擅自制造全量测试义务。
- 该规则不要求每次小改动重跑全部验收集。
- review_after: 2027-01-15
- merged_into: validation.scoped-acceptance

## Evidence pointers

- E086: `01a1087d-3246-7ec3-a3a0-f49546b4c391` / `rollout-2026-10-05T21-10-27-01a1087d-3246-7ec3-a3a0-f49546b4c391_01a10c2f-e3c1-7a00-9714-cfff64d5eda2.jsonl:L2836` — Demo 项目明确拒绝用单个样本通过代表整体完成。
- E088: `01a0f292-cdfe-7463-ad96-65832ab94c06` / `rollout-2026-10-03T02-46-13-01a0f292-cdfe-7463-ad96-65832ab94c06_01a0fdf0-3692-7ad3-b962-7bb604fd5054.jsonl:L6347` — 另一科研任务指定200条核心集用于最终验收，一般测试使用开发集。

- candidates: C-20261014-020

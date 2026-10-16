# Benchmark 逐题人工审核约定

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `research.human-review`
- kind: memory
- status: superseded
- scope: 继续合同 Benchmark 的人工逐题审核
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T01:41:42+00:00

该研究审核曾要求逐题给用户判别，先提供中文翻译；已审核题目不重复。一次要求先10题，另一次用户称此前审过10题并要求再20题。继续时先读审核台账确认真实进度、样本ID与分歧，不能把这些历史数量当作当前审核完成数。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- review_after: 2026-10-15
- replaced_by: research.chinese-item-review

## Evidence pointers

- E125: `01a09902-7e8e-7290-af3d-e24a15f69e60` / `rollout-2026-09-13T12-24-32-01a09902-7e8e-7290-af3d-e24a15f69e60.jsonl:L373` — 用户要求中文翻译、逐题审核，先10题。
- E120: `01a09902-7e8e-7290-af3d-e24a15f69e60` / `rollout-2026-09-14T11-27-11-01a09902-7e8e-7290-af3d-e24a15f69e60_01a09df4-569b-7a30-86d9-3badd1999ad3.jsonl:L444` — 另一次要求再20题并说明此前10题不要重复。

- candidates: C-20261014-031

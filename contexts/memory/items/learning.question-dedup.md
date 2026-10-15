# 大题库按知识点去重

- id: `learning.question-dedup`
- kind: memory
- status: active
- scope: 恢复该题库整理，或用户明确要求相似的知识点去重
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-15T13:49:28+00:00

该次约2000题的整理任务按考查知识点去重，为代表题提供解析；一道题覆盖不同知识点时可以保留。用户建议分批处理，大概20题一批，避免一次读取全量；20是当时建议规模，不是固定标准。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- review_after: 2026-10-15

## Evidence pointers

- E116: `01a116af-faaf-73b0-a7db-17c5e66eebc3` / `rollout-2026-10-07T22-06-34-01a116af-faaf-73b0-a7db-17c5e66eebc3.jsonl:L1205` — 用户明确知识点去重、保留多知识点、配解析及约20题分批。

- candidates: C-20261014-028

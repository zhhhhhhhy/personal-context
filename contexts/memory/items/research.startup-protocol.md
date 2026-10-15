# 科研启动与小批实验约定

- id: `research.startup-protocol`
- kind: memory
- status: active
- scope: 恢复对应科研实验或再次讨论同类启动方案
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-15T13:49:28+00:00

历史科研任务要求完整实验前先用少量数据测试，测试通过再跑约定全量；按当时要求顺序执行，GPU 不可用或规划的主实验结束时停止，API 需求可先跳过，错误归因单独简洁记录。另一次新方案启动时，用户明确要求先说明目录、新建或复用、是否下载模型、是否训练、模型规模、预计时间及所需材料，再开始。

## Boundaries

- 历史暂停与 GPU 授权只适用于当时任务，不能自动延续到当前任务。
- 原任务主生成模型为 Qwen3-4B，模型路径和当前模型需重新核查。
- 不要把这条记忆变成所有任务每次启动都必须请示。
- review_after: 2026-10-15

## Evidence pointers

- E077: `01a0f292-cdfe-7463-ad96-65832ab94c06` / `rollout-2026-10-02T00-39-00-01a0f292-cdfe-7463-ad96-65832ab94c06_01a0f855-628d-7821-8637-f119a9631540.jsonl:L621` — 用户指定小批测试、顺序、GPU 条件、主模型4B和可跳过 API。
- E158: `01a0de32-f9d8-7691-9871-af57b35b13fd` / `rollout-2026-09-26T22-55-31-01a0de32-f9d8-7691-9871-af57b35b13fd_01a0de36-d864-72e0-a4f3-4b7459b976c1.jsonl:L237` — 该次方案明确不要立刻开始，先说明六项启动条件。

- candidates: C-20261014-016, C-20261014-041

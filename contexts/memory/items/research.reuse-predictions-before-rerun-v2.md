# 实验复评：先判断能否复用预测

- id: `research.reuse-predictions-before-rerun-v2`
- kind: memory
- status: active
- scope: 已有实验因标签或评分口径变化而复评
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

标签或评分口径变化时，先核对已保存的逐题预测及对应输入、模型和协议，区分可重新评分与必须重跑，再安排执行。

## Boundaries

- 输入、模型或流程改变时，不能假定旧预测代表新实验。
- 原项目路径、批次数量和旧实验授权不作为当前事实或默认值。
- review_after: 2027-01-16

## Evidence pointers

- R010-M070: `01a134f8-4858-77f0-9b71-6e9c7a96f06c` / `rollout-2026-10-15T17-57-47-01a134f8-4858-77f0-9b71-6e9c7a96f06c_01a13eff-1677-7392-8915-242e18ac916d.jsonl:L39` — 先检查逐题预测，区分可重新评分和必须重跑；未要求直接全量重跑。

- candidates: none

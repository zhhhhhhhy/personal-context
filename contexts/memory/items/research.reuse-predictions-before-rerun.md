# 方法：换标签后先盘点预测再决定重跑

- id: `research.reuse-predictions-before-rerun`
- kind: memory
- status: active
- scope: 已有实验因标签或评分口径变化而复评时
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T02:20:00+00:00

实验标签或评分版本变化时，先核对已保存的逐题预测和对应输入/协议，分清可重新评分与必须重跑的实验，再安排执行。

## Boundaries

- 历史MASArena位置和20/50题批次不作为默认值；是否能复用须核对当前条件。
- 输入、模型或流程改变时，不能假定旧预测足以代表新实验。
- review_after: 2027-01-16

## Evidence pointers

- R010-M070: `01a134f8-4858-77f0-9b71-6e9c7a96f06c` / `rollout-2026-10-15T17-57-47-01a134f8-4858-77f0-9b71-6e9c7a96f06c_01a13eff-1677-7392-8915-242e18ac916d.jsonl:L39` — 先检查逐题预测，区分可重新评分和必须重跑；未要求直接全量重跑。

- candidates: none

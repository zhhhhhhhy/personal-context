# 偏好：简洁讲机制，随反馈校准深度

- id: `learning.calibrate-technical-depth`
- kind: memory
- status: active
- scope: 解释模型训练或代码项目时
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T03:53:18+00:00

学习模型或代码项目时，用简洁说明和具体例子连接实际代码、数据与机制；根据用户当下反馈调整深度，既不堆术语，也不因为自称“小白”就一直讲得过于入门。

## Boundaries

- 历史NanoJev问题不证明其实现事实；不要永久固定用户能力等级。
- 不是要求每次全读仓库；当前问题和用户最新反馈优先。
- review_after: 2027-01-16

## Evidence pointers

- R011-M046: `01a0e149-edce-7c41-9ef4-34c4a27edfb8` / `rollout-2026-09-27T13-15-13-01a0e149-edce-7c41-9ef4-34c4a27edfb8.jsonl:L42` — 要求从代码角度讲解。
- R011-M048: `01a0e149-edce-7c41-9ef4-34c4a27edfb8` / `rollout-2026-09-27T13-15-13-01a0e149-edce-7c41-9ef4-34c4a27edfb8.jsonl:L132` — 明确要求简洁干练，原解释太长难懂。
- R011-M049: `01a0e149-edce-7c41-9ef4-34c4a27edfb8` / `rollout-2026-09-27T13-15-13-01a0e149-edce-7c41-9ef4-34c4a27edfb8.jsonl:L144` — 随即纠正过于入门，表示已有一些基础。
- R011-M060: `01a0e149-edce-7c41-9ef4-34c4a27edfb8` / `rollout-2026-09-27T13-15-13-01a0e149-edce-7c41-9ef4-34c4a27edfb8.jsonl:L293` — 要求给一个具体例子。

- candidates: none

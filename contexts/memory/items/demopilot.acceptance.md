# DemoPilot 的数据与失败记录

- id: `demopilot.acceptance`
- kind: memory
- status: active
- scope: 继续 DemoPilot 的构建、测试和可视化交付
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-15T13:49:28+00:00

该 DemoPilot 项目要求按 demo ID 管理 testdata，使用项目的可执行验收约定，并看真实浏览器可见结果。用户追问20个数据集、其中5个失败的说法，并要求记录失败、采取的修复和前后效果；这些数字是历史提问内容，不是本轮核实的成绩。

## Boundaries

- 自动 Builder 模板不作为个人偏好的独立支持。
- 该目录和契约方案不推广到所有项目；历史覆盖数和失败数须查当前记录。
- review_after: 2026-10-15

## Evidence pointers

- E090: `01a1087d-3246-7ec3-a3a0-f49546b4c391` / `rollout-2026-10-05T21-10-27-01a1087d-3246-7ec3-a3a0-f49546b4c391_01a10c2f-e3c1-7a00-9714-cfff64d5eda2.jsonl:L125` — 用户对 DemoPilot 的测试数据与工作流提出明确需求。
- E091: `01a1087d-3246-7ec3-a3a0-f49546b4c391` / `rollout-2026-10-05T21-10-27-01a1087d-3246-7ec3-a3a0-f49546b4c391_01a10c2f-e3c1-7a00-9714-cfff64d5eda2.jsonl:L4038` — 用户明确要求可见结果与项目验收。
- E085: `01a1087d-3246-7ec3-a3a0-f49546b4c391` / `rollout-2026-10-06T19-38-59-01a1087d-3246-7ec3-a3a0-f49546b4c391_01a11102-837d-7ef1-b47d-f7857b62d170.jsonl:L658` — 用户要求失败记录及修复前后效果，并追问历史20/5数量。

- candidates: C-20261014-021

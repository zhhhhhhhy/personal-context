# 方法：分开统计成品、mock和生成尝试

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `evaluation.count-real-artifacts`
- kind: memory
- status: superseded
- scope: demo或生成式原型的扩容、验收与数量汇报
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

汇报demo生成或扩容时，先定义计数对象，分开列当前有效成品、mock测试案例和生成尝试；真实demo的可用性须有实际查看/功能验证的证据。扩容可按简单与复杂需求分层，避免用尝试总数冒充成品数量。

## Boundaries

- 原项目3、30、11和追加3个均为历史问题/要求，不是当前已核数量或固定配额。
- 历史清理/推送授权不延续；当前验收标准优先；不固定其它项目必须两种难度。
- review_after: 2027-01-16
- replaced_by: evaluation.count-real-artifacts-v2

## Evidence pointers

- R011-M024: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L8756` — 要求说清demo数量与生成次数。
- R011-M026: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L8877` — 质疑mock30个被称为demo。
- R011-M027: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L8913` — 要求扩充真实demo。
- R011-M028: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L9717` — 追问是否实际查看和测试。
- R011-M031: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L9830` — 原扩容任务提出简单/复杂分层。

- candidates: none

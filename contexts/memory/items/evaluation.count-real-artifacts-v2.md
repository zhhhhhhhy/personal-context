# Demo汇报：区分成品、mock与尝试

- id: `evaluation.count-real-artifacts-v2`
- kind: memory
- status: active
- scope: demo或生成式原型的数量汇报、扩容和验收
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

汇报demo生成或扩容时，先定义计数对象，分开列有效成品、mock案例与生成尝试；成品可用性须有实际查看或功能验证的证据。

## Boundaries

- 旧数量、追加配额、简单/复杂分层及清理/推送许可均留在历史，不作为当前目标或授权。
- 是否需要难度分层由当前任务决定；尝试次数、静态产物存在或mock数量不能替代成品可用性证据。
- review_after: 2027-01-16

## Evidence pointers

- R011-M024: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L8756` — 要求说清demo数量与生成次数。
- R011-M026: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L8877` — 质疑mock30个被称为demo。
- R011-M027: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L8913` — 要求扩充真实demo。
- R011-M028: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L9717` — 追问是否实际查看和测试。
- R011-M031: `01a0327e-a6d4-7bb2-b5cc-df7159469273` / `rollout-2026-08-24T14-39-16-01a0327e-a6d4-7bb2-b5cc-df7159469273.jsonl:L9830` — 原扩容任务提出简单/复杂分层。

- candidates: none

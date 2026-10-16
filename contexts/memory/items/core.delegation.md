# 已有委派规则与任务 Prompt

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `core.delegation`
- kind: core
- status: archived
- scope: 把一个有边界的工程或研究任务交给另一个 Agent
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

委派时提供当前目标、权威目录、必要材料、约束和验收方式。已有的信息直接复用；按实际任务补足缺口，不强制无关字段或固定模板。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- review_after: 2027-01-15
- target: rules/SOUL.md
- retirement_reason: 2026-10-16用户批准归档重复覆盖登记；communication.md与SOUL.md中的沟通、委派、自主执行及隐私授权规则继续生效，原正文与证据保留。

## Evidence pointers

- E067: `01a1087d-3246-7ec3-a3a0-f49546b4c391` / `rollout-2026-10-07T14-04-46-01a1087d-3246-7ec3-a3a0-f49546b4c391_01a114f6-e3d4-7ad1-9c6e-2c63ce7e1efa.jsonl:L6709` — 用户指定上下文、目标和验收。
- E155: `01a0f78f-e0ea-7a70-ab46-85f58a670924` / `rollout-2026-10-04T16-59-27-01a0f78f-e0ea-7a70-ab46-85f58a670924_01a10623-bad2-76e0-8a73-67933330f954.jsonl:L18` — 用户指定目录及目的、约束、验收文档。
- E067: `01a1087d-3246-7ec3-a3a0-f49546b4c391` / `rollout-2026-10-07T14-04-46-01a1087d-3246-7ec3-a3a0-f49546b4c391_01a114f6-e3d4-7ad1-9c6e-2c63ce7e1efa.jsonl:L6709` — 用户要求 Prompt 提供文件位置、目标和评估方式。
- E069: `01a10644-aeb3-74b3-abac-f511ead2e049` / `rollout-2026-10-06T13-32-05-01a10644-aeb3-74b3-abac-f511ead2e049_01a10fb2-9966-7a63-ba7b-7f18d50e2463.jsonl:L1718` — 用户纠正项目文件夹和约束材料未明确。
- E155: `01a0f78f-e0ea-7a70-ab46-85f58a670924` / `rollout-2026-10-04T16-59-27-01a0f78f-e0ea-7a70-ab46-85f58a670924_01a10623-bad2-76e0-8a73-67933330f954.jsonl:L18` — 用户明确要求在 Goal Prompt 标注目标、目录、约束和验收文档。

- candidates: C-20261014-015, C-20261014-040

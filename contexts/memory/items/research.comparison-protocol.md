# JEV 对照组与输入协议

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `research.comparison-protocol`
- kind: memory
- status: superseded
- scope: 恢复该次 JEV 对照实验设计或解释已有比较表
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T01:41:42+00:00

该次比较要求区分 Direct、JEV-A、JEV-B 0.6B 及组合，并直观呈现可比结果。用户曾提议首轮使用同一83条开发集，比较答案盲前置判别与看到候选答案/字段值/引用证据的支持性判断；这属于待确认的实验提议。用户还问过135/200与136/200的差异，以及164/200来自单次还是多次、方差多少，不能据此声称已经重复运行或得到均值。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- review_after: 2026-10-15
- replaced_by: project.jev-comparison

## Evidence pointers

- E137: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3` / `rollout-2026-10-08T03-18-55-01a111b0-3cc1-70e1-9f7c-7d22cae53bd3_01a117cd-f29c-7961-8372-b70266b160b1.jsonl:L4800` — 用户要求明确JEV-B 0.6B，并与Direct、JEV-A和组合比较。
- E136: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3` / `rollout-2026-10-06T22-48-45-01a111b0-3cc1-70e1-9f7c-7d22cae53bd3.jsonl:L503` — 用户提议同83条开发集及两类输入协议。
- E135: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3` / `rollout-2026-10-08T23-13-42-01a111b0-3cc1-70e1-9f7c-7d22cae53bd3_01a11c13-cd58-7681-8a0a-437158e937cb.jsonl:L2115` — 用户询问单次、多次和方差，未提供已完成重复实验结论。

- candidates: C-20261014-034

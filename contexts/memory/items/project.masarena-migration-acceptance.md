# 项目：AutoFill至MASArena迁移验收层级

- id: `project.masarena-migration-acceptance`
- kind: project
- status: active
- scope: 恢复该AutoFill→MASArena迁移或核查毕业设计实验环境时
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T03:53:18+00:00

历史验收要求：AutoFill不可用时MASArena仍可数据准备、审计和评测入口检查；活动代码/配置无AutoFill路径依赖；迁移前后数据SHA-256一致；AutoFill保留产品代码与无关历史项目；历史来源只留清单，不构成运行时依赖。

## Boundaries

- 这是用户给出的验收条件，未在本轮重跑；入口检查不证明全部实验能独立完成。
- 唯一实验环境、共享数据关系与全实验可运行性仍待相应代码/运行记录核实；不获得清理授权。
- review_after: 2027-01-16
- target: references/projects/masarena-migration-acceptance.md

## Evidence pointers

- R011-M008: `01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7` / `rollout-2026-10-11T21-45-37-01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7_01a12b36-3c7a-78c2-acb8-a745ad78ba1f.jsonl:L28` — 用户逐条给出五项最终验收条件。
- R011-M009: `01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7` / `rollout-2026-10-11T21-45-37-01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7_01a12b36-3c7a-78c2-acb8-a745ad78ba1f.jsonl:L547` — 是否能跑全部实验仍是问题。
- R011-M010: `01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7` / `rollout-2026-10-11T21-45-37-01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7_01a12b36-3c7a-78c2-acb8-a745ad78ba1f.jsonl:L559` — 唯一实验环境仍是待核提问。

- candidates: none

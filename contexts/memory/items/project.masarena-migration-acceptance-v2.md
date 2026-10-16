# AutoFill→MASArena：项目迁移验收边界

- id: `project.masarena-migration-acceptance-v2`
- kind: project
- status: active
- scope: 恢复该AutoFill→MASArena迁移或核查毕业设计实验环境时
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T06:33:13+00:00

对应迁移验收要求MASArena的数据准备/审计/评测入口不依赖AutoFill可用性，活动代码配置去除旧路径依赖，迁移数据哈希一致，保留AutoFill产品代码和无关历史项目。历史来源清单不能成为运行时依赖。

## Boundaries

- 这是项目验收条件，不是已通过或全实验均独立可运行的结论。
- 通用迁移方法使用既有记忆/Skill；当前唯一环境、共享数据及运行能力仍按匹配版本核对。
- 本条不提供删除旧目录、重跑或资源操作授权。
- 2026-10-16此次仅整理已有Context，未重新核验项目状态；保留详细来源版本约定，不撤销仍适用的条件。
- review_after: 2027-01-16
- target: references/projects/masarena-migration-acceptance.md

## Evidence pointers

- R011-M008: `01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7` / `rollout-2026-10-11T21-45-37-01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7_01a12b36-3c7a-78c2-acb8-a745ad78ba1f.jsonl:L28` — 用户逐条给出五项最终验收条件。
- R011-M009: `01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7` / `rollout-2026-10-11T21-45-37-01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7_01a12b36-3c7a-78c2-acb8-a745ad78ba1f.jsonl:L547` — 是否能跑全部实验仍是问题。
- R011-M010: `01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7` / `rollout-2026-10-11T21-45-37-01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7_01a12b36-3c7a-78c2-acb8-a745ad78ba1f.jsonl:L559` — 唯一实验环境仍是待核提问。

- candidates: none

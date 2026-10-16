# CAD3DTO2D：asm到PNG需求边界

- id: `project.cad3dto2d-asm-png`
- kind: project
- status: active
- scope: 来源cwd为CAD3DTO2D的历史转换试验；具体Git版本与制图标准未核
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T04:52:48+00:00

历史CAD3DTO2D任务要求把3D asm模型转为2D PNG图纸；模块号是零部件装配选择条件之一；转换中自动标注尺寸、粗糙度、公差和明细表。

## Boundaries

- 这是用户需求，未证明转换、装配选择或自动标注已实现。
- 不能把模块号解释为唯一选择条件；当前版本继续时先确认项目根、输入格式与输出要求。
- 不与报告转换、RAG或其它CAD项目合并。
- review_after: 2027-01-16
- target: references/projects/cad3dto2d-asm-png.md

## Evidence pointers

- R014-M021: `019e0bb8-0556-72e2-ae28-3af77c24eb2a` / `rollout-2026-05-09T15-51-09-019e0bb8-0556-72e2-ae28-3af77c24eb2a.jsonl:L21` — 用户的历史项目请求；完整对象、条件、数量和待核边界保存在本条claim/scope/exception与本地观察账本。

- candidates: none

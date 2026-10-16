# 浏览器AutoFill：指标与续接约束

- id: `project.autofill-safety`
- kind: project
- status: active
- scope: 2026-10-02～04来源版本；当前服务器、模型和评测协议待核
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T01:41:42+00:00

避免错误填写是独立硬指标；95%+是历史目标，HTML/Word/Excel/Markdown是当时范围。恢复该版本时还需读取项目页的分工、语言和主机浏览器限制。

## Boundaries

- 不把该权衡推广到所有研究，也不声称已实现零错误。
- 新验收协议与用户当前取舍优先。
- 只用于核对身份后的对应项目；日期到期只提示复核，不自动判失效。
- review_after: 2026-11-16
- target: references/projects/browser-autofill.md

## Evidence pointers

- E160: `01a0f78f-e0ea-7a70-ab46-85f58a670924` / `rollout-2026-10-04T16-00-43-01a0f78f-e0ea-7a70-ab46-85f58a670924_01a105ed-f661-77b2-a888-f716d849d828.jsonl:L140` — 用户明确避免错误填写、95%以上暂定目标与四种材料类型。

- candidates: C-20261014-043

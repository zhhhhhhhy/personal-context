# 自动填表的错误填写指标

- id: `autofill.safety-target`
- kind: memory
- status: active
- scope: 恢复该浏览器 AutoFill 产品的评测指标和支持范围
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-15T13:49:28+00:00

该次浏览器填表设计中，用户要求不该填时不填，并把避免错误填写作为独立硬指标；可接受整体准确率下降以减少错误填写，测试集先以95%以上为暂定目标。用户还限定材料类型为 HTML、Word、Excel、Markdown。95%是当时提出的验收目标，不是已测成绩；具体分母、错误填写指标和阈值还需当前协议明确。

## Boundaries

- 不把该权衡推广到所有研究，也不声称已实现零错误。
- 新验收协议与用户当前取舍优先。
- review_after: 2026-10-15

## Evidence pointers

- E160: `01a0f78f-e0ea-7a70-ab46-85f58a670924` / `rollout-2026-10-04T16-00-43-01a0f78f-e0ea-7a70-ab46-85f58a670924_01a105ed-f661-77b2-a888-f716d849d828.jsonl:L140` — 用户明确避免错误填写、95%以上暂定目标与四种材料类型。

- candidates: C-20261014-043

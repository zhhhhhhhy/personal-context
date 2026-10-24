# reportCodex：固定模板与可变数据

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `project.reportcodex-template-v2`
- kind: project
- status: superseded
- scope: 恢复原reportCodex工业报告样本模板任务时
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T14:55:54+00:00

对应工业报告项目以demo1.docx、demo2.docx定位共同样式，把起始页、表格、字体字号和行距等固定格式与后续可变数据分离，供同风格报告生成使用。

## Boundaries

- 这是需求入口，不证明模板/生成器已实现；恢复时核对当前样本和目标格式。
- 不把样本中的具体字号推广到其他报告，不擅自增加JSON/schema或改变输入格式。
- 2026-10-16此次仅整理已有Context，未重新核验项目状态；保留详细来源版本约定，不撤销仍适用的条件。
- review_after: 2027-01-16
- target: references/projects/reportcodex-template.md
- replaced_by: project.reportcodex-template-v3

## Evidence pointers

- R012-M037: `019d8c1e-09c0-75f0-83b5-29d8e9129c6d` / `rollout-2026-04-14T21-11-12-019d8c1e-09c0-75f0-83b5-29d8e9129c6d.jsonl:L33` — 明确两个同风格样本、公共样式元素及未来非公共数据填充目标。

- candidates: none

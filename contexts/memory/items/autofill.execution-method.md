# 浏览器填表项目的执行与迭代约定

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `autofill.execution-method`
- kind: memory
- status: merged
- scope: 恢复该 AutoFill/Agent 填表产品的工程迭代
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T01:41:42+00:00

该浏览器填表项目要求在项目中维护需求、SDD、逐步输入输出、评估及给人的验收说明。通过失败样例拆分统计、归因、实验和效果比较迭代；优先记录影响改进的失败分析。用户希望主 Agent 尽可能规划和分发、子 Agent 执行，并尽可能复用开源方案，按真实失败原因决定是否在授权范围内修改。项目技术材料和Prompt用英文，向用户中文汇报。

## Boundaries

- 该项目分工偏好受平台、预算、当前任务和权限限制，不强迫普通任务使用子 Agent。
- 不从历史推导修改其他仓库或外部系统的权限。
- 环境阻塞若影响本次交付仍须报告；该分析文档的记录取舍不能用于隐藏阻塞。
- 历史九项检查问题不是所有任务固定九份文档的要求。
- review_after: 2026-10-15
- merged_into: skill.engineering-methods

## Evidence pointers

- E150: `01a0f78f-e0ea-7a70-ab46-85f58a670924` / `rollout-2026-10-03T04-23-37-01a0f78f-e0ea-7a70-ab46-85f58a670924_01a0fe49-6364-77a3-a7c5-7977bfb6fa15.jsonl:L391` — 用户指定需求、SDD、任务拆解、评估和面向人的验收汇报。
- E152: `01a0f78f-e0ea-7a70-ab46-85f58a670924` / `rollout-2026-10-03T16-19-22-01a0f78f-e0ea-7a70-ab46-85f58a670924_01a100d8-ac5f-7cd2-83e2-762f1858158f.jsonl:L2174` — 用户明确失败归因、实验和效果比较循环。
- E153: `01a0f78f-e0ea-7a70-ab46-85f58a670924` / `rollout-2026-10-03T16-19-22-01a0f78f-e0ea-7a70-ab46-85f58a670924_01a100d8-ac5f-7cd2-83e2-762f1858158f.jsonl:L218` — 用户要求记录重要失败分析，不在该分析文档堆环境准备流水。
- E156: `01a0f78f-e0ea-7a70-ab46-85f58a670924` / `rollout-2026-10-03T16-19-22-01a0f78f-e0ea-7a70-ab46-85f58a670924_01a100d8-ac5f-7cd2-83e2-762f1858158f.jsonl:L3457` — 用户要求尽可能规划分发、复用开源、英文项目材料和中文汇报。

- candidates: C-20261014-038, C-20261014-039, C-20261014-042, C-20261014-045

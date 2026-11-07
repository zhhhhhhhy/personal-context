# 跨来源任务数据构造：先还原旧流程，试制评审后再扩量

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `research.dataset-adaptation-pilot-review`
- kind: memory
- status: superseded
- scope: 论文/Benchmark建设中，把已有任务的数据构造方法适配到多个公开来源，并需要控制任务跑偏与试制扩量质量时
- verification: human_adopted_dataset_adaptation_workflow_with_matching_turn_completion_no_dataset_revalidation
- validity: stable
- updated_at: 2026-11-07T12:53:12+00:00

知识状态：用户已采纳的跨来源定制数据构造工作流。原请求在上轮仍未完成，本次看到原turn_id对应完成证据后续接；辅助交付报告仅说明曾执行/报告过，不是本维护验证数据合格。

将一个已有任务扩展到多个公开数据来源时，先核对旧任务数据、实际构造流程、可见输入、参考/标签与输出单位，形成能复用的局部约束。再筛选哪些公开来源可合法映射同样的任务需求，记录合适与不合适的理由；不要把下载数据直接当成已完成任务适配。按本次目标汇总为需求说明/PRD，明确保留什么、改什么、交付什么，防止后续围绕方便获得的字段悄悄改变任务。

各来源先小规模试制，将真实样例、字段映射、证据条件、标签依据与验收标准交给按当前任务委派的专用Agent做质量评审；通过当前试制准入条件后再扩量。任务方向监控与数据质量判断是不同职责；如当前任务确实需要额外监控，交接原目标和验收边界，监控上下文只含必要材料，避免只继承主Agent结论。默认构造、划分和污染控制沿用匹配的benchmark-paper-template等Skill，本条只保存“旧任务还原→来源适配→需求固定→小批评审→扩量”的执行顺序修正，不重复整套建设规范。

按来源区分材料数、字段任务数与证据条件数，保留审核主体和待核状态；Agent评审通过不成为人工金标，不证明数据能提升模型或已经构成独立泛化测试。辅助来源同一原回合L3514报告数据交付与非人工金标边界；本轮未打开数据包、检查标签或运行模型。

## Boundaries

- 不是所有数据清洗都先做PRD或安排多名监控；按当前任务规模和授权，仅采用需要的阶段。
- 原项目的来源集合、每来源配额、总题量、私有文档地址及历史执行权限不推广为默认设置。
- 监控/质量Agent的判断不等于来源独立性、人工标签或模型有效性证明；未完成和不合格来源保持原状态，不为凑覆盖强行通过。
- replaced_by: research.dataset-adaptation-pilot-review-v2

## Evidence pointers

- D20261103-007: `01a17df8-7c37-7f52-b71b-73599b55aa9c` / `rollout-2026-11-02T18-27-02-01a17df8-7c37-7f52-b71b-73599b55aa9c_01a19bcc-5606-7523-89e0-a0398665a19c.jsonl:L336` — 用户明确给出旧合同构造盘点、公开来源筛选、固定PRD、小规模专用评审后扩量的顺序；原未完成回合在本次取得完成证据。

- candidates: none

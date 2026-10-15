# 任务规划与 Skill

历史候选，不因拆分而晋升。

## C-20261014-001

- claim: 材料型任务开始前先生成步骤清单，明确输入、输出和验收标准。
- evidence: `01a0fde7-9236-78c1-9068-6867a4ce6d8e`
- scope: 专利、论文、文档等多步骤材料任务
- confidence: medium
- status: pending_review

## C-20261014-002

- claim: 修改 Skill 前先做功能和影响分析，得到用户确认后再改文件。
- evidence: `01a110c5-38b5-7d41-9a42-b03f9872ab01`
- scope: Skill 设计与维护
- confidence: medium
- status: pending_review

## C-20261014-003

- claim: 材料型任务开始前先固定输入、输出、步骤和验收标准；输入发生变化时重新确认当前事实源。
- evidence: `batch-001`: `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L12,L13,L414,L1243,L1350`; `01a12610-58b1-7752-82c3-7c1ddb82f21a#L12,L526,L691`
- scope: 专利、论文、开题报告、规格书等多步骤材料任务
- confidence: high
- overlap: reinforces C-20261014-001
- status: pending_review

## C-20261014-007

- claim: 用户期望匹配任务的 Skill 被动触发；无法确认触发时应区分资格、选择器观测和实际加载，不把未观测误报为未触发或已触发。
- evidence: `batch-001`: `01a110ab-dbb0-7f10-9f7d-a31f4ce0e75c#L12,L553,L1159`; `01a117d1-2764-72e2-ad04-6d9436d6ce3e#L12,L242,L253,L315`; `01a1102f-03ff-78d0-a2cb-0c548a5fc046#L1338,L1883,L2291,L2543`
- scope: 个人 Skill 路由、触发审计和长程重路由
- confidence: high
- overlap: reinforces `skills/personal-context/SKILL.md` and routing audit notes
- status: pending_review

## C-20261014-014

- claim: 新产品或工程项目先建立可调整的 PLAN.md，明确架构、目标、输入输出和验收标准，再进入实现。
- evidence: `019ff1d6-4550-7441-a14c-a7e4d1695d48#L9`; `019ff1d5-eb3d-7292-a1a6-aaff2c18ad39#L9`; `019ff1d6-cccb-7113-ad3e-e1e694689557#L9`
- scope: 新产品、Demo、工程和研究工具项目
- confidence: high
- overlap: reinforces C-20261014-001 and C-20261014-003
- privacy: safe_to_sync
- status: pending_review

## C-20261014-015

- claim: 给 Agent 的任务必须明确权威项目根目录、要读取的文件、目标、边界、可修改范围、预期结果和验收方式；不能依赖隐含路径或上下文。
- evidence: `01a1087d-3246-7ec3-a3a0-f49546b4c391#L471,6709`; `01a10644-aeb3-74b3-abac-f511ead2e049#L1577,1718`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L7084`
- scope: 委托 Agent 执行工程、研究和远程任务
- confidence: high
- overlap: new; complements C-20261014-009
- privacy: safe_to_sync
- status: pending_review

## C-20261014-022

- claim: 在已授权的研究或工程范围内，常规迭代可以自主完成；向用户汇报时集中呈现最终结果、逻辑链、证据边界和需要人工判断的少数事项，不必逐步请求确认。
- evidence: `01a10644-aeb3-74b3-abac-f511ead2e049#L4052,3497`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L5514`
- scope: L5/L6科研和工程迭代
- confidence: high
- overlap: new; complements C-20261014-011
- privacy: safe_to_sync
- status: pending_review

## C-20261014-038

- claim: 复杂项目先形成需求文档、SDD/约定文档、任务拆解报告和评估方案，再按拆解执行并给出面向人的验收汇报。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L391,681,2174`
- scope: 多步骤工程、科研工具和 Agent 项目
- confidence: high
- overlap: reinforces C-20261014-014 and C-20261014-020
- privacy: safe_to_sync
- status: pending_review

## C-20261014-040

- claim: Goal Prompt 必须标明项目地址、目标、预期结果、约束、需要读取的文档、可修改范围和验收文档；在这些要素含糊时先反馈，不直接执行。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L18,3457,391,584`; `01a0de32-f9d8-7691-9871-af57b35b13fd#L237`
- scope: Agent委托、远程项目和持续执行任务
- confidence: high
- overlap: reinforces C-20261014-015
- privacy: safe_to_sync
- status: pending_review

## C-20261014-041

- claim: 开始任务前先确认工作目录、是否新建项目、模型和训练需求、输入材料与时间边界；如果任务目的尚未收敛，应先暂停讨论，不盲目运行。
- evidence: `01a0de32-f9d8-7691-9871-af57b35b13fd#L237,41`; `01a0f78f-e0ea-7a70-ab46-85f58a670924#L3046`
- scope: 科研实验、远程工程和新项目启动
- confidence: high
- overlap: reinforces C-20261014-016 and C-20261014-039
- privacy: safe_to_sync
- status: pending_review

## C-20261014-042

- claim: 长程任务中主 Agent 尽量只负责规划、约束和分发，子 Agent 负责执行；项目文档和 Prompt 可用英文统一，向用户汇报使用中文。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L3457,140`; `01a0f78f-e0ea-7a70-ab46-85f58a670924#L18`
- scope: L6 Agent编排、科研工程和跨环境执行
- confidence: high
- overlap: reinforces C-20261014-022 and existing L5/L6 guidance
- privacy: safe_to_sync
- status: pending_review

## C-20261014-045

- claim: 可以优先复用开源项目，但要根据已定位的错误原因决定是否修改，并在需求、约束、目的和结果中保留复用边界与来源。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L3457`
- scope: Agent系统、工程集成和科研工具开发
- confidence: medium
- overlap: new
- privacy: safe_to_sync
- status: pending_review

# Candidate Rules

候选规则必须包含来源、范围、置信度和人工处理状态。

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

## C-20261014-004

- claim: 参考模板提供结构、版式和检查维度；参考材料中的事实不能直接写入用户材料，目标材料与最新材料必须先建立清单。
- evidence: `batch-001`: `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L414,L1350,L6129,L10193,L13172,L13247`; `01a12dfc-1aab-7101-bf6d-c2758be02026#L903,L1173`
- scope: 专利、论文、简历和其他参考模板驱动的文档任务
- confidence: high
- status: pending_review

## C-20261014-005

- claim: 编辑已有文档时默认保留原结构和风格；文字、版式、渲染和目标路径分别验收，只有用户明确要求才重构模板。
- evidence: `batch-001`: `01a1078a-5052-73a2-b38e-5624a193a91f#L487,L560`; `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L3210,L3945,L11275,L11765,L12340`
- scope: 简历、专利、开题报告、PDF/Word/HTML 等已有材料
- confidence: high
- overlap: partially covered by `habits/communication.md`
- status: pending_review

## C-20261014-006

- claim: 研究写作先锁定论文类型、中心逻辑和贡献层级，再修改具体段落；用户冻结某一节时，后续工作转移到明确指定的节。
- evidence: `batch-001`: `01a12dfc-1aab-7101-bf6d-c2758be02026#L627,L810,L903,L1173`; `01a129b0-b99c-7f42-96c0-a0f4b948f786#L31,L22,L148,L253,L564`
- scope: Benchmark、ICML 论文、Intro、方法与实验写作
- confidence: high
- overlap: reinforces existing academic-write guidance
- status: pending_review

## C-20261014-007

- claim: 用户期望匹配任务的 Skill 被动触发；无法确认触发时应区分资格、选择器观测和实际加载，不把未观测误报为未触发或已触发。
- evidence: `batch-001`: `01a110ab-dbb0-7f10-9f7d-a31f4ce0e75c#L12,L553,L1159`; `01a117d1-2764-72e2-ad04-6d9436d6ce3e#L12,L242,L253,L315`; `01a1102f-03ff-78d0-a2cb-0c548a5fc046#L1338,L1883,L2291,L2543`
- scope: 个人 Skill 路由、触发审计和长程重路由
- confidence: high
- overlap: reinforces `skills/personal-context/SKILL.md` and routing audit notes
- status: pending_review

## C-20261014-008

- claim: 验证的目标是减少无关和重复检查，同时保留能证明变更路径的最小证据；少做验证不等于不验收。
- evidence: `batch-001`: `01a117d1-2764-72e2-ad04-6d9436d6ce3e#L315,L594`
- scope: 代码、Skill 和工程任务
- confidence: high
- overlap: evidence-only candidate; already covered by `minimal-validation-workflow`
- status: pending_review

## C-20261014-009

- claim: 远程工程任务要先声明权威工作区、执行通道和同步边界；本地、服务器和浏览器各自的结果只能在对应证据成立后报告为完成。
- evidence: `batch-001`: `01a1065a-38b3-74f0-b70a-b05d3e7c9c9c#L12`; `01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7#L12`; `01a12aad-f0a6-7231-9c18-bd8b38e73036#L12`; `01a134f8-4858-77f0-9b71-6e9c7a96f06c#L8,L34`
- scope: SSH、远程服务器、AutoFill、浏览器和科研项目同步
- confidence: high
- overlap: reinforces existing RAGSystem and browser-channel guidance
- status: pending_review

## C-20261014-010

- claim: 第一次使用插件或浏览器工具时，用户偏好按步骤看到当前界面和下一步；完成授权和边界确认后可以转为自主执行。
- evidence: `batch-001`: `019ff24d-6d48-7321-80f0-e96c1cedbeda#L190,L421,L433,L444,L454,L464,L474,L485,L1261`
- scope: 插件安装、浏览器和不熟悉的工具
- confidence: medium
- status: pending_review

## C-20261014-011

- claim: 重复意图审计和阶段汇报应优先给出用户意图、模型行为、原因和证据边界，减少与结论无关的进度播报。
- evidence: `batch-001`: `01a1102f-03ff-78d0-a2cb-0c548a5fc046#L685,L748,L1112`
- scope: 重复意图分析、工程进展和对外汇报
- confidence: high
- overlap: reinforces `habits/communication.md`
- status: pending_review

## C-20261014-012

- claim: 专利具体实施方案要把每个步骤分别写成已经完成的输入、动作和输出，并与发明内容中的步骤一一对应；不要把步骤合并成模糊的计划语气。
- evidence: `batch-001`: `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L9638,L10193,L11136`
- scope: 专利交底书和说明书
- confidence: high
- status: pending_review

## C-20261014-013

- claim: 材料交付需要同时检查语义内容和渲染结果；公式编号、箭头指向、字体、居中、图示同步等视觉问题不能由文本扫描替代。
- evidence: `batch-001`: `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L3210,L6738,L8585,L11275,L11765,L12340`
- scope: 专利、简历、PDF/Word 和图示材料
- confidence: high
- overlap: reinforces document and PDF render-validation guidance
- status: pending_review

## Batch 002 — 2026-10-14

以下候选来自第二批 20 个父级对话；原始证据包仍只保留在本机工作区。所有条目都需要人工批量审核后才能晋升。

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

## C-20261014-016

- claim: 开始实验或大规模运行前先做只读预检，并用小样本验证输入输出和运行稳定性；预检阻塞时停止，基线和历史结果保持可追溯。
- evidence: `01a10644-aeb3-74b3-abac-f511ead2e049#L82,42,32`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L5514,621`
- scope: 模型训练、评测和远程科研实验
- confidence: high
- overlap: new; partly reinforces C-20261014-008
- privacy: safe_to_sync
- status: pending_review

## C-20261014-017

- claim: 项目执行状态、实验记录和论文叙事要分开存放；项目变化不应自动改写论文，只有明确指定的同步任务才更新论文。
- evidence: `01a10644-aeb3-74b3-abac-f511ead2e049#L1577,1718`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L5514,5837`
- scope: 毕业设计、ICML论文和科研工程项目
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: pending_review

## C-20261014-018

- claim: Benchmark 论文先保证 benchmark 的任务定义、评价框架和实证发现成立；方法模块只是被评测对象，正文应移除路径、版本、哈希和项目日志等内部管理信息。
- evidence: `01a0fe11-bb1e-7611-afc3-6a939e318c78#L36,951`; `01a11266-18ff-7b92-bdec-81772b1c0b18#L960`
- scope: Benchmark、ICML和评价型论文
- confidence: high
- overlap: reinforces C-20261014-006 and existing academic-write guidance
- privacy: safe_to_sync
- status: pending_review

## C-20261014-019

- claim: 提出或实现方法前先从真实错误和任务难点建立因果链；先讨论问题定义、假设和可检验机制，再编码，不能把一个路由判断点直接包装成方法机制。
- evidence: `01a11266-18ff-7b92-bdec-81772b1c0b18#L960,691`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L4245,4265`
- scope: Benchmark方法设计、实验迭代和论文叙事
- confidence: high
- overlap: new; complements C-20261014-018
- privacy: safe_to_sync
- status: pending_review

## C-20261014-020

- claim: 工程或实验验收必须说明覆盖了哪些完整数据和测试集，并保留失败问题、修复动作、前后结果和当前状态；只通过单个样本不能报告整体完成。
- evidence: `01a1087d-3246-7ec3-a3a0-f49546b4c391#L658,2836,2176`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L6347`
- scope: Demo构建、模型实验和项目汇报
- confidence: high
- overlap: reinforces C-20261014-008 and C-20261014-011
- privacy: safe_to_sync
- status: pending_review

## C-20261014-021

- claim: Demo或可视化产品必须把测试数据放在按 demo ID 划分的 testdata 中，使用可执行的验收契约和真实浏览器可见结果；Builder 只改授权目录，未通过测试的结果不能发布。
- evidence: `01a117ce-5f61-7ac3-8fdf-2fcf570aa0b6#L9`; `01a1087d-3246-7ec3-a3a0-f49546b4c391#L125,4038,658`
- scope: Demo生成器、前端展示和CLI Builder工作流
- confidence: high
- overlap: new
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

## C-20261014-023

- claim: 模型改进前先审计数据管道、证据完整性、标签和参考答案冲突；找不到材料时明确标记未找到，不能根据最终结果反推过程或把不可靠标签当成人工金标准。
- evidence: `01a11266-18ff-7b92-bdec-81772b1c0b18#L1268,3853,691`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L4265,4370`
- scope: 科研数据、Benchmark标注和模型实验
- confidence: high
- overlap: new; complements C-20261014-019
- privacy: safe_to_sync
- status: pending_review

## C-20261014-024

- claim: 面向导师或非工程听众的汇报以行为和产出、核心结论和下一步判断为主，隐藏无助于决策的工程细节。
- evidence: `01a12e11-c5c2-71f0-871f-a34737fc4f2a#L12,581,638`; `01a11266-18ff-7b92-bdec-81772b1c0b18#L215`
- scope: 组会、导师汇报和阶段性项目报告
- confidence: high
- overlap: reinforces C-20261014-011
- privacy: safe_to_sync
- status: pending_review

## C-20261014-025

- claim: 编辑简历时保留已有真实经历和用户明确要求的重点；不能静默删除经历或把未经用户审核的草稿内容当成事实，新增内容应标为待审核草稿。
- evidence: `019fb23f-7970-7062-a9d4-fcc5a65df049#L1353,1500,1138,1113`; `019fb23f-7970-7062-a9d4-fcc5a65df049#L1712,842`
- scope: 简历、求职材料和个人经历描述
- confidence: medium
- overlap: reinforces C-20261014-005; conflicting evidence requires review
- privacy: safe_to_sync
- status: pending_review

## Batch 003 — 2026-10-14

以下候选来自第三批 20 个父级对话；原始证据包仍只保留在本机工作区。所有条目都需要人工批量审核后才能晋升。

## C-20261014-026

- claim: 简历中的项目、技术栈和贡献先基于真实项目材料核验，并为新增表述准备可追问的面试证据；未经核验的内容只能作为待审核草稿。
- evidence: `019fc335-4f96-78e1-afc4-070dd9e47b5c#L9`; `019fc30c-a94e-7f50-971c-c4adcd1a2811#L9,125,265,289`
- scope: 简历、项目经历和面试准备
- confidence: high
- overlap: reinforces C-20261014-025
- privacy: safe_to_sync
- status: pending_review

## C-20261014-027

- claim: 可视化 Demo 的验收契约是唯一验收来源，应使用指定 testdata、精确选择器和真实浏览器可见结果；不能用模型自报或更弱的测试替代，并应保留已有通过行为。
- evidence: `01a1128a-01ea-7ae1-9538-1a5e2443cdc1#L9`; `01a11a0d-7362-78f0-a885-ba87ee4f17cc#L9`; `01a117e5-c5be-7f00-95a7-db4bca838c6e#L9`
- scope: DemoPilot、CLI Builder和浏览器验收
- confidence: high
- overlap: reinforces C-20261014-021
- privacy: safe_to_sync
- status: pending_review

## C-20261014-028

- claim: 大题库或知识材料按约 20 题的小批次处理；按知识点去重，保留覆盖多个知识点的题目，并为每个代表题提供可复用解析，不一次性读取全量材料。
- evidence: `01a116af-faaf-73b0-a7db-17c5e66eebc3#L12,1205`
- scope: 刷题库、知识抽取和大规模材料整理
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: pending_review

## C-20261014-029

- claim: 删除远程旧目录前先清理旧路径引用、核对迁移文件和哈希、完成提交或压缩归档，再执行删除；遇到删除风险先说明影响范围。
- evidence: `01a12aaf-133a-7d63-977d-927f3b56711e#L334,384`
- scope: 服务器迁移、旧目录清理和工程归档
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: pending_review

## C-20261014-030

- claim: 研究主张先写成可检验假设并明确审核标准，再判断 benchmark 是否合理、独特和足够；结论范围必须服从已有证据，不能把初步结果写成普遍规律。
- evidence: `01a09902-7e8e-7290-af3d-e24a15f69e60#L418,444,989,1943,2256,2559`
- scope: Benchmark设计、论文审查和研究结论
- confidence: high
- overlap: reinforces C-20261014-019 and C-20261014-023
- privacy: safe_to_sync
- status: pending_review

## C-20261014-031

- claim: 人工审核按小批次逐题进行，已审核题目不重复；用户看不懂原文时先提供中文翻译，同时保留每题判断、分歧和记录缺口。
- evidence: `01a09902-7e8e-7290-af3d-e24a15f69e60#L373,444,1503,2580`
- scope: Benchmark人工审核、标注和证据核验
- confidence: high
- overlap: new; complements C-20261014-023
- privacy: safe_to_sync
- status: pending_review

## C-20261014-032

- claim: 论文整体逻辑稳定后只做定位明确的文字层小步修改；先确认待改位置和外部编辑 Prompt，再修改，避免无边界的大面积重写。
- evidence: `01a116a5-96a5-7cb3-8150-3c62ba850e3f#L410,4353,4564`
- scope: ICML论文和其他已有学术文稿
- confidence: high
- overlap: reinforces C-20261014-006 and C-20261014-018
- privacy: safe_to_sync
- status: pending_review

## C-20261014-033

- claim: 固定人工审核评测集与开发集用途分离：固定评测集的人工 judgments 用作评测依据，模型选择和阈值学习使用开发集；论文应准确描述评测集用途和人工审核范围。
- evidence: `01a116a5-96a5-7cb3-8150-3c62ba850e3f#L314,1178,258`; `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3#L2297`
- scope: Core200、Benchmark和模型评测
- confidence: high
- overlap: new; complements C-20261014-018 and C-20261014-023
- privacy: safe_to_sync
- status: pending_review

## C-20261014-034

- claim: 模型对比使用同一数据划分和统一指标，并在需要时重复运行报告随机方差；至少同时呈现 Direct、候选方法和组合方法的可比结果。
- evidence: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3#L2115,503,4800`
- scope: JEV、模型路由和 Benchmark实验
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: pending_review

## C-20261014-035

- claim: 解释复杂技术时先用直白、具体的语言说明核心行为，再从代码或前向过程补充机制，并明确它与一般模型的差异。
- evidence: `01a0e149-edce-7c41-9ef4-34c4a27edfb8#L269,305,317`; `01a0ddd6-44b2-7a60-ada3-74bc62dbf566#L9`
- scope: 模型、算法和科研代码解释
- confidence: medium
- overlap: reinforces profile.md communication guidance
- privacy: safe_to_sync
- status: pending_review

## C-20261014-036

- claim: 论文或实验报告要把已验证材料、缺失归档和结论范围分开呈现；有人工审核汇总不等于每条模型输出都已人工核验，缺口应保留为缺口。
- evidence: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3#L2297,1374`; `01a09902-7e8e-7290-af3d-e24a15f69e60#L2580,53`
- scope: Benchmark证据、论文审计和结果汇报
- confidence: high
- overlap: reinforces C-20261014-023 and C-20261014-030
- privacy: safe_to_sync
- status: pending_review

## Batch 004 — 2026-10-14

以下候选来自第四批 20 个父级对话；原始证据包仍只保留在本机工作区。所有条目都需要人工批量审核后才能晋升。

## C-20261014-037

- claim: AI任务可视化应按 Workspace→Run→Task Graph 保留每次运行的独立历史，并通过明确的 HTTP/JSON 协议接收状态；可自动验证的任务自动验收，无法自动验证的任务进入待验收。
- evidence: `019f92c5-1c9c-78a3-acb0-c23a892d49c1#L9,61,104,126,147,221`
- scope: AI任务图、工程执行可视化和长程任务追踪
- confidence: high
- overlap: new
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

## C-20261014-039

- claim: 工程或实验迭代形成问题发现→问题拆分与统计→失败归因→数据集实验→效果比较的循环，并只记录重要、可改进的失败，不把单纯环境未准备好当作核心问题。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L218,2174,3046`
- scope: Agent工程、模型实验和持续改进
- confidence: high
- overlap: new; complements C-20261014-020 and C-20261014-022
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

## C-20261014-043

- claim: 自动填表系统的硬性安全目标是宁可降低可填写数量，也要避免证据不足时错误填写；应把错误填写率或安全阈值作为独立验收指标。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L140,218`; `01a0de32-f9d8-7691-9871-af57b35b13fd#L41`
- scope: AutoFill、JEV和证据不足路由
- confidence: high
- overlap: reinforces C-20261014-019 and existing AutoFill guidance
- privacy: safe_to_sync
- status: pending_review

## C-20261014-044

- claim: 跨环境项目要明确服务器、浏览器和本机的执行边界；例如服务器承担模型和工程任务，主机浏览器承担真实网页验收，完成后释放临时资源。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L1051,265`; `01a0f78f-e0ea-7a70-ab46-85f58a670924#L3457`
- scope: 远程科研工程、浏览器验收和模型运行
- confidence: high
- overlap: reinforces C-20261014-009 and C-20261014-015
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

## C-20261014-046

- claim: 面向用户的实验汇报先用最简洁的结构说明任务、流程、结果和差异；复杂执行细节保留在项目记录中，需要时再追溯。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L425,3046`; `01a0de32-f9d8-7691-9871-af57b35b13fd#L41`
- scope: 科研实验、远程工程和阶段汇报
- confidence: high
- overlap: reinforces C-20261014-011 and C-20261014-024
- privacy: safe_to_sync
- status: pending_review

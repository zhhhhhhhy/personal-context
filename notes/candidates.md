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

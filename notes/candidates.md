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
- evidence: `batch-001`: `01a1078a-5052-73a2-b38e-5624a193a91f#L147,L487,L560`; `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L3210,L3945,L11275,L11765,L12340`
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

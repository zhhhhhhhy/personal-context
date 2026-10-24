# 工程与环境

历史候选原文；已逐条裁决。按 disposition 和目标记忆使用，不能把旧 claim 整条当成生效规则。

## C-20261014-008

- claim: 验证的目标是减少无关和重复检查，同时保留能证明变更路径的最小证据；少做验证不等于不验收。
- evidence: `batch-001`: `01a117d1-2764-72e2-ad04-6d9436d6ce3e#L315,L594`
- scope: 代码、Skill 和工程任务
- confidence: high
- overlap: evidence-only candidate; already covered by `minimal-validation-workflow`
- status: resolved
- disposition: rule / merge_existing_coverage
- destination: validation.scoped-acceptance

## C-20261014-009

- claim: 远程工程任务要先声明权威工作区、执行通道和同步边界；本地、服务器和浏览器各自的结果只能在对应证据成立后报告为完成。
- evidence: `batch-001`: `01a1065a-38b3-74f0-b70a-b05d3e7c9c9c#L12`; `01a12ad7-d6a3-72e0-8b0e-bcb71d595eb7#L12`; `01a12aad-f0a6-7231-9c18-bd8b38e73036#L12`; `01a134f8-4858-77f0-9b71-6e9c7a96f06c#L8,L34`
- scope: SSH、远程服务器、AutoFill、浏览器和科研项目同步
- confidence: high
- overlap: reinforces existing RAGSystem and browser-channel guidance
- status: resolved
- disposition: project / scope_project_material
- destination: project.rag-contract-v3

## C-20261014-021

- claim: Demo或可视化产品必须把测试数据放在按 demo ID 划分的 testdata 中，使用可执行的验收契约和真实浏览器可见结果；Builder 只改授权目录，未通过测试的结果不能发布。
- evidence: `01a117ce-5f61-7ac3-8fdf-2fcf570aa0b6#L9`; `01a1087d-3246-7ec3-a3a0-f49546b4c391#L125,4038,658`
- scope: Demo生成器、前端展示和CLI Builder工作流
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: resolved
- disposition: skill / merge_existing_method
- destination: skill.engineering-methods-v2

## C-20261014-027

- claim: 可视化 Demo 的验收契约是唯一验收来源，应使用指定 testdata、精确选择器和真实浏览器可见结果；不能用模型自报或更弱的测试替代，并应保留已有通过行为。
- evidence: `01a1128a-01ea-7ae1-9538-1a5e2443cdc1#L9`; `01a11a0d-7362-78f0-a885-ba87ee4f17cc#L9`; `01a117e5-c5be-7f00-95a7-db4bca838c6e#L9`
- scope: DemoPilot、CLI Builder和浏览器验收
- confidence: high
- overlap: reinforces C-20261014-021
- privacy: safe_to_sync
- status: resolved
- disposition: discard / discarded
- destination: discarded

## C-20261014-029

- claim: 删除远程旧目录前先清理旧路径引用、核对迁移文件和哈希、完成提交或压缩归档，再执行删除；遇到删除风险先说明影响范围。
- evidence: `01a12aaf-133a-7d63-977d-927f3b56711e#L334,384`
- scope: 服务器迁移、旧目录清理和工程归档
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: resolved
- disposition: memory / concise_reusable
- destination: migration.verify-before-cleanup-v2

## C-20261014-037

- claim: AI任务可视化应按 Workspace→Run→Task Graph 保留每次运行的独立历史，并通过明确的 HTTP/JSON 协议接收状态；可自动验证的任务自动验收，无法自动验证的任务进入待验收。
- evidence: `019f92c5-1c9c-78a3-acb0-c23a892d49c1#L9,61,104,126,147,221`
- scope: AI任务图、工程执行可视化和长程任务追踪
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: resolved
- disposition: project / scope_project_material
- destination: project.taskgraph-design-scoped-v2

## C-20261014-044

- claim: 跨环境项目要明确服务器、浏览器和本机的执行边界；例如服务器承担模型和工程任务，主机浏览器承担真实网页验收，完成后释放临时资源。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L1051,265`; `01a0f78f-e0ea-7a70-ab46-85f58a670924#L3457`
- scope: 远程科研工程、浏览器验收和模型运行
- confidence: high
- overlap: reinforces C-20261014-009 and C-20261014-015
- privacy: safe_to_sync
- status: resolved
- disposition: archive / archive_history_constraints_retained
- destination: remote.server-browser-topology

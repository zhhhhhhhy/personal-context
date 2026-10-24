# 文档与模板

历史候选原文；已逐条裁决。按 disposition 和目标记忆使用，不能把旧 claim 整条当成生效规则。

## C-20261014-004

- claim: 参考模板提供结构、版式和检查维度；参考材料中的事实不能直接写入用户材料，目标材料与最新材料必须先建立清单。
- evidence: `batch-001`: `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L414,L1350,L6129,L10193,L13172,L13247`; `01a12dfc-1aab-7101-bf6d-c2758be02026#L903,L1173`
- scope: 专利、论文、简历和其他参考模板驱动的文档任务
- confidence: high
- status: resolved
- disposition: skill / already_covered
- destination: skill.patent-workflow-v2

## C-20261014-005

- claim: 编辑已有文档时默认保留原结构和风格；文字、版式、渲染和目标路径分别验收，只有用户明确要求才重构模板。
- evidence: `batch-001`: `01a1078a-5052-73a2-b38e-5624a193a91f#L487,L560`; `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L3210,L3945,L11275,L11765,L12340`
- scope: 简历、专利、开题报告、PDF/Word/HTML 等已有材料
- confidence: high
- overlap: partially covered by `habits/communication.md`
- status: resolved
- disposition: rule / new
- destination: documents.preserve-style-v2

## C-20261014-012

- claim: 专利具体实施方案要把每个步骤分别写成已经完成的输入、动作和输出，并与发明内容中的步骤一一对应；不要把步骤合并成模糊的计划语气。
- evidence: `batch-001`: `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L9638,L10193,L11136`
- scope: 专利交底书和说明书
- confidence: high
- status: resolved
- disposition: skill / already_covered
- destination: skill.patent-workflow-v2

## C-20261014-013

- claim: 材料交付需要同时检查语义内容和渲染结果；公式编号、箭头指向、字体、居中、图示同步等视觉问题不能由文本扫描替代。
- evidence: `batch-001`: `01a0fde7-9236-78c1-9068-6867a4ce6d8e#L3210,L6738,L8585,L11275,L11765,L12340`
- scope: 专利、简历、PDF/Word 和图示材料
- confidence: high
- overlap: reinforces document and PDF render-validation guidance
- status: resolved
- disposition: skill / already_covered
- destination: skill.patent-workflow-v2

## C-20261014-025

- claim: 编辑简历时保留已有真实经历和用户明确要求的重点；不能静默删除经历或把未经用户审核的草稿内容当成事实，新增内容应标为待审核草稿。
- evidence: `019fb23f-7970-7062-a9d4-fcc5a65df049#L1353,1500,1138,1113`; `019fb23f-7970-7062-a9d4-fcc5a65df049#L1712,842`
- scope: 简历、求职材料和个人经历描述
- confidence: medium
- overlap: reinforces C-20261014-005; conflicting evidence requires review
- privacy: safe_to_sync
- status: resolved
- disposition: discard / discarded
- destination: discarded

## C-20261014-026

- claim: 简历中的项目、技术栈和贡献先基于真实项目材料核验，并为新增表述准备可追问的面试证据；未经核验的内容只能作为待审核草稿。
- evidence: `019fc335-4f96-78e1-afc4-070dd9e47b5c#L9`; `019fc30c-a94e-7f50-971c-c4adcd1a2811#L9,125,265,289`
- scope: 简历、项目经历和面试准备
- confidence: high
- overlap: reinforces C-20261014-025
- privacy: safe_to_sync
- status: resolved
- disposition: memory / concise_reusable
- destination: local.verify-project-materials-v3

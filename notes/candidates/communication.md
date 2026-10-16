# 沟通与学习

历史候选原文；已逐条裁决。按 disposition 和目标记忆使用，不能把旧 claim 整条当成生效规则。

## C-20261014-010

- claim: 第一次使用插件或浏览器工具时，用户偏好按步骤看到当前界面和下一步；完成授权和边界确认后可以转为自主执行。
- evidence: `batch-001`: `019ff24d-6d48-7321-80f0-e96c1cedbeda#L190,L421,L433,L444,L454,L464,L474,L485,L1261`
- scope: 插件安装、浏览器和不熟悉的工具
- confidence: medium
- status: resolved
- disposition: memory / concise_reusable
- destination: learning.adaptive-guidance

## C-20261014-011

- claim: 重复意图审计和阶段汇报应优先给出用户意图、模型行为、原因和证据边界，减少与结论无关的进度播报。
- evidence: `batch-001`: `01a1102f-03ff-78d0-a2cb-0c548a5fc046#L685,L748,L1112`
- scope: 重复意图分析、工程进展和对外汇报
- confidence: high
- overlap: reinforces `habits/communication.md`
- status: resolved
- disposition: archive / archive_duplicate_receipt
- destination: core.communication

## C-20261014-024

- claim: 面向导师或非工程听众的汇报以行为和产出、核心结论和下一步判断为主，隐藏无助于决策的工程细节。
- evidence: `01a12e11-c5c2-71f0-871f-a34737fc4f2a#L12,581,638`; `01a11266-18ff-7b92-bdec-81772b1c0b18#L215`
- scope: 组会、导师汇报和阶段性项目报告
- confidence: high
- overlap: reinforces C-20261014-011
- privacy: safe_to_sync
- status: resolved
- disposition: archive / archive_duplicate_receipt
- destination: core.communication

## C-20261014-028

- claim: 大题库或知识材料按约 20 题的小批次处理；按知识点去重，保留覆盖多个知识点的题目，并为每个代表题提供可复用解析，不一次性读取全量材料。
- evidence: `01a116af-faaf-73b0-a7db-17c5e66eebc3#L12,1205`
- scope: 刷题库、知识抽取和大规模材料整理
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: resolved
- disposition: memory / concise_reusable
- destination: learning.deduplicate-by-knowledge-v2

## C-20261014-035

- claim: 解释复杂技术时先用直白、具体的语言说明核心行为，再从代码或前向过程补充机制，并明确它与一般模型的差异。
- evidence: `01a0e149-edce-7c41-9ef4-34c4a27edfb8#L269,305,317`; `01a0ddd6-44b2-7a60-ada3-74bc62dbf566#L9`
- scope: 模型、算法和科研代码解释
- confidence: medium
- overlap: reinforces profile.md communication guidance
- privacy: safe_to_sync
- status: resolved
- disposition: archive / archive_duplicate_receipt
- destination: core.communication

## C-20261014-046

- claim: 面向用户的实验汇报先用最简洁的结构说明任务、流程、结果和差异；复杂执行细节保留在项目记录中，需要时再追溯。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L425,3046`; `01a0de32-f9d8-7691-9871-af57b35b13fd#L41`
- scope: 科研实验、远程工程和阶段汇报
- confidence: high
- overlap: reinforces C-20261014-011 and C-20261014-024
- privacy: safe_to_sync
- status: resolved
- disposition: archive / archive_duplicate_receipt
- destination: core.communication

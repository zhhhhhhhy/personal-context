# 研究与论文

历史候选原文；已逐条裁决。按 disposition 和目标记忆使用，不能把旧 claim 整条当成生效规则。

## C-20261014-006

- claim: 研究写作先锁定论文类型、中心逻辑和贡献层级，再修改具体段落；用户冻结某一节时，后续工作转移到明确指定的节。
- evidence: `batch-001`: `01a12dfc-1aab-7101-bf6d-c2758be02026#L627,L810,L903,L1173`; `01a129b0-b99c-7f42-96c0-a0f4b948f786#L31,L22,L148,L253,L564`
- scope: Benchmark、ICML 论文、Intro、方法与实验写作
- confidence: high
- overlap: reinforces existing academic-write guidance
- status: resolved
- disposition: skill / already_covered
- destination: skill.academic-writing-entry

## C-20261014-017

- claim: 项目执行状态、实验记录和论文叙事要分开存放；项目变化不应自动改写论文，只有明确指定的同步任务才更新论文。
- evidence: `01a10644-aeb3-74b3-abac-f511ead2e049#L1577,1718`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L5514,5837`
- scope: 毕业设计、ICML论文和科研工程项目
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: resolved
- disposition: archive / archive_history_constraints_retained
- destination: research.paper-sync-current

## C-20261014-018

- claim: Benchmark 论文先保证 benchmark 的任务定义、评价框架和实证发现成立；方法模块只是被评测对象，正文应移除路径、版本、哈希和项目日志等内部管理信息。
- evidence: `01a0fe11-bb1e-7611-afc3-6a939e318c78#L36,951`; `01a11266-18ff-7b92-bdec-81772b1c0b18#L960`
- scope: Benchmark、ICML和评价型论文
- confidence: high
- overlap: reinforces C-20261014-006 and existing academic-write guidance
- privacy: safe_to_sync
- status: resolved
- disposition: skill / already_covered
- destination: skill.academic-writing-entry

## C-20261014-019

- claim: 提出或实现方法前先从真实错误和任务难点建立因果链；先讨论问题定义、假设和可检验机制，再编码，不能把一个路由判断点直接包装成方法机制。
- evidence: `01a11266-18ff-7b92-bdec-81772b1c0b18#L960,691`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L4245,4265`
- scope: Benchmark方法设计、实验迭代和论文叙事
- confidence: high
- overlap: new; complements C-20261014-018
- privacy: safe_to_sync
- status: resolved
- disposition: skill / refined
- destination: skill.academic-writing-entry

## C-20261014-030

- claim: 研究主张先写成可检验假设并明确审核标准，再判断 benchmark 是否合理、独特和足够；结论范围必须服从已有证据，不能把初步结果写成普遍规律。
- evidence: `01a09902-7e8e-7290-af3d-e24a15f69e60#L418,444,989,1943,2256,2559`
- scope: Benchmark设计、论文审查和研究结论
- confidence: high
- overlap: reinforces C-20261014-019 and C-20261014-023
- privacy: safe_to_sync
- status: resolved
- disposition: skill / already_covered
- destination: skill.academic-writing-entry

## C-20261014-032

- claim: 论文整体逻辑稳定后只做定位明确的文字层小步修改；先确认待改位置和外部编辑 Prompt，再修改，避免无边界的大面积重写。
- evidence: `01a116a5-96a5-7cb3-8150-3c62ba850e3f#L410,4353,4564`
- scope: ICML论文和其他已有学术文稿
- confidence: high
- overlap: reinforces C-20261014-006 and C-20261014-018
- privacy: safe_to_sync
- status: resolved
- disposition: archive / archive_history_constraints_retained
- destination: research.localized-paper-edits

## C-20261014-036

- claim: 论文或实验报告要把已验证材料、缺失归档和结论范围分开呈现；有人工审核汇总不等于每条模型输出都已人工核验，缺口应保留为缺口。
- evidence: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3#L2297,1374`; `01a09902-7e8e-7290-af3d-e24a15f69e60#L2580,53`
- scope: Benchmark证据、论文审计和结果汇报
- confidence: high
- overlap: reinforces C-20261014-023 and C-20261014-030
- privacy: safe_to_sync
- status: resolved
- disposition: skill / refined
- destination: skill.academic-writing-entry

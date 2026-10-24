# 实验与证据

历史候选原文；已逐条裁决。按 disposition 和目标记忆使用，不能把旧 claim 整条当成生效规则。

## C-20261014-016

- claim: 开始实验或大规模运行前先做只读预检，并用小样本验证输入输出和运行稳定性；预检阻塞时停止，基线和历史结果保持可追溯。
- evidence: `01a10644-aeb3-74b3-abac-f511ead2e049#L82,42,32`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L5514,621`
- scope: 模型训练、评测和远程科研实验
- confidence: high
- overlap: new; partly reinforces C-20261014-008
- privacy: safe_to_sync
- status: resolved
- disposition: skill / merge_existing_method
- destination: skill.engineering-methods-v2

## C-20261014-020

- claim: 工程或实验验收必须说明覆盖了哪些完整数据和测试集，并保留失败问题、修复动作、前后结果和当前状态；只通过单个样本不能报告整体完成。
- evidence: `01a1087d-3246-7ec3-a3a0-f49546b4c391#L658,2836,2176`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L6347`
- scope: Demo构建、模型实验和项目汇报
- confidence: high
- overlap: reinforces C-20261014-008 and C-20261014-011
- privacy: safe_to_sync
- status: resolved
- disposition: rule / merge_existing_coverage
- destination: validation.scoped-acceptance

## C-20261014-023

- claim: 模型改进前先审计数据管道、证据完整性、标签和参考答案冲突；找不到材料时明确标记未找到，不能根据最终结果反推过程或把不可靠标签当成人工金标准。
- evidence: `01a11266-18ff-7b92-bdec-81772b1c0b18#L1268,3853,691`; `01a0f292-cdfe-7463-ad96-65832ab94c06#L4265,4370`
- scope: 科研数据、Benchmark标注和模型实验
- confidence: high
- overlap: new; complements C-20261014-019
- privacy: safe_to_sync
- status: resolved
- disposition: skill / merge_existing_method
- destination: skill.academic-writing-entry

## C-20261014-031

- claim: 人工审核按小批次逐题进行，已审核题目不重复；用户看不懂原文时先提供中文翻译，同时保留每题判断、分歧和记录缺口。
- evidence: `01a09902-7e8e-7290-af3d-e24a15f69e60#L373,444,1503,2580`
- scope: Benchmark人工审核、标注和证据核验
- confidence: high
- overlap: new; complements C-20261014-023
- privacy: safe_to_sync
- status: resolved
- disposition: memory / concise_reusable
- destination: research.chinese-item-review-v3

## C-20261014-033

- claim: 固定人工审核评测集与开发集用途分离：固定评测集的人工 judgments 用作评测依据，模型选择和阈值学习使用开发集；论文应准确描述评测集用途和人工审核范围。
- evidence: `01a116a5-96a5-7cb3-8150-3c62ba850e3f#L314,1178,258`; `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3#L2297`
- scope: Core200、Benchmark和模型评测
- confidence: high
- overlap: new; complements C-20261014-018 and C-20261014-023
- privacy: safe_to_sync
- status: resolved
- disposition: project / scope_project_material
- destination: project.core200-provenance-v7

## C-20261014-034

- claim: 模型对比使用同一数据划分和统一指标，并在需要时重复运行报告随机方差；至少同时呈现 Direct、候选方法和组合方法的可比结果。
- evidence: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3#L2115,503,4800`
- scope: JEV、模型路由和 Benchmark实验
- confidence: high
- overlap: new
- privacy: safe_to_sync
- status: resolved
- disposition: project / scope_project_material
- destination: project.jev-comparison-v3

## C-20261014-039

- claim: 工程或实验迭代形成问题发现→问题拆分与统计→失败归因→数据集实验→效果比较的循环，并只记录重要、可改进的失败，不把单纯环境未准备好当作核心问题。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L218,2174,3046`
- scope: Agent工程、模型实验和持续改进
- confidence: high
- overlap: new; complements C-20261014-020 and C-20261014-022
- privacy: safe_to_sync
- status: resolved
- disposition: skill / merge_existing_method
- destination: skill.engineering-methods-v2

## C-20261014-043

- claim: 自动填表系统的硬性安全目标是宁可降低可填写数量，也要避免证据不足时错误填写；应把错误填写率或安全阈值作为独立验收指标。
- evidence: `01a0f78f-e0ea-7a70-ab46-85f58a670924#L140,218`; `01a0de32-f9d8-7691-9871-af57b35b13fd#L41`
- scope: AutoFill、JEV和证据不足路由
- confidence: high
- overlap: reinforces C-20261014-019 and existing AutoFill guidance
- privacy: safe_to_sync
- status: resolved
- disposition: project / scope_project_material
- destination: project.autofill-safety-v2

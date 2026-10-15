# Candidate Rules Index

46 条历史候选按主题保留原文、证据、范围和状态；它们不是已生效规则。当前晋升流程以 `docs/evolution/POLICY.md` 为准。

旧 overlap 位置是历史元信息；当前相近规则按 `INDEX.md` 和 `habits/communication.md` 核对。

| 任务信号 | 只读对应主题 | 条数 |
|---|---|---:|
| 计划、Goal Prompt、委派、触发、复用 | [任务规划与 Skill](candidates/planning-and-skills.md) | 12 |
| 版式、参考样式、专利、简历、视觉交付 | [文档与模板](candidates/documents.md) | 6 |
| 论文类型、因果链、假设、论证和结论范围 | [研究与论文](candidates/research-writing.md) | 7 |
| 数据、标签、人工审核、比较、预检和失败归因 | [实验与证据](candidates/experiments.md) | 8 |
| 验收、可视化、远程、同步、删除和执行边界 | [工程与环境](candidates/engineering.md) | 7 |
| 解释、汇报、浏览器引导、知识整理 | [沟通与学习](candidates/communication.md) | 6 |

已知 ID 时用 `python scripts/context-evolution.py show-candidate --id C-20261014-035` 精确读取单条。按主题查找时只读对应页；跨主题用 `rg -n "关键词" notes/candidates` 找命中记录。信息不足再展开其他主题，不默认拼接六页；脚本可扫描全部 ID，无需把全部正文送入模型。

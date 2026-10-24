# 项目资料入口

当前有14个活跃项目入口。只在继续对应项目时，先确认项目、目录/版本和目标材料，再读取命中条目的“续接摘要”；详细来源按需追溯。项目名相似不代表同版，历史约定不授予新权限。本次只整理已有Context，没有核验任何项目进度。

| # | 活跃入口 | 项目键 | 何时加载 |
|---|---|---|---|
| 1 | [浏览器AutoFill](browser-autofill.md) | `browser-autofill` | 错误填写指标、浏览器通道及对应版本的续接约束 |
| 2 | [RAGSystem契约](rag-system.md) | `rag-system` | 定位权威项目契约；不混用其他AutoFill设置 |
| 3 | [JEV比较与任务边界](contract-research.md) | `contract-research` | 区分系统/判断协议，核对工程、论文和外部编辑范围 |
| 4 | [任务图](taskgraph.md) | `taskgraph` | 区分历史设计与记录中的只读MVP能力 |
| 5 | [ContractFill中文稿](contractfill-zh-20261012.md) | `contract-research` | 区分旧Benchmark定位与后续重新立题讨论；先确认语种和版本 |
| 6 | [开题报告版本入口](opening-report-versions.md) | `contract-research` | 先选2026-10-03原稿或2026-10-10备份，再加载各自约定 |
| 7 | [MASArena迁移验收](masarena-migration-acceptance.md) | `contract-research` | 核对对应迁移的依赖、数据一致性及保留范围 |
| 8 | [GAIA Claude test](gaia-claude-trace-contract.md) | `gaia-claude-test` | 该项目trace、计量范围与联调验收要求 |
| 9 | [GAIA Claude Code](gaia-claude-code-inputs.md) | `gaia-claude-code` | 该项目输入/prompt契约；不与上一项目混用 |
| 10 | [reportCodex版本](reportcodex-template.md) | `reportcodex` | 模板/工作台分版本；核对JSON计划与后续Vue/Python约定 |
| 11 | [CAD3DTO2D](cad3dto2d-asm-png.md) | `cad3dto2d` | asm→PNG、装配条件和标注需求范围 |
| 12 | [Core200版本](core200-provenance.md) | `contract-research` | 按已有记录确认标签/结果版本及证据边界；不自动跟踪进度 |
| 13 | [刷题项目](bank-quiz.md) | `bank-quiz` | 定位项目README；仅启动时不加载题库整理方法 |
| 14 | [Agent/API语义匹配验证](agent-review-api-evaluation.md) | `contract-research` | 仅续接 idea-novelty-check 工作区的复核任务；项目术语与历史数量在此，当前状态按原项目索引核实 |

检索使用既有工具，例如：

```powershell
python -X utf8 D:/worker/personal-context/scripts/context-memory.py search --project reportcodex --query "模板"
python -X utf8 D:/worker/personal-context/scripts/context-memory.py show --id project.reportcodex-template-v2
```

搜索默认只返回少量路由，选中后再读正文；不整份加载所有项目。普通关键词检索默认排除项目资料。合并、替代和归档的旧记录退出默认检索，稳定偏好和通用方法仍使用原有入口。

## 归档任务（仅显式恢复原任务或追溯时读取）

归档不是完成、失效或撤销约定。下面4份原文和来源保持原样；未完成要求仍属原任务，恢复同一任务时先核对当前版本及仍适用的约束。

| 原任务 | 保留资料与边界 |
|---|---|
| [工业智能体单页PPT](industrial-slide-request.md) | 原布局、内容衔接和第五项缺口；没有确认已完成 |
| [PDF转Word修复](visual-pdf-word-uv-exception.md) | uv要求和当次API处理例外；不推广或自动延续为新权限 |
| [GAIA九题批次](gaia-new-data-nine.md) | 三级各三道及未跑数据要求；不是默认配额或运行成功记录 |
| [Benchmark文献检索](icml-published-benchmark-comparator.md) | 已发表、最接近、Benchmark三个条件；没有确认已找到 |

可用 `history --id <旧条目ID> --include-retired` 查旧条目。精简保留的11条旧记录及两份开题旧入口同样保留历史；两份开题正文未改，入口合并不拼接其约定。

其他已有历史参考：[DemoPilot旧项目补充](demopilot.md)，不计入上述14个活跃入口。

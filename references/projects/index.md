# 项目资料入口

仅在继续对应项目时加载。先用当前目录、Git remote/commit、协议或稿件确认身份；项目名相似不代表同一版本。历史日期不是失效证明，未核实的当前状态继续标为待核。

| 项目键 | 正文 | 来源版本与边界 |
|---|---|---|
| `browser-autofill` | [浏览器 AutoFill](browser-autofill.md) | 2026-10-02～04；指标、语言/分工、主机浏览器与条件模型；当前远程版本待核 |
| `rag-system` | [RAGSystem](rag-system.md) | 2026-10-04 提供的 `/workspace/zhy/RAGSystem` 契约；不与前一项擅自合并 |
| `contract-research` | [合同研究](contract-research.md) | JEV、Core200 待核问题；Core200版本资料另见下方，保留论文同步和外部编辑限制 |
| `taskgraph` | [任务图](taskgraph.md) | 2026-07-24 `D:/worker/codex-visual` 设计；实现状态待核 |
| `demopilot` | [DemoPilot 历史补充](demopilot.md) | 方法已进 Skill；目录和旧数量只留项目资料 |

检索示例：`python -X utf8 scripts/context-memory.py search --project contract-research --query "Core200 人审"`。默认关键词检索不返回 `kind=project`；知道项目后再加 `--project`，用 `show` 选中条目并读取目标正文的相关小节。旧记录用 `history --id <旧ID>`，不作为当前指令。

本轮补充（2026-10-16）：合同研究按对象读取[Core200构造/版本追溯](core200-provenance.md)（历史73/127、88/112与本地正式冻结89/111；远端镜像未同步）、[2026-10-12中文稿定位](contractfill-zh-20261012.md)、[2026-10-10开题报告约定](opening-report-20261010.md)。旧人审缺口和各次任务边界继续保留；后两份不会自动覆盖新稿。

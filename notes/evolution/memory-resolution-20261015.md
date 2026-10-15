# 记忆落地与46条候选处理结果

本轮把历史候选转成可按任务使用的记忆，并实现合并、替代、归档、舍弃和受保护回滚。处理的是现有46条候选，没有另导入新批对话。原始日志与敏感内容只留本地。最终语义质量由用户评估。

| 去向 | 候选条数 | 实际结果 |
|---|---:|---|
| 可用记忆 | 23 | 合并为19条：18条非敏感记忆、1条敏感主题仅本地 |
| Skill | 11 | 归入3个Skill；9条确认已有覆盖，2条补充或细化原指导 |
| 长期规则 | 9 | 新增2条；另7条已被3项核心规则覆盖 |
| 舍弃 | 3 | 关闭原候选，保留原因和历史证据 |

每一条的理由和目标见 [46条完整去向](../candidate-dispositions.md)。原候选保留原文供审计，不能再把复合claim整条当作现行指令。

## 本次新增的两条长期规则

1. **编辑已有材料时保留约定风格（005）**：沿用用户认可的结构和风格；文字修改不自动授权更换整套布局。当前要求重做时按新要求执行。证据来自不同简历与专利任务。
2. **按约定范围说明验收结果（020）**：用户指定最终验收集合时，用该集合判断整体完成，报告已测与未测范围。单例通过只证明单例；普通开发仍采用最小充分检查。证据分别来自Demo和科研任务。

7条已有覆盖为：011/024/035/046合并到沟通规则；015/040合并到委派规则；022由授权内自主执行规则覆盖。它们不计作本次新增。

## 19条可用记忆

可用意味着可以指导相关任务或提供明确的核查线索；带待核状态的内容不能直接当成已经证明的事实。项目记忆保留历史范围，重用时核对当前项目协议和状态。

| 记忆 | 对应候选 | 正文 |
|---|---|---|
| 浏览器填表项目的执行与迭代约定 | 038/039/042/045 | [查看](../../contexts/memory/items/autofill.execution-method.md) |
| 自动填表的错误填写指标 | 043 | [查看](../../contexts/memory/items/autofill.safety-target.md) |
| DemoPilot 的数据与失败记录 | 021 | [查看](../../contexts/memory/items/demopilot.acceptance.md) |
| 陌生插件的逐步引导 | 010 | [查看](../../contexts/memory/items/learning.plugin-guidance.md) |
| 大题库按知识点去重 | 028 | [查看](../../contexts/memory/items/learning.question-dedup.md) |
| 个人材料的项目核验任务 | 026 | 仅本机可用，正文不入Git |
| 迁移后清理旧目录的检查清单 | 029 | [查看](../../contexts/memory/items/migration.old-directory-checklist.md) |
| 新产品原型的可调整计划 | 014 | [查看](../../contexts/memory/items/project.adjustable-plan.md) |
| RAGSystem 的历史执行契约 | 009 | [查看](../../contexts/memory/items/remote.rag-execution-contract.md) |
| 一次服务器与本机浏览器分工 | 044 | [查看](../../contexts/memory/items/remote.server-browser-topology.md) |
| JEV 对照组与输入协议 | 034 | [查看](../../contexts/memory/items/research.comparison-protocol.md) |
| Core200 用途与人审事实的待核边界 | 033 | [查看](../../contexts/memory/items/research.core200-status.md) |
| 研究材料与标签缺口核对 | 023 | [查看](../../contexts/memory/items/research.data-audit-task.md) |
| Benchmark 逐题人工审核约定 | 031 | [查看](../../contexts/memory/items/research.human-review.md) |
| 特定论文的局部修改约定 | 032 | [查看](../../contexts/memory/items/research.localized-paper-edits.md) |
| 论文同步要求的实际时间线 | 017 | [查看](../../contexts/memory/items/research.paper-sync-current.md) |
| 科研启动与小批实验约定 | 016/041 | [查看](../../contexts/memory/items/research.startup-protocol.md) |
| 个人 Skill 的触发期望 | 007 | [查看](../../contexts/memory/items/skills.passive-routing.md) |
| 任务图产品的设计选择 | 037 | [查看](../../contexts/memory/items/taskgraph.project-design.md) |

## Skill的实际吸收

- **专利 Skill：001/003/004/012/013。** 已有步骤清单、模板与事实隔离、实施步骤直接动作、格式及渲染检查。本次把完整运行时包纳入统一仓库；长正文完整移到支持参考，入口保持短。
- **最小验证 Skill：008。** 原已覆盖，完整包纳入统一维护源，没有重复增加一条同义个人规则。
- **academic-write：006/018/019/030/036。** 保留论文类型与贡献层级指导，补充“决策节点不等于已证实机制”及“用户陈述/写作要求不等于已核实人审事实”两处指导。
- 共同步4个完整包到运行时：以上3个，加personal-context路由Skill；逐文件内容已核对一致。

## 舍弃的三条

- **002**：按会话ID核查后仍未定位原线程；不能据此设立所有Skill修改前都要再次审批的全局要求。
- **025**：复合主张来自存在矛盾且敏感的材料，不能选择性拼成稳定偏好；不删除本地原始证据。026中明确的独立任务要求已收窄为仅本地记忆。
- **027**：三个来源都是自动exec的Builder模板，不能算三次独立个人表达。Demo项目的有效要求从021的直接用户来源保留。

## 合并、替代与淘汰怎样运行

- **合并**：保留源证据与候选ID的并集，重复条目退出检索；本轮真实合并了两份委派记录。
- **替代**：新解释成为活跃条目，旧解释保留版本、原因和去向。C017首轮把两条指令时间写反；核实原消息后修正为10月4日指定更新ICML稿、10月6日随后只推进工程且不自动同步。两版旧摘要都退出检索。
- **归档/舍弃**：不再作为活跃指令，保留审计记录。明确设置有效期的临时记忆到期即不进入检索，maintain --apply会归档；稳定偏好到复核日期只提醒检查。
- **回滚**：恢复该次写入的原文件；若这些文件后来被修改，拒绝覆盖，先处理冲突。仅记忆写入路径可回滚，不自动重写核心或其他Skill。
- **触发**：每次用户请求Context进化先运行maintain；没有配置后台定时任务。三个月的复用价值判断没有被做成统一删除计时器。

## 以后怎么按需加载

每次会话只读一次四份核心文件。INDEX按实际任务触发检索，即使用户没有说“查记忆”。检索只返回少量标题与范围，再show选中条目的内容、条件和待核状态；需要核查出处时再用--evidence或读对应叶子文件。

| 当前任务 | 加载与使用 | 检索和选中正文tokens |
|---|---|---:|
| 修改已有简历 | documents.preserve-style：保留模板和风格；个人经历另核验 | 371 |
| 继续Core200人审 | core200-status + human-review：先查台账，中文逐题，不把待核人审流程写成事实 | 820 |
| 迁移后清理旧目录 | old-directory-checklist：路径引用、文件哈希、归档，最后核对本次删除授权 | 575 |
| 恢复任务图产品 | taskgraph.project-design：使用该产品选定的运行历史、协议和混合验收设计 | 762 |
| 继续论文与工程同步 | paper-sync-current：按真实时间线和当前范围判断，不自动延续旧授权 | 647 |

当前本机核心从1,917变为1,931 tokens；新增的任务路由保持在2,000预算内。记忆入口340、learned入口135 tokens。上表只计实际CLI返回的检索结果与选中正文，不含核心、第一次读入口、平台提示、工具、聊天历史或生成成本，不是本轮总开销或计费。入口已读后无需重复。

```powershell
python -X utf8 D:/worker/personal-context/scripts/context-memory.py search --query "论文 人工审核" --project contract-research
python -X utf8 D:/worker/personal-context/scripts/context-memory.py show --id research.core200-status
python -X utf8 D:/worker/personal-context/scripts/context-memory.py maintain
```

普通任务会由Agent完成以上路由，用户无需手工运行命令。需要本人敏感材料时加--include-local，只在本机使用。与个人项目无关的行星问题未命中任何记忆。

## 验证和实际边界

58处原始父对话来源经过文件哈希、真实用户消息和精确行号检查。8个记忆测试方法与1个覆盖测试方法通过；来源检查另加入时间伪造的定向回归。一次独立的只读使用检查用4次搜索、4次精确读取检验了简历、人审、迁移及无关任务；没有进行全量独立提炼复核。中文乱码问题已修复并以强制cp936输出环境验证。

五个真实检索场景、一个无关负例、私有存储隔离、46条完整去向、运行时同步和既有用户改动保护均已核对。源码与规则已可日常试用；这些功能检查不证明所有未来任务都一定检索正确，也没有重新核实历史实验或人审结果。本轮发现并修正时间线错误，说明提炼判断仍需要事实边界和可纠正机制。

证据：[validation.json](../../docs/memory-lifecycle/validation.json)、[loading.json](../../docs/memory-lifecycle/loading.json)、[budget-final.json](../../docs/memory-lifecycle/budget-final.json)、[forward-use.json](../../docs/memory-lifecycle/forward-use.json)、[时间线修正](../../docs/memory-lifecycle/chronology-correction.json)。执行问题及解法见 [T36–T39](../../docs/evolution/TROUBLESHOOTING.md)。

本轮保留了原先未提交的habits/communication.md改动；它不属于本次提交。上述核心大小按本机现有文件计量。用户最终验收：待评估。

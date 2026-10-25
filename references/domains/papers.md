# 论文经验：按当前任务读取

适用选题、研究规划、文献、实验与评估、写作及审稿。分组维持选题与贡献、文献、实验与评估、写作与审稿；下表仅列任务触发条件，不增加细分目录。先匹配本次任务，只读相关条目；个人沟通要求复用核心，不读取整套科研Skill。项目名称仅用于定位必要材料，不作为经验主分类。

| 当前任务 | 经验或工作流入口 | 继续深入的条件 |
|---|---|---|
| 凝练科研问题、构思方法、比较或拆分技术方案 | [问题→多方案→自评→取舍→拆分交付](../../contexts/memory/items/research.problem-first-proposals-v2.md) | 按当前阶段使用输入输出和判断条件；只在涉及复杂机制必要性时读下一条，novelty 核查另读相应条目；不因构思自动启动实验 |
| 新增复杂机制的必要性、与简单方法并排比较 | [具体案例中的必要性检查](../../contexts/memory/items/research.mechanism-necessity-check.md) | 复用先推荐后撤回的过程教训；未显示额外作用时保留待证，不把纸面推演或助手报告当算法实测 |
| idea构思、novelty、贡献定位与审核衔接 | [优先发展并沿用贡献标准](../../contexts/memory/items/research.idea-development-novelty-v2.md) | 需要判断新颖性时按匹配科研Skill核查近邻；明确研究取舍时再读[公理入口](../../habits/axioms/INDEX.md) |
| 已有成果重新定位、按专硕目标规划 | [比较主线并校准当前目标](../../contexts/memory/items/research.framing-collaboration-v3.md) | 只核对支撑当前定位的材料；该条不降低其他投稿任务的标准 |
| 文献调研 | [deep-research](../../skills/deep-research/SKILL.md) | 按其路由读取必要方法与来源，不默认加载写作和实验执行流程 |
| 实验设计、结果解释与证据核查 | 匹配当前可用的科研Skill；论文写作中的证据与因果边界见[学术写作入口](../../contexts/memory/items/skill.academic-writing-entry.md) | 涉及具体数据、标签或协议时再核对对应版本；设计讨论不自动授权实验 |
| 核心结论准备确定、主线实质修改后、重要版本交付前 | [论文评审 Agent](../../skills/paper-review-agent/SKILL.md) | 主智能体在给出最终判断或交付前主动匹配；命中且有可定位材料时按 Skill 派遣真实子智能体，无需用户提及审稿或委派；同材料同问题复用已有意见，普通文字处理不触发 |
| 标签/评分改变后的复评 | [版本对齐→有效预测盘点→分层重评](../../contexts/memory/items/research.reuse-predictions-before-rerun-v3.md) | 区分行数、唯一题数、有效回答和加载错误；机械重算与语义重审分别安排，不把旧预测或盘点完成当作新复评结果 |
| 模型或判别模块的效率比较 | [对齐被测任务和计时阶段](../../contexts/memory/items/evaluation.match-measurement-stage.md) | 仅用于该条范围内的速度问题，不把旧测量当当前结果 |
| 本人逐项审查研究样本 | [说明对象、工作量和收益](../../contexts/memory/items/research.chinese-item-review-v3.md) | 需要本人参与时适用；不自动要求所有研究都人工审核 |
| 子Agent复核、Agent as Judge、与单次API比较 | [复核与判别框架](../skills/agent-review-and-api-evaluation.md) | 依其要求显式交接相关规则并核对读取回执；具体项目协议另按身份加载 |
| 整理、局部改写与实验部分写作 | [范文功能与改写蓝图](../../contexts/memory/items/research.reference-guided-rewriting.md)；实质写作匹配[academic-write](../../skills/academic-write/SKILL.md) | 只读取批准章节、所需结果和范文；简单文字修正不默认加载完整写作流程 |
| 学习独立审查论文 | [本人自查教学](../../contexts/memory/items/research.self-review-coaching.md) | 用户明确要求学习时使用；普通评审匹配当前可用评审Skill |
| 核查研究进度或实验缺口 | 按[项目资料入口](../projects/index.md)定位当前项目及权威索引 | 先确认目标和版本，只读所需完成证据；没找到不等于没做，不因查进度自动启动实验 |

查新增经验时，用实际任务词从[记忆入口](../../contexts/memory/INDEX.md)检索；只有需要项目事实才加项目限定。论文调用API做评测仍属于本领域，接口鉴权/通道故障才补读后端排障入口。需求、PRD、模块设计和Java/Go等标签不在此扩展成目录。

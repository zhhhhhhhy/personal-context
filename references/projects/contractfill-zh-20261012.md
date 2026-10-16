# ContractFill：2026-10-12中文稿约定

项目键 `contract-research`；来源 `01a12dfc-1aab-7101-bf6d-c2758be02026`。仅继续对应稿件时使用；不把这版论文目标当作个人长期研究取舍。

用户指定`C:/Users/郑惠宇/OneDrive/Desktop/icml_chinese`，纠正此前误评英文稿，要求先建立AGENTS.md和中英文索引，再以Supervisor-Skills评审中文稿。评审范围包括选题/idea、写作、实验、数据集、指标；后续重点为创新性、结果、方法设计和实验。原摘要修改只涉及中文，标题也需随定位核对；不沿用为未来稿件的永久修改范围。

用户明确认可该版为**Benchmark / Evaluation paper**。主要贡献为ContractFill的任务定义、数据构造和字段级联合评测；回答系统实验为次，固定生成器前JEV-A gate是说明routing与insufficient-evidence false fill收益边界的案例。固定可见证据下用FILL/NEEDS_REVIEW决策，并联合检查动作、值、必要内容完整性及实际引用支持。

该版不得把coverage–synthesis mismatch当成Qwen3-4B已证明的内部机制，不把JEV-A当完整JEV系统，不声称gate改善充足证据值生成，或推广到未见合同、其他字段、端到端检索、真实企业材料。以上是用户采纳的写作边界，不是本轮复核过的实验结论。

2026-10-16只读核对：该目录当前`AGENTS.md`仍把`paper_zh.tex`/`paper_zh.pdf`列为中文主稿，`paper.tex`/`paper.pdf`为较早英文稿，明确两种语言未同步；其定位仍为Benchmark/Evaluation。检查的是索引文件，未重新编译或核验正文与PDF一致性。再次继续时先读当前索引，确认目标文件与版本；不要凭不带`_zh`的文件名猜“最新”。

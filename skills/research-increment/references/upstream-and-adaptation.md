# 来源与适配边界

2026-10-28 只读核查 SakanaAI/AI-Scientist-v3，固定提交 `df8313889a004f8a44a472e19a833cd547bb828a`。本 Skill 是原创的流程适配说明，没有复制上游执行脚本、安装依赖或提供其 CLI。科研效果未由静态核查证明。

## 借鉴的原生机制

- [create-idea/SKILL.md](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/agents/skills/create-idea/SKILL.md)：目标、rubrics 和历史输入，产出一个 hypothesis、implementation_plan 与相互一致的验收记录。
- [idea prompt](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/prompts/idea.md)：沿用既有观测、接口、失败与未知；构思和执行分开。
- [memory-log](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/agents/skills/memory-log/SKILL.md)：按证据记录尝试，只在有意义的变化下调整结论。
- [campaign loop](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/src/investigation/campaign_loop.py)：基于实际验收与任务指标选择最佳程序；数值晋级不是论文创新判断。

## 本地新增及改动

加入实验前的最近邻方法核查、强简单基线的同例比较、替代解释、贡献知识状态、语义重复辨别与无合格候选终点；接入已有审稿收敛流程。允许用户选择范围与只读讨论，取消原生“每轮必须产出一个可执行 idea、不得交互”的要求。

已查上游构思入口未提供明确文献新颖性 gate；文献引用 Skill 在 paper 阶段。不能把这些本地适配归功于上游原生能力，也不能把讨论完成说成已经执行了代码、消融、封存评测或端到端论文生产。

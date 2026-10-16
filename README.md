# personal-context

个人上下文仓库：积累与 AI 协作时的个人 context，实现按需存取、渐进式披露。

## 为什么

模型能力在不断进步，但我们的上下文并没有。每个人都有自己的行为准则、使用习惯、思考方式和技术沉淀——这些构成了"个人上下文"。把它们结构化地积累下来，AI 才能更懂你，协作才能更高效。

> 相关思考：[模型在进步，上下文却没有](https://zhhhhhhhy.github.io/homepage/posts/ai-context.html)

## 包含什么

```
personal-context/
├── README.md           # 本文件
├── profile.md          # 个人画像：身份、研究方向、技术栈
├── skills/             # 可复用的 skill 定义与使用说明
├── notes/              # 工作笔记、思考记录
├── habits/             # 行为准则、使用习惯、偏好
└── references/         # 参考资料与外部 context
```

## 如何使用

- **渐进式披露**：不需要一次性把所有 context 塞给 AI，按任务需要按需取用。
- **持续维护**：context 是活的，每次协作后有价值的沉淀都应该回流到这里。
- **结构化优先**：每一份 context 都应该有明确的主题和用途，方便检索和引用。
- **受控自进化**：围绕真实任务观察新要求与经验，对照相关已有内容，再校验写入或合并。明确的一次项目约定即可成为有范围的可用记忆；没有新价值就不写。历史对话批量提炼只在明确要求时开展。

## 关于我

郑惠宇（Huiyu Zheng）· 计算机科学方向研究生，聚焦 RAG 与 AI Agent。

- 博客：https://zhhhhhhhy.github.io/homepage/
- GitHub：https://github.com/zhhhhhhhy

## 当前工作结构

```text
AGENTS.md              # 入口路由，只负责告诉 AI 去哪里找内容
INDEX.md               # 任务类型到 Context 文件的映射
profile.md             # 当前个人画像草稿
habits/                # 沟通偏好和长期判断 baseline
skills/                # 可复用的 Context/工作流入口
notes/                 # 历史观察、候选去向和工作笔记，按需追溯
contexts/memory/       # 有范围的可用记忆、项目资料与检索入口
references/            # 对话索引、项目索引、个人画像和导入资料
scripts/               # 将仓库中的 Skill 同步到 Codex 运行时
```

核心会话规则位于 `rules/SOUL.md`、`profile.md`、`habits/communication.md` 和 `INDEX.md`。如果希望它们在每个 Codex 会话进入路由，可运行 `scripts/install-context-router.ps1`；脚本会在覆盖已有全局入口前停止，使用 `-Force` 才会备份并替换。

可用记忆从 `contexts/memory/INDEX.md` 按任务检索；长期规则见 `habits/learned.md`。46条历史候选的去向见 `notes/candidate-dispositions.md`，原文只供追溯。核心规则与权限仍由用户决定。

## Skill 库

原 `zhy-private-skill` 仓库中的 `academic-write`、`deep-research`、`grill-me` 和 `grilling` 已迁入本仓库的 `skills/`。本仓库现在是个人 Context 和个人 Skill 的唯一维护入口；旧仓库保留为历史副本，不再继续维护。

Skill 的完整说明仍按目录独立维护。需要让本机 Codex 使用最新版本时，运行 `scripts/sync-skills.ps1`；脚本只复制更新，不删除运行时已有内容。

## 日常加载和维护

`rules/CONTEXT_LOADING.md` 规定“短入口 → 相关条目 → 必要证据”的读取方式。核心读一次；详细 Skill 和项目资料只在相关任务中加载，历史材料不默认读取。Skill 同步只复制所选包，不运行预算或成本检查。

`context-budget.py`、`context-meter.py`、既有预算配置和历轮报告保留为手动诊断与历史资料。只有明确请求对应专项任务时使用，不是日常记忆更新的前置条件；本次不调整既有阈值，也不继续成本实验。

## Context evolution

`docs/evolution/POLICY.md` 定义最小闭环：**加载相关记忆 → 完成真实任务 → 观察有复用价值的信息 → 对照已有内容 → 校验写入 → 后续任务使用或淘汰**。用户已授权非敏感、可撤回的记忆维护；核心规则、权限和 Skill 修改仍需当前相应任务，不由自动写入器完成。

例如：`python -X utf8 scripts/context-memory.py search --query "文档 风格"`，再用 `show --id documents.preserve-style` 读取命中条目。继续 Core200 时先核对项目，再用 `search --project contract-research --query "Core200 人审"` 和 `show --id project.core200-provenance-v5`。项目资料退出默认关键词检索；项目键见 `references/projects/index.md`。

有值得保存的新内容时才读 `references/skills/personal-context-memory.md`，复用现有 `snapshot`、本地来源清单与变更计划、`validate/apply` 和受保护回滚。无需批量 prepare、观察账本、评测分区、全量复核或每次全库 maintain。原始日志和敏感证据只留本地；敏感摘要未经明确确认不推送 GitHub；不保存凭据，没有后台定时任务。

重复内容合并；新约定明确替代旧约定时保留版本；失效项目约定归档并退出默认检索，仍有效的条件先保存到对应项目。稳定偏好不因年龄自动删除，复核日期只提醒，只有明确有效期的临时记忆才会过期。平时只维护相关条目；全库 `maintain` 仅在明确要求维护时使用。

旧19条整理、46条候选去向和历轮实验保留追溯，不重新当作积压任务。只有明确要求历史导入时，才读 `references/skills/personal-context-evolution.md` 并使用现有批量工具。

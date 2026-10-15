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
- **受控自进化**：用户授权后，可从限定时间窗的本地对话中提炼低风险经验；Observer 只记录，Reflector 只生成候选，脚本负责校验、应用和回滚。

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
notes/                 # 观察记录和候选规则
references/            # 对话索引、项目索引、个人画像和导入资料
scripts/               # 将仓库中的 Skill 同步到 Codex 运行时
```

核心会话规则位于 `rules/SOUL.md`、`profile.md`、`habits/communication.md` 和 `INDEX.md`。如果希望它们在每个 Codex 会话进入路由，可运行 `scripts/install-context-router.ps1`；脚本会在覆盖已有全局入口前停止，使用 `-Force` 才会备份并替换。

长期规则与候选规则分开维护：`notes/candidates.md` 是历史候选的主题入口。低风险经验按 `docs/evolution/POLICY.md` 校验后应用，核心规则与权限仍由用户决定。

## Skill 库

原 `zhy-private-skill` 仓库中的 `academic-write`、`deep-research`、`grill-me` 和 `grilling` 已迁入本仓库的 `skills/`。本仓库现在是个人 Context 和个人 Skill 的唯一维护入口；旧仓库保留为历史副本，不再继续维护。

Skill 的完整说明仍按目录独立维护。需要让本机 Codex 使用最新版本时，运行 `scripts/sync-skills.ps1`；脚本只复制更新，不删除运行时已有内容。

## 加载预算

`rules/CONTEXT_LOADING.md` 规定“短入口 → 当前主题或阶段 → 必要证据”的读取方式。四份核心合计不超过 2,000 tokens，每份 Skill 入口不超过 1,000；历史候选按主题展开。维护后运行 `python scripts/context-budget.py`，同步 Skill 前也会检查预算。详细流程和历史归档只在当前任务需要时读取。

预算计量需要当前 Python 环境安装 `tiktoken`；缺少该依赖时检查会失败，不用字符数代替 token 数。测量口径和变更结果见 `docs/context-loading/REPORT.md`。

## Context evolution

`docs/evolution/POLICY.md` 定义 Observer → Reflector → validate → apply → evaluate → rollback。`scripts/context-evolution.py` 负责选择未处理父对话、冻结训练/评估分区、调用脱敏提取器、检查证据和敏感性、原子更新 `habits/learned.*`，并保留本地回滚快照。原始日志、完整证据和敏感主题不进入 GitHub。

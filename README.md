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

长期规则与候选规则分开维护：对话先进入 `notes/observations.md`，经过证据和人工确认后才进入 `habits/` 或 `skills/`。

## Skill 库

原 `zhy-private-skill` 仓库中的 `academic-write`、`deep-research`、`grill-me` 和 `grilling` 已迁入本仓库的 `skills/`。本仓库现在是个人 Context 和个人 Skill 的唯一维护入口；旧仓库保留为历史副本，不再继续维护。

Skill 的完整说明仍按目录独立维护。需要让本机 Codex 使用最新版本时，运行 `scripts/sync-skills.ps1`；脚本只复制更新，不删除运行时已有内容。

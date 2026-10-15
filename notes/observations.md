# Observations

本文件只追加观察，不直接存放长期准则。

## Date: 2026-10-14

- 🟡 用户确认参考仓库的初始通用规则可以作为快速启动 baseline。
- 🟡 当前目标是快速构建属于用户自己的 Context，并逐步导入历史对话。
- 🟡 材料型任务应先拆成步骤，并为每一步写清输入、输出和完成标准；来源：对话 `01a0fde7-9236-78c1-9068-6867a4ce6d8e`。
- 🟡 修改已有 Skill 前，先说明当前功能、预期执行方式、拟添加方法、插入位置和预期效果；用户明确要求先讨论，不要立即修改；来源：对话 `01a110c5-38b5-7d41-9a42-b03f9872ab01`。
- 🟡 清理或整理文件时，应先根据参考目录建立保留清单，限定修改范围，再检查最终目录；来源：对话 `01a0fde7-9236-78c1-9068-6867a4ce6d8e`。
- 🟡 本地 Codex 历史需要按 thread ID 去重：当前索引发现 1,397 个线程对应 1,477 个 JSONL 文件，其中 32 个线程有多个文件；来源：本地只读索引 `work/context-import/conversation-index.summary.json`。
- 🟡 历史提炼以 546 个父级对话为主，844 个子线程只补充工作流、执行过程和失败原因；原始日志和敏感主题证据只保留在本机批次工作区；来源：用户在 2026-10-14 的批次边界确认和 `batch-001` 工作记录。
- 🟡 首批 20 个父级对话产生 11 条待审候选；每条候选都保留线程 ID、消息行号、范围、置信度和状态，长期规则尚未晋升；来源：`notes/candidates.md` 与本地 `batch-001.candidates.json`。

- 🟡 第二批继续处理 20 个父级对话，覆盖 9 个归档和 11 个主动线程，保留 3,346 条脱敏消息中的 486 条直接用户消息；来源：本机 `work/context-import/batch-002.evidence.jsonl`。
- 🟡 第二批产生 12 条待审候选，集中在 Agent 上下文契约、实验预检、项目与论文边界、Benchmark 叙事、全量验收、Demo 发布门槛和汇报方式；长期规则仍未晋升。
- 🟡 提炼器新增运行时包裹过滤，并修正中文相邻凭据的脱敏边界；第二批脱敏证据未检测到秘密样式值，原始日志保持只读。

- 🟡 第三批继续处理 20 个父级对话，主动与归档线程各 10 个，保留 1,491 条脱敏消息中的 289 条直接用户消息；来源：本机 `work/context-import/batch-003.evidence.jsonl`。
- 🟡 第三批产生 11 条待审候选，新增题库分批去重、远程清理门槛、固定评测集与开发集边界、实验重复运行和学术小步修改等主题；长期规则仍未晋升。

- 🟡 第四批继续处理 20 个父级对话，覆盖 7 个归档和 13 个主动线程，保留 935 条脱敏消息中的 172 条直接用户消息；来源：本机 `work/context-import/batch-004.evidence.jsonl`。
- 🟡 第四批产生 10 条待审候选，补充任务图可观测性、需求与 SDD 拆解、迭代失败台账、Goal Prompt 门槛、主 Agent 分发边界和跨环境验收等主题；长期规则仍未晋升。
- Context evolution `pilot-20261014-v1` processed 12 training roots and deferred all 3 proposed learned rules after conflict and independent quality review; human acceptance pending.
- Context evolution `pilot-20261014-v1` applied 0 low-risk rule(s); human acceptance pending; detailed evidence is local.
- Context evolution `round-002-20261014` applied 0 low-risk rule(s); human acceptance pending; detailed evidence is local.
- Context evolution `round-003-20261015` applied 0 low-risk rule(s); human acceptance pending; detailed evidence is local.
- Context evolution `round-004-20261015` applied 0 low-risk rule(s); human acceptance pending; detailed evidence is local.

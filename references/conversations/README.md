# Conversation Import

先建立索引，再按批次提炼，不要一次把全部历史对话塞进 Context。

`manifest.jsonl` 每行记录一条对话的元数据。优先处理用户纠正、重要决策、失败修复、重复工作流和最终验收记录。

## Evidence boundary

- `manifest.jsonl` 和 `batches/*.jsonl` 只保存去敏后的线程元数据；不把完整 Codex JSONL 复制进仓库。
- 原始会话文件、批次证据包和含敏感主题的候选暂存在本机工作区，默认不推送 GitHub。
- 父级对话中的明确用户表达是个人偏好的主要证据；子线程只补充工作流、执行过程和失败原因。
- 每条候选规则必须保留线程 ID、消息行号、范围、置信度和人工处理状态；长期规则需要单独批量审核后才能晋升。
- 当前已登记批次：`2026-10-14-batch-001`、`2026-10-14-batch-002`、`2026-10-14-batch-003`、`2026-10-14-batch-004`；批次证据包均留在本机工作区。

## Context evolution pilot

新的有限批次使用 `scripts/context-evolution.py prepare` 创建本地训练/评估分区。它会排除已经登记的批次，并在读取正文前冻结评估对话。语义提炼必须只使用 `evidence.train.jsonl`；`evidence.eval.jsonl` 只能用于完成后的独立检查。应用路径只允许写入 `habits/learned.*` 和去敏审计指针，异常时使用本地回滚快照。

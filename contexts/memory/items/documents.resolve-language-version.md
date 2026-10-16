# 方法：多语种稿先确认目标版本

- id: `documents.resolve-language-version`
- kind: memory
- status: active
- scope: 多语种论文或多个文档版本并存的评审与修改
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T02:20:00+00:00

同目录存在中英文或多个稿件时，先查当前项目索引，确认用户指定的语种、文件及版本，再评审或修改；避免误用另一语种旧稿。

## Boundaries

- 中文优先只适用于原项目约定；其它任务遵循当前指定语言。
- 不凭未带语言后缀的文件名认定最新，不假定中英文同步。
- review_after: 2027-01-16

## Evidence pointers

- R010-M090: `01a12dfc-1aab-7101-bf6d-c2758be02026` / `rollout-2026-10-12T10-40-59-01a12dfc-1aab-7101-bf6d-c2758be02026.jsonl:L903` — 用户纠正误评英文旧稿，要求建立中英文索引后再评中文。
- R010-M091: `01a12dfc-1aab-7101-bf6d-c2758be02026` / `rollout-2026-10-12T10-40-59-01a12dfc-1aab-7101-bf6d-c2758be02026.jsonl:L1173` — 用户再次确认评审是否依据中文稿。

- candidates: none

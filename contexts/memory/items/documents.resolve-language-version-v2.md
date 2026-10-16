# 多稿件编辑：确认语种与版本

- id: `documents.resolve-language-version-v2`
- kind: memory
- status: active
- scope: 多语种或多个文档版本并存的评审与修改
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

中英文或多个稿件并存时，先通过已有索引定位当前指定的语种、文件和版本，再评审或修改，避免误用另一语种旧稿。

## Boundaries

- 某项目的中文优先约定不推广到其他任务；当前指定语言优先。
- 不凭文件名认定最新，不假定不同语种同步；没有索引时也须确认目标，不强制新建一套管理流程。
- review_after: 2027-01-16

## Evidence pointers

- R010-M090: `01a12dfc-1aab-7101-bf6d-c2758be02026` / `rollout-2026-10-12T10-40-59-01a12dfc-1aab-7101-bf6d-c2758be02026.jsonl:L903` — 用户纠正误评英文旧稿，要求建立中英文索引后再评中文。
- R010-M091: `01a12dfc-1aab-7101-bf6d-c2758be02026` / `rollout-2026-10-12T10-40-59-01a12dfc-1aab-7101-bf6d-c2758be02026.jsonl:L1173` — 用户再次确认评审是否依据中文稿。

- candidates: none

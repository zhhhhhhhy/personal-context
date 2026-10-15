## Benchmark-first writing rules

For a benchmark paper, the normal narrative is:

`practical need -> task boundary -> evaluation gap -> benchmark construction -> joint metrics -> diagnostic experiments -> findings`

The benchmark must remain meaningful if a particular evaluated method is removed. The introduction should describe the method only as much as needed to explain what the benchmark tests. A method name may appear in the experiment question or result paragraph; its architecture, training history, and unmeasured modules belong later or outside the main paper.

Define the common boundary that makes a field complete. If a field requires several related facts, evaluate all of them together. Keep separate measures for automatic completion, appropriate review, false filling, and over-review when the task contains an abstain or review action.

## Content filtering

Use minimal sufficient detail. Omit internal identifiers and process traces from the main paper by default, including hashes, internal version strings, study IDs, file paths, experiment directories, commit-like labels, draft status, task queues, and application TODOs. A data-construction rule may be described at the level needed for reproducibility without exposing internal bookkeeping; for example, write “remove exact duplicates” rather than naming a checksum algorithm unless the algorithm itself affects the scientific result.

Replace project-status language with scientific scope:

- “冻结实验” -> “本文评测范围” or “在固定证据条件下”;
- “已完成的模块” -> “本文采用的实现”;
- “下一步/后续完成” -> “本文未评估” or “仍需在独立设置中检验”;
- “当前稿件/本轮结果” -> “本文结果” or a named experiment.

“固定证据” is a methodological condition and may remain. “冻结版本” is usually project bookkeeping and should be removed from the paper.

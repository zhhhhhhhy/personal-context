# Classified evolution round 002

User request: complete the next evolution round with category comparisons. State: [WORKFLOW_STATE.md](WORKFLOW_STATE.md).

| Task | Owner | Evidence / completion |
|---|---|---|
| Metadata selection | Script + parent AI | Exclude the prior 95 roots, automated tasks and empty chats; freeze 4 training roots and 1 evaluation root per category |
| Observation and reflection | Parent AI | Read training messages only; count independent direct-user evidence; compare core, relevant Skills and old candidates |
| Publication boundary | Script | Validate input hashes, source roles/locations, category partitions, sensitivity and base state; reread learned output |
| Fresh response comparison | Independent forward-test agents | Same sanitized held-out task snapshots and existing task Skills; frozen baseline versus candidate Context; no original-task execution |
| Judgment | Parent AI, then user | Category-specific effects, counterexamples, overlap, age and sample-size limits; human acceptance remains pending |

The recent unused corpus is dominated by automated execution tasks and article questions. This round therefore uses a metadata-selected historical sample from April through October 2026, not all activity in one week. Related project/conversation families stay in one partition; multiple sessions of the same experiment do not automatically count as independent preferences. Titles determine initial categories and are not preference evidence.

Freeze selection before reading message bodies. Freeze candidate wording before opening evaluation messages. Evaluation uses compact, sanitized task snapshots and newly generated first responses, not full execution of past tasks or reuse of old assistant answers. Both conditions receive the same relevant current Skills. A useful response difference does not prove long-term benefit or user acceptance. Ties, pre-existing Skill coverage and insufficient evidence are valid outcomes.

Only nonsensitive rules and summary reports may enter Git. Source logs, quotations, detailed family analysis, response prompts and test outputs remain under the ignored `.local/context-evolution/round-002-20261014` directory. The final report includes safe examples for user review. No scheduler or unrelated Skill is changed.

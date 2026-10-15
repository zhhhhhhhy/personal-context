---
name: personal-context
description: Load personal Context and, when asked to evolve or distill it from conversations, run evidence-based observation, reflection, bounded promotion and evaluation. Do not turn an ordinary task into a history import.
---

# Personal Context Skill

Source of truth: `D:/worker/personal-context` (or the repository containing this source Skill). The installed Skill is a router, not a duplicate memory store.

## Use Context

Read the repository `AGENTS.md` and its four core files once per session. Use `INDEX.md` for relevant details. Read learned rules only in their stated scope; current user instructions outrank historical inferences. Do not load all conversation history.

When maintaining entries, follow `rules/CONTEXT_LOADING.md` and run `scripts/context-budget.py`. Historical candidates start at `notes/candidates.md`; inspect relevant topic pages and search across topics for duplicates before opening more detail.

## Evolve Context when requested

Read `docs/evolution/POLICY.md` and the execution contract at `D:/worker/personal-context/references/skills/personal-context-evolution.md`. The absolute canonical path also works from the installed runtime copy. Use the current Codex session as the semantic engine:

1. Prepare an incremental, redacted local evidence pack with `scripts/context-evolution.py prepare`. Freeze dates and evaluation split before reading content. For category comparisons, use `--partition-manifest`; exclude automated tasks and keep related conversation families in one partition.
2. Observer reads only the training partition, writes local `observations.json`, and records sources, limits and rejected ideas. It does not modify active rules.
3. Reflector compares observations with existing rules and historical candidates, writes local `reflection.json`, merges duplicates and tests conflicting interpretations. Produce zero promotions when evidence is insufficient.
4. Run `validate` then `apply`. The script alone publishes eligible learned rules, a redacted decision log and evidence pointers. Core identity, permissions, sensitive material and raw quotes stay outside automatic publication.
5. Assess evidence fidelity, scope, novelty and usefulness on the frozen evaluation partition. When comparing fresh responses, freeze the baseline and candidate instructions, use the same sanitized cases and relevant Skills in both conditions, and report category-specific differences and limits. Do not tune rules on the holdout. Report model judgment separately from human acceptance. Use `rollback` if the applied batch is unsound.

The user authorized bounded low-risk evolution on 2026-10-14; do not ask again for each eligible rule. Ask only at the actual boundary described in the policy. No background scheduler is installed by invoking this Skill.

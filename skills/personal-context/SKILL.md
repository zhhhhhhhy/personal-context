---
name: personal-context
description: Load personal Context and, when asked to evolve or distill it from conversations, run evidence-based observation, reflection, bounded promotion and evaluation. Do not turn an ordinary task into a history import.
---

# Personal Context Skill

Source of truth: `D:/worker/personal-context` (or the repository containing this source Skill). The installed Skill is a router, not a duplicate memory store.

## Use Context

Read the repository `AGENTS.md` and its four core files once per session. Use `INDEX.md` for relevant details. For related project agreements or corrections, read `contexts/memory/INDEX.md`, search task keywords and show only selected entries. Current user instructions outrank historical memories; pending factual claims remain unverified.

When maintaining entries, follow `rules/CONTEXT_LOADING.md` and run `scripts/context-budget.py`. Historical candidates start at `notes/candidates.md`; inspect relevant topic pages and search across topics for duplicates before opening more detail.

## Evolve Context when requested

Read `docs/evolution/POLICY.md` and the execution contract at `D:/worker/personal-context/references/skills/personal-context-evolution.md`. The absolute canonical path also works from the installed runtime copy. Use the current Codex session as the semantic engine:

1. Prepare an incremental, redacted local evidence pack with `scripts/context-evolution.py prepare`. Freeze dates and evaluation split before reading content. For category comparisons, use `--partition-manifest`; exclude automated tasks and keep related conversation families in one partition.
2. Observer follows the source coverage contract linked from the execution reference: account for every direct training message, split concrete requirements and exceptions, then write local `observations.json` before candidate lookup. Preserve valuable single-task agreements as scoped memory when their meaning is clear.
3. Reflector compares observations with active memory, Skills and historical dispositions. A clear single-project agreement may become usable memory; only general-rule promotion needs repeated independent support. Credit existing coverage instead of leaving duplicate candidates pending.
4. For saving or maintaining memory, read `D:/worker/personal-context/references/skills/personal-context-memory.md`, check `maintain`, and create a local lifecycle plan. Validate and apply with the repository's `scripts/context-memory.py`. It owns merge, replacement, archive/discard, source checks and rollback. Core identity, permissions, sensitive material and raw quotes stay outside automatic publication.
5. Assess evidence fidelity, scope, novelty and task retrieval. Use a frozen evaluation partition when comparing fresh responses; keep baseline conditions matched and report model judgment separately from human acceptance. A saved project agreement does not require an A/B win. Roll back an unsound transaction with the memory CLI.

The user authorized bounded low-risk evolution on 2026-10-14; do not ask again for each eligible rule. Ask only at the actual boundary described in the policy. No background scheduler is installed by invoking this Skill.

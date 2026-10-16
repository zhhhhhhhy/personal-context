# Usable memory and lifecycle contract

Read this only when saving/changing memory or diagnosing retrieval. Ordinary use needs only `contexts/memory/INDEX.md` and selected entries. Current policy: `docs/evolution/POLICY.md`. This is the existing writer contract, not a batch-import or evaluation requirement.

## Update from a real task

1. Use relevant evidence already available in the current task. If nothing has future reuse value, stop without a write. Search only overlapping active entries and related Skill/core coverage; do not load old candidates or all memory.
2. Keep a clear preference, working method or project agreement within its scope. Preserve concrete conditions and unverified facts. Compare actual message dates before deciding that a newer agreement replaces an older one.
3. Take `snapshot` for the current base hash and create a small local plan for only the affected IDs. New evidence needs a local `source_manifest`; `context-evolution.py prepare`, `observations.json`, reflection/coverage ledgers and evaluation partitions are not writer prerequisites.
4. Validate and apply that plan with the commands below. Reread changed entries and check one relevant retrieval. Reuse the transaction ID if a guarded rollback is needed. Do not add a full review, token report or new experiment round.
5. Report the useful memory applied, actual change and pending facts when relevant. Maintain unrelated records only when the user asks or they become relevant in a later task.

## Meaning and use

- `memory`: a concise reusable scenario preference or working method with evidence and scope. Old task quantities stay in its history unless still needed for reuse.
- `project`: one evidenced project agreement or open issue is enough. Keep concrete quantities, conditions, attribution, unknown facts and source version in the project target. A writing request does not prove its requested facts.
- `rule`: a reusable behavior supported by distinct direct human expressions in independent parent conversations and task families. Preserve scope and exceptions. Existing core coverage is recorded as `core`, not counted as a new learned rule.
- `skill`: a receipt pointing to a real canonical Skill or reference. The Skill carries the workflow; the receipt must not create another divergent instruction copy.
- Private themes stay in `.local/context-memory/`. Retrieval requires `--include-local`; only local summaries and original evidence may contain sensitive details.

Search returns bounded routing metadata. Read selected entries with `show`; then use their scope, exceptions, verification label and current user instructions. Project memories describe historical agreements until current files confirm they still apply. Unresolved factual claims are leads to check, never established results.

## Semantic reflection

Reuse already available evidence and source pointers. Check overlapping active memory and relevant Skills/core before writing. Save useful scoped content, credit existing coverage or decline to save it; do not wait for recurrence merely to preserve a clear project agreement. General-rule promotion remains stricter. A task does not need a separate observation ledger or a candidate for every message.

Reflector chooses:

| Operation | Effect |
|---|---|
| `add` | New active scoped memory, rule or coverage receipt |
| `merge` | Union evidence/candidate IDs into an explicit destination; close source entries |
| `replace` | Activate a later interpretation and mark old entries superseded; retain the old claim and source |
| `archive` | Stop ordinary use and retain history; move any still-applicable constraint to its scoped destination before archiving a redundant execution record |
| `discard` | Reject incorrect, unsupported, redundant or non-reusable material; retain the reason |
| `review` | Record a justified recheck and next review date without changing the claim |

Conflicting human preferences require a contextual resolution or explicit new instruction. Age alone never overturns a stable preference. An expired project milestone may become historical rather than false. Do not delete raw source logs.

Before interpreting a later instruction as replacing an earlier one, check the actual message timestamps. Conversation creation dates, candidate numbering and source-map order do not establish message order. For a correction, record which prior interpretation was wrong and retain the source dates.

## Executable boundary

The 2026-10-16 cleanup separates reusable `kind=memory` entries from `kind=project` material. Project records require a project key, `validity=project` and an existing target file. Default keyword search excludes project material; use `--project <key>` after checking identity/version. Explicit `show` may read a selected project record. Project roots, commits and task versions are checked on continuation; an overdue review is not proof that an agreement expired.

Historical candidate dispositions may use `project` for an active project record or `archive` for an archived original. Archiving an execution record does not cancel its still-applicable conditions: preserve those in the matching project target with source dates and verification boundaries first.

`scripts/context-memory.py` reads a local plan. Only memory registries/leaves, learned projections, candidate statuses and the disposition report are writable. Core and Skill edits need current user-directed work and are outside this automatic writer. Transactions and raw source manifests stay local. `habits/learned.json` is a projection, not a second source of truth.

```powershell
python -X utf8 scripts/context-memory.py snapshot
python -X utf8 scripts/context-memory.py validate --plan .local/context-memory/next.plan.json
python -X utf8 scripts/context-memory.py apply --plan .local/context-memory/next.plan.json
python -X utf8 scripts/context-memory.py maintain
python -X utf8 scripts/context-memory.py maintain --apply
python -X utf8 scripts/context-memory.py rollback --transaction <returned-transaction-id>
```

`maintain` lists overdue reviews and explicit temporary expiry; use it for an explicitly requested store-wide maintenance task, not before every save. `maintain --apply` archives all eligible expired temporary entries, so it is not a task-scoped default. For a related stale record, use an explicit operation on its ID. Completing reviews, merging and replacing require semantic decisions with reasons; no scheduler is installed.

Plans require the current `base_sha256`, a reason and operations. `add`, or `merge`/`replace` with a new destination, include a complete record: `id`, `title`, `kind`, `claim`, `scope`, `exceptions`, `tags`, `visibility`, `sensitivity`, `validity`, `verification`, `evidence`, and optionally `project`, `review_after` or `expires_after`. Existing destinations use `into`; sources use `from`. Archive/discard use `ids`. Only temporary records may have an expiry date.

Each new evidence pointer identifies a thread, exact source filename/line, family, source kind, expression hash and brief sanitized support. The local `source_manifest` maps its `ref` to the original file, byte hash and LF line number. The validator checks the actual user role, parent session and exact source expression; compressed `.jsonl.zst` logs are read without altering them. This establishes provenance, not semantic truth. The current session must still check who said what, independence, scope, privacy and contradictions.

For current-task evidence, a small local source manifest is sufficient. Each `ref` maps to `path`, `sha256`, `line`, `thread_id` and `origin=human_parent`. Evidence uses the same `ref`/thread, `source_kind=user_authored`, `family_id`, sanitized `support` and `location=<original-basename-without-.zst>:L<line>`; retain the actual message timestamp when known. `text_sha256` hashes the JSON serialization of the source payload's full `content` value (or `message` fallback), using `ensure_ascii=False, sort_keys=True` and UTF-8, not a normalized plain-text excerpt.

If the current session log is still growing, copy it byte-for-byte to `.local/context-memory/sources/<thread-id>/` under its original basename before computing the manifest hash. Keep the original path/line mapping locally and point validation at the stable copy. Preserve session metadata and LF line offsets; do not export only a rewritten quote. This avoids a changing whole-file hash without importing other conversations or returning the whole log to the model. If the source is unavailable or fails the existing checks, leave a local pending lead rather than fabricate evidence or loosen the validator.

Use `history --id <id> --include-retired` or inspect a local transaction for audit. Rollback refuses when its outputs have been modified since that transaction, preventing accidental reversal of newer work. Do not bypass this by restoring old files by hand.

## Relation to the historical evolution script

`context-evolution.py prepare` and its source/coverage checks remain available only for explicitly requested history import. New memory writes use the lifecycle plan after task-scoped observation/reflection. Legacy `apply`/`rollback` refuse to overwrite an initialized memory store. General-rule checks in the older reflection format do not gate saving scoped memories. Neither an A/B win nor a second unrelated project is required for a clear project agreement. Historical candidate dispositions are read only for relevant provenance, not as a prerequisite for every plan.

Upstream basis: [PRD](https://github.com/grapeot/context-infrastructure/blob/main/periodic_jobs/ai_heartbeat/docs/PRD.md), [SOP](https://github.com/grapeot/context-infrastructure/blob/main/periodic_jobs/ai_heartbeat/docs/KNOWLEDGE_BASE.md), [Reflector](https://github.com/grapeot/context-infrastructure/blob/main/periodic_jobs/ai_heartbeat/src/v0/reflector.py). The three-month reuse criterion is a value judgment, not a universal retention timer.

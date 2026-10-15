# Usable memory and lifecycle contract

Read this only for memory maintenance, candidate resolution, or a retrieval problem. Ordinary tasks use `contexts/memory/INDEX.md` and exact matching entries.

## Meaning and use

- `memory`: one evidenced project agreement or narrow scenario preference is enough. Keep concrete quantities, conditions, attribution, and unknown facts. A writing request does not prove its requested facts.
- `rule`: a reusable behavior supported by distinct direct human expressions in independent parent conversations and task families. Preserve scope and exceptions. Existing core coverage is recorded as `core`, not counted as a new learned rule.
- `skill`: a receipt pointing to a real canonical Skill or reference. The Skill carries the workflow; the receipt must not create another divergent instruction copy.
- Private themes stay in `.local/context-memory/`. Retrieval requires `--include-local`; only local summaries and original evidence may contain sensitive details.

Search returns bounded routing metadata. Read selected entries with `show`; then use their scope, exceptions, verification label and current user instructions. Project memories describe historical agreements until current files confirm they still apply. Unresolved factual claims are leads to check, never established results.

## Semantic reflection

Reuse the already read observations and source pointers. Check overlapping active memory and Skills before writing. Dispose of every useful observation as a scoped memory, Skill/core coverage, a general rule, or a reasoned rejection; do not wait for recurrence merely to preserve a project agreement. General-rule promotion remains stricter.

Reflector chooses:

| Operation | Effect |
|---|---|
| `add` | New active scoped memory, rule or coverage receipt |
| `merge` | Union evidence/candidate IDs into an explicit destination; close source entries |
| `replace` | Activate a later interpretation and mark old entries superseded; retain the old claim and source |
| `archive` | Stop ordinary use, retain audit/history for a completed or expired context |
| `discard` | Reject incorrect, unsupported, redundant or non-reusable material; retain the reason |
| `review` | Record a justified recheck and next review date without changing the claim |

Conflicting human preferences require a contextual resolution or explicit new instruction. Age alone never overturns a stable preference. An expired project milestone may become historical rather than false. Do not delete raw source logs.

Before interpreting a later instruction as replacing an earlier one, check the actual message timestamps. Conversation creation dates, candidate numbering and source-map order do not establish message order. For a correction, record which prior interpretation was wrong and retain the source dates.

## Executable boundary

`scripts/context-memory.py` reads a local plan. Only memory registries/leaves, learned projections, candidate statuses and the disposition report are writable. Core and Skill edits need current user-directed work and are outside this automatic writer. Transactions and raw source manifests stay local. `habits/learned.json` is a projection, not a second source of truth.

```powershell
python -X utf8 scripts/context-memory.py snapshot
python -X utf8 scripts/context-memory.py validate --plan .local/context-memory/next.plan.json
python -X utf8 scripts/context-memory.py apply --plan .local/context-memory/next.plan.json
python -X utf8 scripts/context-memory.py maintain
python -X utf8 scripts/context-memory.py maintain --apply
python -X utf8 scripts/context-memory.py rollback --transaction <returned-transaction-id>
```

`maintain` lists overdue reviews and explicit temporary expiry. `--apply` archives only expired temporary entries. Completing reviews, merging and replacing require semantic decisions with reasons; no scheduler is installed. During each requested evolution run, check maintenance once before adding new content. A weekly run can be scheduled separately when requested.

Plans require the current `base_sha256`, a reason and operations. `add`, or `merge`/`replace` with a new destination, include a complete record: `id`, `title`, `kind`, `claim`, `scope`, `exceptions`, `tags`, `visibility`, `sensitivity`, `validity`, `verification`, `evidence`, and optionally `project`, `review_after` or `expires_after`. Existing destinations use `into`; sources use `from`. Archive/discard use `ids`. Only temporary records may have an expiry date.

Each new evidence pointer identifies a thread, exact source filename/line, family, source kind, expression hash and brief sanitized support. The local `source_manifest` maps its `ref` to the original file, byte hash and LF line number. The validator checks the actual user role, parent session and exact source expression; compressed `.jsonl.zst` logs are read without altering them. This establishes provenance, not semantic truth. The current session must still check who said what, independence, scope, privacy and contradictions.

Use `history --id <id> --include-retired` or inspect a local transaction for audit. Rollback refuses when its outputs have been modified since that transaction, preventing accidental reversal of newer work. Do not bypass this by restoring old files by hand.

## Relation to the historical evolution script

`context-evolution.py prepare` and its source/coverage checks remain available. New memory writes use the lifecycle plan after Observer/Reflector reasoning. Legacy `apply`/`rollback` refuse to overwrite an initialized memory store. General-rule checks in the older reflection format do not gate saving scoped memories. Neither an A/B win nor a second unrelated project is required for a clear project agreement.

Upstream basis: [PRD](https://github.com/grapeot/context-infrastructure/blob/main/periodic_jobs/ai_heartbeat/docs/PRD.md), [SOP](https://github.com/grapeot/context-infrastructure/blob/main/periodic_jobs/ai_heartbeat/docs/KNOWLEDGE_BASE.md), [Reflector](https://github.com/grapeot/context-infrastructure/blob/main/periodic_jobs/ai_heartbeat/src/v0/reflector.py). The three-month reuse criterion is a value judgment, not a universal retention timer.

# Personal Context evolution reference

This repository uses a two-stage semantic process with deterministic controls:

```text
prepare -> evidence.train/eval -> Observer -> reflection.json
       -> validate -> apply -> evaluate -> user acceptance or rollback
```

## Prepare

Use only unused root conversations in a bounded local-date window. Exclude prior selection manifests and reserve the evaluation roots before reading message bodies.

```powershell
$run = 'D:\worker\personal-context\.local\context-evolution\run-YYYYMMDD'
python D:\worker\personal-context\scripts\context-evolution.py prepare `
  --index 'C:\Users\郑惠宇\Documents\Codex\2026-10-14\wo-shi\work\context-import\conversation-index.jsonl' `
  --start 2026-09-28 --end 2026-10-05 --eval-count 3 `
  --exclude-selection 'C:\Users\郑惠宇\Documents\Codex\2026-10-14\wo-shi\work\context-import\batch-001.selection.json' `
  --exclude-selection 'C:\Users\郑惠宇\Documents\Codex\2026-10-14\wo-shi\work\context-import\batch-002.selection.json' `
  --exclude-selection 'C:\Users\郑惠宇\Documents\Codex\2026-10-14\wo-shi\work\context-import\batch-003.selection.json' `
  --exclude-selection 'C:\Users\郑惠宇\Documents\Codex\2026-10-14\wo-shi\work\context-import\batch-004.selection.json' `
  --output $run
```

The command reads raw logs read-only through the existing redacting extractor. It writes no raw evidence into Git.

For classified comparisons, supply `--partition-manifest` with a local JSON list containing `thread_id`, `category`, `family_id`, and `partition` (`train` or `eval`). Select by metadata before reading message bodies, exclude automated worker tasks even if the index calls them roots, and keep each related family in one partition. The date range still applies. Each category must have both train and evaluation roots. `input_hashes.json` freezes selection and evidence files; validation rejects later changes. The default `--message-date-policy strict` excludes missing-timestamp and out-of-window messages.

For a bounded historical import with complete native user messages but missing message dates, explicitly select `--message-date-policy thread-bounded`. An undated direct message is admitted only when its parent's valid creation/update interval lies wholly within the declared window. Keep its timestamp null and record thread-level precision; never manufacture a message date. Known dates still obey the message window. Missing or invalid thread bounds block this fallback. This does not establish which day the user made the statement. Inspect the frozen date-filter counts, and do not use this option to claim a precise weekly sample.

For a fresh response comparison, freeze the candidate wording before opening the evaluation partition. Use identical sanitized case prompts and relevant current Skills in both conditions. Save the frozen baseline and the candidate supplement separately, and generate new responses in isolated evaluation sessions. Assess explicit current-request adherence, evidence grounding, useful next action, and unnecessary constraints. Report ties and regressions by category; do not call model judgments human acceptance or tune candidates using held-out answers.

## Observer and Reflector output

Before candidate lookup, read [the source coverage contract](personal-context-observation.md).
Write and validate the local message-to-unit-to-observation ledger first. New
prepared cohorts require it, and every observation must receive a reflection
disposition. This catches missing bookkeeping, while independent semantic
review checks whether multi-part messages were interpreted completely.

After freezing observations, use [concentrated semantic review](personal-context-review.md)
for risk-directed checking with a low-risk sample and explicit escalation.
Full independent inventories are reserved for a requested comparison or a
discovered coverage failure; do not repeat them by default on every batch.

The current Codex session reads only `evidence.train.jsonl` and writes `reflection.json`. It must distinguish direct user-authored messages from assistant summaries, tool outputs, runtime wrappers and child-thread material. A promotion contains:

```json
{
  "key": "workflow.example",
  "claim": "A narrow, reusable user preference",
  "scope": "When this applies",
  "exceptions": ["When it does not apply"],
  "confidence": "high",
  "sensitivity": "non_sensitive",
  "evidence": [
    {
      "thread_id": "root-thread-id",
      "source_kind": "user_authored",
      "location": "session.jsonl:L123",
      "support": "Short non-sensitive evidence description"
    }
  ]
}
```

The reflection must include `schema_version`, `run_id`, `base_snapshot_sha256`, `conflict_check`, `promotions`, `deferred` and `rejected`. Set `conflict_check.core_checked`, `.learned_checked` and `.candidate_ledger_checked` to true only after inspecting those sources. For candidates, start with `notes/candidates.md`; use `show-candidate --id` for a known ID, otherwise inspect relevant topic pages and search across topics for overlaps. Expand only when needed. The script resolves all candidate IDs without putting every record into the model prompt. Do not include raw quotes, secrets, private topics or evaluation-thread evidence.

Each promotion must also include `candidate_audit`: use `new` with no related IDs only when the candidate ledger has no overlapping rule; use `refine` with one or more existing candidate IDs when the wording narrows, extends or operationalizes an existing candidate. The validator resolves each cited ID and resolves every evidence location to a direct user-authored message in `evidence.train.jsonl`.

The extractor removes AGENTS runtime wrappers and normalizes IDE request wrappers before deduplication. Adopted assistant plans are labelled `user_plan_confirmation`, which records approval of that task but is not evidence of an independently expressed personal preference. Pasted logs, quoted documents and less structured copied material still require semantic review. Promotion validation checks the source filename as well as line, distinct expressions and independent conversation families. `apply` reruns validation against the current reflection, so a formerly passed status cannot bypass checks after an edit.

Record `reinforced` existing rules separately from novel `promotions`. Additional support can be useful even when no new rule is needed. Keep current core and Skill behavior as the baseline; do not weaken it to make a candidate look beneficial.

When the user requests measured loading, use `scripts/context-meter.py` with a
prepared local run and separate arm names. Its bootstrap, training, candidate
search and exact-record commands log the text actually returned, including
repeated payloads. Keep matching evidence and constraints across conditions;
the explicit whole-ledger arm verifies that archived candidate bodies still
match. Report Context and historical-evidence payloads separately from setup,
platform prompts and tool schemas, which this reader does not observe. A reader
log alone does not prove every later tool output was metered.

For recovery from missing logs, API limits, coverage failures or metering
errors, read only the relevant entry in
[the troubleshooting record](../../docs/evolution/TROUBLESHOOTING.md).

## Apply, evaluate, rollback

```powershell
python D:\worker\personal-context\scripts\context-evolution.py validate --run-dir $run
python D:\worker\personal-context\scripts\context-evolution.py apply --run-dir $run
python D:\worker\personal-context\scripts\context-evolution.py status --run-dir $run
# if the applied batch is unsound:
python D:\worker\personal-context\scripts\context-evolution.py rollback --run-dir $run
```

Only `habits/learned.json`, `habits/learned.md`, a redacted `notes/evolution/<run>.md` decision log and an observation pointer are writable by the automatic path. Core rules and Skills require a separate user-directed change.

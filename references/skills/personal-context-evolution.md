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

## Observer and Reflector output

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

The reflection must include `schema_version`, `run_id`, `base_snapshot_sha256`, `conflict_check`, `promotions`, `deferred` and `rejected`. Set `conflict_check.core_checked`, `.learned_checked` and `.candidate_ledger_checked` to true only after actually reading those sources. Do not include raw quotes, secrets, private topics or evaluation-thread evidence.

Each promotion must also include `candidate_audit`: use `new` with no related IDs only when the candidate ledger has no overlapping rule; use `refine` with one or more existing candidate IDs when the wording narrows, extends or operationalizes an existing candidate. The validator resolves each cited ID and resolves every evidence location to a direct user-authored message in `evidence.train.jsonl`.

## Apply, evaluate, rollback

```powershell
python D:\worker\personal-context\scripts\context-evolution.py validate --run-dir $run
python D:\worker\personal-context\scripts\context-evolution.py apply --run-dir $run
python D:\worker\personal-context\scripts\context-evolution.py status --run-dir $run
# if the applied batch is unsound:
python D:\worker\personal-context\scripts\context-evolution.py rollback --run-dir $run
```

Only `habits/learned.json`, `habits/learned.md`, a redacted `notes/evolution/<run>.md` decision log and an observation pointer are writable by the automatic path. Core rules and Skills require a separate user-directed change.

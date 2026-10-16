# Source coverage for Context observation

Use this contract during requested Context evolution. All source excerpts and
coverage ledgers remain in the ignored local run directory.

## Observe before lookup

Prefer `context-review.py --run-dir <run> build-source --page-tokens 6500`,
then `read --file <each returned source_files path> --reader observer`.
Messages use short IDs and share conversation metadata; exact text is unchanged.
Full IDs, filenames and line numbers stay in the frozen local source-map.
Use `expand --draft <draft.json>` to restore the coverage ledger. Do not return
the map or core packet to a role that already has them. Source pages are hashed,
bounded and never truncated; changed pages/maps or source identities are rejected.
The older `context-meter.py ... train` remains available for explicit comparisons,
not the default source reader. Do not use evaluation messages.

For each message, separate concrete requirements, corrections, exceptions,
permissions and project facts. One message can contain several independent
requirements. Keep useful one-off task requirements as observations even when
they cannot support a permanent rule. Identify questions and continuation
messages as such; do not invent a preference to fill a row. Quoted/copied
material still needs semantic exclusion even if the extractor labelled the
message as user-authored.

Write the complete ledger before reading the candidate index, searching old
rules or opening candidate bodies. This prevents familiarity with existing
rules from suppressing new observations. Freeze the ledger hash before
Reflector starts. Later corrections must be explicit revisions, not silent
replacement of measured results.

## Local observations.json

```json
{
  "schema_version": "coverage/1",
  "run_id": "run-YYYYMMDD",
  "source_digest": "from the training reader",
  "messages": [
    {
      "message_id": "from the training reader",
      "units": [
        {
          "id": "U001",
          "quote": "a short exact substring of this message",
          "kind": "task_requirement",
          "claim": "One concrete requirement with its condition",
          "reason": "Why this is relevant; limits or uncertainty",
          "observation_ids": ["O001"]
        }
      ]
    }
  ],
  "observations": [
    {
      "id": "O001",
      "claim": "The observation without added authority or permanence",
      "scope": "Original task or explicitly supported wider scope",
      "source_units": ["U001"]
    }
  ],
  "review": {
    "completeness_reviewed": true,
    "method": "Rechecked every message for additional requirements and exceptions"
  }
}
```

Allowed unit kinds: `preference_signal`, `task_requirement`, `correction`,
`exception`, `project_fact`, `question`, `non_substantive`, `permission_scope`,
`sensitive`. The first four require an observation link. Other kinds may have
no observation with an explicit reason; do not hide a meaningful task
requirement under `question` just because the request is phrased as a question.
Permission and sensitive content never become new automatic authority.

Before freezing, audit every unit with no observation link. A question can
request diagnosis, comparison, capability explanation or object confirmation;
keep that task intent without inventing its answer. If a continuation refers
to missing prior text, preserve the request and the unknown referent. Record
historical permission only as scoped history, never as current authority.
Referenced material may define the object of analysis without becoming the
user's belief. Keep its task-relevant constraints with that attribution.

### Preserve details before judging certainty

Unverified material is still evidence of what must be investigated. For each
task-relevant claim, retain its concrete quantities (including units, ranges
and inclusive/exclusive operators), named objects or reference identifiers,
conditions, alternatives and exceptions. Split independently actionable checks
into separate units. Do not compress a multi-part critique to "verify the
experiment" or drop a proposed branch because it has not been confirmed.

State who said or supplied it and its status in the observation claim:
direct user request, user-reported fact pending verification, quoted feedback,
or unconfirmed proposal. Keep source message/quote links; retain a URL, document
name or output identifier locally when it identifies the object to check.
Missing antecedents and unknown implementation status remain explicit unknowns.
Do not infer that a named baseline was run or that quoted advice was adopted.

Before freezing the first pass, compare each substantive source unit with its
claim for four facets: quantities/objects, conditions/branches, attribution/
source, and verification status. These details must survive in the claim that
the reviewer receives, not only in hidden notes or a generic scope. This is the
Observer's bounded self-check, not a new full independent review. Preserve
applicable detail once and link repeated statements instead of duplicating
whole sources. Private facts and raw quotations still stay local.

Compare retained observations against the source for exact thresholds, required
output sections, mandatory versus optional wording, exceptions and who performs
each step. Do not replace an inclusive threshold with an exclusive one, or a
requirement with background. Record this semantic audit in `review.method`;
setting `completeness_reviewed=true` alone is not semantic evidence. When a
comparison reveals gaps, preserve both measured outputs, write explicit local
revisions, and verify the repaired items separately. A successful repair of
known gaps is not a fresh-sample completeness score.

Every direct message appears once with at least one unit. Every quote must be
an exact substring of that message. Unit and observation IDs are unique, and
their references must agree in both directions. Direct source truncation
blocks validation; recover a complete source or replace the selection before
semantic work, preserving the failed attempt.

```powershell
python scripts/context-coverage.py validate --run-dir $run --observations $observations
```

Now compare the observations with core, learned rules and relevant candidate
records. Every entry in reflection `promotions`, `reinforced`, `deferred` or
`rejected` includes `observation_ids`. Each observation must reach exactly one
disposition; merging related observations is allowed. An observation that is
not a stable preference can be deferred or rejected with its original scope
intact. Do not turn "already covered" into a new rule.

```powershell
python scripts/context-coverage.py validate --run-dir $run --observations $observations --reflection $reflection
```

New `prepare` runs set `coverage_required=true`; normal evolution validation
and application enforce this ledger. Earlier frozen runs retain their legacy
contract and remain historical evidence, not new compliance claims.

## Completeness evidence

Script coverage proves accounting and source linkage, not semantic recall.
For a requested completeness comparison, an independent reviewer first builds
a reference inventory from the same raw training sources without seeing the
arms or candidate conclusions. Freeze that inventory, then compare anonymized
arm outputs for covered, partial, missing and unsupported requirements. Review
the reference inventory too; it is model judgment, not human ground truth.
Keep useful single-task observations separate from promotable stable rules.

Report structural message coverage, semantic requirement coverage, scope
distortion and unsupported generalization separately. Count extra reference
reads and adjudication outside each metered extraction arm; do not claim the
whole experiment became cheaper from a smaller candidate payload alone.

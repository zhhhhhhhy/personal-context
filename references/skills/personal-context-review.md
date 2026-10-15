# Source-preserving semantic review

Use after the Observer freezes a valid `coverage/1` ledger. The parent can act
as Observer and Reflector in one session; this adapter does not require another
full-source Reflector read. Independent review reads only selected source pages.
It does not grant permission, promote rules, or prove semantic completeness.

## Default v2 workflow

Use one run directory throughout. These commands are callable by the parent:

```powershell
$run = 'D:/worker/personal-context/.local/context-evolution/<run>'
python scripts/context-review.py --run-dir $run plan --page-tokens 9000
python scripts/context-review.py --run-dir $run read --file review/shared/page-001.json --reader reviewer
python scripts/context-review.py --run-dir $run read --file review/shared/page-002.json --reader reviewer
python scripts/context-review.py --run-dir $run read --file review/initial/page-001.json --reader reviewer
python scripts/context-review.py --run-dir $run check-review --report <raw-report.json> --validate-only
python scripts/context-review.py --run-dir $run route --report <adjudicated-report.json>
python scripts/context-review.py --run-dir $run route --report <followup-report.json>
python scripts/context-review.py --run-dir $run route --outside-audit
```

`plan` prints the actual shared/page file lists and a complete `report_template`.
Read those lists, not an assumed page count. Read the shared task once and the
scope dictionary pages needed by each message page; the reader enforces these
dependencies. Reuse the same reader name across the review chain. Four Context
core files are session prerequisites, not repeated per page. `build-source`
still prepares the optional legacy Observer/core packets.

Every original message stays verbatim. Exact equal scope strings share short
`scope_ref` IDs; every distinct scope stays in the shared dictionary. Claims,
observation links and reasons for unobserved units remain available. Pages are
bounded without truncation; a single oversized message or scope rejects the
plan so the caller can choose a larger explicit bound. The plan, page manifests,
catalog, observations, source identities and training-file hashes are checked
on each page read. A frozen plan cannot be overwritten. The local SHA anchors
detect drift; they are not signatures against someone rewriting all artifacts.

`read` rejects a repeated file/hash/reader combination. An explicit necessary
reread uses `--reread-reason "why this second read is needed"`; its input and
reason remain in `review/reads/reads.jsonl`. These counts measure returned JSON
input, not platform context, generation tokens or the provider bill.

## Compact result and validation

Copy the emitted template, retaining its identity fields:

```json
{
  "schema_version": "risk-review-result/2",
  "manifest": "review/initial/manifest.json",
  "manifest_sha256": "<copy emitted value>",
  "source_digest": "<copy emitted value>",
  "observations_sha256": "<copy emitted value>",
  "checked_ids": ["M001", "M002"],
  "issues": [
    {
      "message_id": "M001",
      "risk_class": "quantity",
      "kind": "partial",
      "quote": "<exact substring>",
      "problem": "Which source meaning was lost or changed",
      "minimal_repair": "Smallest source-supported repair"
    }
  ]
}
```

`checked_ids` must contain every selected ID exactly once, across all pages of
that manifest. Clean messages need no extra rows or counts. Issues must refer
to selected IDs, use `missing`, `partial`, `unsupported` or `scope`, and quote
an exact nonempty substring from that message or its linked claim/scope. The
validator rejects invented quotes, unknown kinds/classes, incomplete/duplicate
IDs and changed source/manifest hashes.
It validates structure and quote location, not the truth of a semantic judgment.

Before freezing, the tool assigns overlapping clues to every message from both
source text and unit/observation claims: `quantity`,
`constraint`, `format_reference`, `delivery_stage`, `actor`, `causality`,
`fidelity`. Shared scope remains available for interpretation, but does not
create risk tags: repeated project descriptions must not tag an entire batch.
First-person knowledge limits such as "I do not know" also trigger `actor`, so
personal uncertainty is not silently rewritten as an objective project state.
Short corrections of the editing target also count as reference clues.
The initial selection preserves all v1 risk conditions plus the
same fixed 20% low-risk sentinel (at least one when available). `actor` requires
role/ownership clues rather than a bare “I/you”; `fidelity` is not a universal
fallback. Tags are heuristic and can miss a semantic class.

A finding's semantic class may lack a keyword clue in its own source. New plans
accept a defined class and record `unmatched_issue_clues`; adjudication checks
that interpretation. Frozen tags select follow-up candidates, not which kinds
of errors a reviewer is allowed to discover. Older frozen plans retain their
original class-label check. A problem outside the defined classes uses
`risk_class: "other"` and the additional
field `scope: {"conversation": "T01"}`, matching that message's conversation.
This explicitly limits fallback to its parent conversation; it never silently
maps to zero scope or automatically selects all remaining conversations.

## Adjudication, chained follow-up and outside-class audit

Use `check-review --validate-only` on raw findings before adjudication; it does
not register their issues for routing. Preserve the raw report and rejection
reasons locally, and create a separate adjudicated report. Ordinary
`check-review` or `route --report` validates and registers an immutable receipt.
Registered reports and their source files must remain unchanged. Do not register
a raw report whose issues have yet to be accepted: routing accumulates all
registered issues, not just the last report or sentinel findings.

`route` selects unchecked messages sharing any accepted issue class, using the
original frozen tags. A follow-up can discover another class and trigger a new
route. It never rewrites the initial plan, changes tags, repeats checked IDs or
uses a full fallback for follow-up. Every issued review bundle must have a
validated complete report before another route; merely delivering a page does
not establish review coverage. Zero remaining matches are reported explicitly.

Once the class chain has no unchecked matches, `route --outside-audit` creates
one separate bounded audit: a fixed hash sample of 10% of still-unchecked
messages outside active classes, at least 2 and at most 4, capped by available
messages. This audit cannot be issued repeatedly to drain the remainder. Its
input tokens are reported separately. Validate its result and call `route`
again; new accepted classes expand through the same frozen rule. Report actual
checked/repair scope and remaining unknowns, not a 100% recall claim.

The initial plan alone may use the existing 80% whole-packet fallback. Its
decision and cost are explicit. `tokens` includes mechanically estimated v1
whole/selected inputs and v2 shared/whole/initial inputs; legacy whole is not a
second model review. Count actual extraction, shared input, review, follow-up,
audit, adjudication, candidate lookup and dispatch separately when comparing
complete workflows. Savings alone do not establish fidelity.

## Legacy compatibility

Existing v1 plans, packets and per-message count results remain readable and
checkable. `plan --protocol v1` creates that protocol for a fresh run; its
sentinel issue still escalates to all remaining messages. Do not mix v1 results
with a v2 plan. The optional `build-source` and `expand --draft <draft.json>`
Observer adapter remains unchanged: each short-ID message has `units` with
`quote`, `kind`, `claim`, `scope`, `observe`, `reason`, plus the completeness
`review` object. Expanded observations keep `coverage/1`, and the existing
coverage/reflection validators and apply/rollback path remain unchanged.

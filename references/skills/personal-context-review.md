# Concentrated semantic review

Use during requested Context evolution after the Observer ledger is frozen.
Structural coverage remains mandatory. This review does not grant permission,
promote rules, or prove completeness merely by matching a risk keyword.

1. `context-review.py --run-dir <run> plan` validates the ledger and creates
   compact review packets. They retain each selected original message verbatim,
   linked claims and scopes, plus reasons for unobserved units. Long provenance
   IDs stay in the local mapping; do not summarize away source constraints.
2. Review all selected risk messages: meaningful units with no observation,
   quantities, formatting, mandatory conditions, exceptions, unresolved
   references and multi-part/quoted material. Also review the fixed 20% sample
   of remaining messages, at least one. Risk labels are routing clues only.
3. Read packets using `read --file review/targeted.json --reader targeted`.
   If selected input is at least 80% of the compact whole packet, the tool
   chooses the whole packet. Do not lower coverage to meet a savings target.
4. Save one review row per supplied message with requirement counts and
   source-backed issues. Run `check-review --report <report>`; any issue in
   the low-risk sample requires reading `review/remaining.json`. Treat partial,
   missing, unsupported or scope problems conservatively. Record repairs and
   check their specific source support; do not silently edit frozen results.
5. Return to Reflector for candidate lookup and dispositions. New single-task
   observations may be useful without becoming long-term rules. Apply only
   through the existing evolution validator and rollback path.

For a requested strategy comparison, use the same frozen observations and
same source-preserving packet format for targeted and whole reviewers. Keep
their findings isolated until both finish. The whole reviewer serves as an
additional model reference; inspect disagreements against original source,
and disclose its possible misses. Count extraction, candidate lookup, review,
escalation and repair inputs in each alternative pipeline; list the comparison
arm separately from actual production work. Platform context and billing are
not observed by these tools. A smaller packet and zero observed regressions
in one batch are not proof of universal recall or of the cheapest total session.

Commands support local JSON packets only. `build-source` and `expand` are
optional compact Observer adapters; the expanded ledger still uses coverage/1
and passes the unchanged source and reflection validation.

Observer adapter draft: `messages` contains `{id, units}` for every supplied
short message ID. Each unit has `quote` (exact source substring), `kind`,
`claim`, `scope`, `observe` (boolean), and `reason`. Include
`review: {completeness_reviewed: true, method: "what was checked"}`. The adapter
expands short IDs into the unchanged provenance schema. Conversation aliases
and family labels differ: never merge separate parent conversations merely
because they concern the same project family.

Reviewer result: `messages` contains `{id, useful_requirements, covered,
partial, missing, issues}` once per supplied message. Counts are nonnegative
integers and the last three sum to the total; issues contain `quote`, `problem`,
`minimal_repair`, and `kind`. Splitting counts may differ between reviewers;
compare source meanings and scope, not only totals.

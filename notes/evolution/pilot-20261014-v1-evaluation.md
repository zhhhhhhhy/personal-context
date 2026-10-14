# Pilot evaluation: context evolution

- Run: `pilot-20261014-v1`
- Status: **reduced**
- Training cohort: 12 unused parent conversations
- Frozen evaluation cohort: 3 parent conversations
- Proposed observations: 3
- Automatically promoted learned rules: 0
- Human acceptance: pending

## What passed

- The train/evaluation partition was frozen before semantic drafting. A deliberately contaminated reflection was rejected.
- A sensitive promotion was rejected.
- A changed base snapshot was rejected.
- The applied batch was rolled back and re-applied successfully during the controller test.
- The repository path received no raw or sensitive evidence; the final `learned` path remains empty.
- Candidate ledger, conflict, direct-user evidence-location, and base-hash checks passed for the final zero-promotion reflection.

## Why no rule was promoted

- The explanation-order candidate is compatible with the evidence, but overlaps the existing communication core and candidate `C-20261014-035`; independent reuse was not established.
- The repository-first candidate is narrow and partly inferred from two project threads, and overlaps `C-20261014-038` and `C-20261014-044`.
- The comparison-table candidate has one explicit request in this cohort and overlaps the existing communication guidance; recurrence and behavioral benefit were not established.

All three candidates remain deferred in the local run artifacts and candidate ledger. Deferral is the intended quality result for this first pilot, not a failed transaction.

## Holdout assessment

The three held-out cases covered article synthesis, resource search, and a high-risk system-operation request. Only the article-synthesis case was applicable to one candidate. The other two cases tested licensing and safety boundaries, which belong to the core rules or deferred queue. No fresh model response, A/B comparison, or user acceptance measurement was run, so this pilot does not claim semantic behavior improvement.

## Quality judgment

The **pipeline is good enough for a first controlled pilot**: it has a fixed cohort, source-role checks, no leakage, sensitivity gating, stale-base protection, atomic application, rollback, and an independent review.

The **content evolution is not yet sufficient for automatic promotion**. The evidence is concentrated in 12 conversations about tools, repositories, comparisons and system operations, and the holdout is small. The next useful test is a non-overlapping batch containing research, documents, engineering and ordinary communication tasks, with a fresh response comparison and explicit human acceptance before any candidate is promoted.

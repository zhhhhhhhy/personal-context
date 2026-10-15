# Workflow Transaction State

- Schema version: 1
- State version: 17
- Transaction ID: TX-ace8a5a1136f
- Objective: Preserve concrete unverified evidence in first-pass extraction, freeze the contract, and evaluate a rich uncovered cohort with bounded semantic review.
- Scope: Observer contract, historical supplemental cohort, local evidence, redacted metrics, context decisions and repository synchronization.
- Status: completed
- Current phase: report
- Owner: user
- Next action: User assesses usefulness, remaining uncertainty and measured cost/completeness tradeoff.
- Created: 2026-10-15T11:47:25+00:00
- Updated: 2026-10-15T12:12:51+00:00

## Acceptance conditions

| ID | Condition | Status | Evidence |
|---|---|---|---|
| AC1 | Explicit uncertainty retention contract calibrated and frozen before new source reading. | passed | calibration.json and protocol-freeze.json: 11 known-case facets checked; 11 files frozen before cohort selection; end hashes unchanged. |
| AC2 | Unused covered-source messages observed before candidate lookup and checked with frozen targeted review, without a default full reference scan. | passed | Source coverage validated before candidate lookup; review receipts show 86 initial +76 same-class +4 outside; no full independent inventory; raw/accepted/rejected and repairs preserved. |
| AC3 | Same-cohort loading and known omissions measured with unreviewed scope and new-context decisions stated. | passed | measurements.json: actual 22422 review tokens vs 25577 same-format mechanical whole; 14 repaired, 42 unreviewed; 4 scoped refinements, 0 promotions; utility/general recall unknown. |
| AC4 | Privacy, validation, reproducibility and clean repository synchronization verified. | passed | validation.json, freeze-verification.json and content-sync.json: coverage/apply/budget/privacy pass; raw sources ignored; content pushed with matching live remote. |

## Preflight

- Status: ready
- Evidence: 2026-10-15: clean main at 0974ba4; origin/main matches via verified local proxy; Python and tiktoken available from previous run; canonical policy and local source packs present.
- Checked at: 2026-10-15T11:47:26+00:00
- Detail:

## Constraints and blockers

- Constraint: Raw evidence stays local; historical uncertainty gives no authority; no new-cohort tuning; sequential shared-ledger reads.

## Gate checkpoints

- route: 2026-10-15T11:47:26+00:00
- execute: 2026-10-15T11:47:27+00:00
- verify: 2026-10-15T12:12:51+00:00
- report: 2026-10-15T12:12:51+00:00

## Decisions

- 2026-10-15T12:12:51+00:00: Requested implementation and evaluation delivered. No claim of full semantic recall or human acceptance; metadata commit follows.

## Attempt log

| Attempt | Phase | Action | Result | Outcome | Evidence |
|---|---|---|---|---|---|
| A-001 | execute | Improve and calibrate the Observer detail-retention contract, then freeze protocol and allocate work. |  | passed | Observer contract and policy updated; 11 known-case facet checks pass (calibration only); 11 protocol files frozen before selection. |
| A-002 | execute | Select uncovered rich sources by metadata, create frozen evidence, observe before lookup and run bounded targeted review. |  | passed | 208 messages/228 units/226 observations validated; isolated review 86+76+4, 16 raw findings/14 accepted/2 locally rejected; all 14 repaired; 42 independently unchecked; reflection and apply passed with zero promotions; evaluation frozen before held-out reads. |
| A-003 | execute | Measure full recorded payloads, publish redacted assessment and execution issues, validate privacy/budgets, commit and synchronize. |  | passed | Measurements/report/T34-T35 published; context budget and privacy checks passed; content commit f20b445 pushed and live origin/main matches with clean tree before final controller metadata. |

## Event log

- `EV-f1fd1c4965b9` 2026-10-15T11:47:25+00:00 `initialized` {"actor": "parent"}
- `EV-199caacb01f8` 2026-10-15T11:47:26+00:00 `preflight_recorded` {"evidence": "2026-10-15: clean main at 0974ba4; origin/main matches via verified local proxy; Python and tiktoken available from previous run; canonical policy and local source packs present.", "status": "ready"}
- `EV-c8863f63b40c` 2026-10-15T11:47:26+00:00 `gate_passed` {"stage": "route"}
- `EV-a6fa23d4c55f` 2026-10-15T11:47:27+00:00 `gate_passed` {"stage": "execute"}
- `EV-ddbe9161303f` 2026-10-15T11:47:27+00:00 `attempt_started` {"attempt_id": "A-001"}
- `EV-73e2ab384571` 2026-10-15T11:48:57+00:00 `attempt_finished` {"attempt_id": "A-001", "outcome": "passed"}
- `EV-82a8e43990e8` 2026-10-15T11:48:57+00:00 `attempt_started` {"attempt_id": "A-002"}
- `EV-fc0a8979e442` 2026-10-15T12:07:38+00:00 `attempt_finished` {"attempt_id": "A-002", "outcome": "passed"}
- `EV-9b2964a900df` 2026-10-15T12:07:39+00:00 `attempt_started` {"attempt_id": "A-003"}
- `EV-ad0c413c44ca` 2026-10-15T12:12:50+00:00 `attempt_finished` {"attempt_id": "A-003", "outcome": "passed"}
- `EV-578b4d94d49e` 2026-10-15T12:12:51+00:00 `gate_passed` {"stage": "verify"}
- `EV-896edcab9723` 2026-10-15T12:12:51+00:00 `acceptance_verified` {"criterion": "AC1", "result": "passed"}
- `EV-1355ec5dcf3c` 2026-10-15T12:12:51+00:00 `acceptance_verified` {"criterion": "AC2", "result": "passed"}
- `EV-2ac11ce98155` 2026-10-15T12:12:51+00:00 `acceptance_verified` {"criterion": "AC3", "result": "passed"}
- `EV-e9942c3aa2ce` 2026-10-15T12:12:51+00:00 `acceptance_verified` {"criterion": "AC4", "result": "passed"}
- `EV-cd5aaf22ae25` 2026-10-15T12:12:51+00:00 `gate_passed` {"stage": "report"}
- `EV-80b27badf971` 2026-10-15T12:12:51+00:00 `checkpoint` {"note": "Requested implementation and evaluation delivered. No claim of full semantic recall or human acceptance; metadata commit follows."}

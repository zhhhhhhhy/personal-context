# Task-Spectrum Routing

Use this workflow before executing a material engineering task when the work includes deterministic checks, contextual interpretation, or decisions that require human accountability.

## Purpose

Turn a broad engineering goal into an auditable work-allocation plan. The plan must say which actor owns each atomic subtask, why that actor is appropriate, what evidence is required, and where the work must stop for human review.

This workflow allocates work; it does not authorize changes to source data, production systems, or external services.

## Required inputs

Collect enough information to describe:

- the user-visible goal and acceptance condition;
- available files, data, tools, scripts, and existing rules;
- expected output and its required precision;
- error costs, reversibility, and any safety, legal, financial, or privacy impact;
- known examples, historical decisions, or evaluation data.

If a missing input changes the ownership decision, record the gap as `UNRESOLVED` and route the affected subtask to human clarification.

## Allocation procedure

1. State the goal, user impact, and acceptance condition in concrete terms.
2. Inspect the available inputs and existing deterministic checks before proposing AI work.
3. Decompose the goal into atomic subtasks with one observable output each.
4. Classify every subtask as `SCRIPT_ONLY`, `AI_ASSISTED`, `HUMAN_REQUIRED`, or `HYBRID`.
5. Record the evidence and risk that support each classification.
6. Define handoff conditions, especially when AI must abstain or ask for human review.
7. Specify an evaluation method for script and AI steps, and a decision record for human steps.
8. Produce the allocation plan and stop before execution unless the user explicitly asks to continue.

## Classification rules

### `SCRIPT_ONLY`

Assign a subtask to a deterministic script when its inputs are structured, its rules are explicit and stable, its output is testable, and the acceptable result does not depend on open-ended context or subjective judgment.

Typical examples include schema checks, missing-field detection, range validation, deduplication, format conversion, joins, and exact threshold checks.

### `AI_ASSISTED`

Assign a subtask to AI when it requires language, semantic, contextual, or example-based reasoning, and its errors can be measured, reviewed, or bounded. Specify the AI action: classify, rank, summarize, explain, generate a candidate, or compare evidence.

AI output must include the case identifier, decision, supporting evidence, uncertainty, and a review flag. Treat model confidence as a routing signal, not as proof of correctness.

### `HUMAN_REQUIRED`

Assign a subtask to a human when it requires accountability, policy or value judgment, resolution of conflicting evidence, approval of an irreversible or high-impact action, or interpretation outside the available examples and rules.

Define what the human must decide and what record must be retained. Do not replace a required human decision with an AI confidence threshold.

### `HYBRID`

Use a hybrid workflow when deterministic filtering can reduce the search space, AI can interpret the remaining ambiguous cases, and a human must review low-confidence, conflicting, novel, or high-impact cases.

The handoff should be explicit:

```text
script prefilter → AI candidate decision → human review queue → feedback and evaluation update
```

## Output contract

Produce both a human-readable plan and a machine-readable allocation table. Each subtask should contain:

```json
{
  "id": "S1",
  "task": "",
  "owner": "script|ai|human|hybrid|unresolved",
  "reason": "",
  "inputs": [],
  "outputs": [],
  "evidence_required": [],
  "risk": "low|medium|high",
  "handoff_condition": "",
  "acceptance_or_eval": ""
}
```

The plan must also state:

- which steps may run automatically;
- which steps are suggestions only;
- which steps require human approval;
- what happens when evidence is missing, contradictory, or novel;
- what feedback becomes a regression case or a candidate rule change.

## Release and feedback boundary

Human feedback may propose changes to rules, prompts, examples, or evaluation cases. Do not silently rewrite the Skill or promote a new rule from one case. Compare the candidate change against regression and holdout cases, retain the version and evidence, and require the appropriate human approval before treating it as an accepted workflow change.

# Engineering Progression Mode

## When to use

Use this reference for a feature, evaluation, safety issue, regression, integration issue, or quality gap that will require more than one decision or attempt. A one-line fix with no meaningful follow-up does not need an iteration record.

## Progress loop

1. **Name the problem.** Describe the observable symptom and who or what it affects. Do not start with a solution.
2. **Set the acceptance condition.** Define the behavior, metric, safety gate, or artifact that will show whether the method worked. Include a fail-closed condition when the evidence may be absent.
3. **Choose the method.** State the implementation, experiment, test, delegation, or data change that addresses the cause. Keep calibration, regression, and sealed holdout inputs separate when evaluation is involved.
4. **Execute the method.** Preserve unrelated user changes. Delegate independent work when useful, but independently verify delegated results before integrating them.
5. **Measure the effect.** Record user-visible behavior first, then quantitative results. Compare with the previous iteration only under a comparable protocol.
6. **Classify the result.** Use `resolved` only when the acceptance condition passes; use `reduced` when the issue improved but remains; use `blocked` when a required dependency or input is unavailable; use `not_run` when the measurement was not executed.
7. **Plan the next method.** The next method must target the remaining cause of the same problem. Explain what new evidence it should produce and what would stop the iteration.

## Entry schema

Use this structure in the project iteration document:

```markdown
### IT-XXX: Short problem name
- Date: YYYY-MM-DD
- Status: open / reduced / resolved / blocked / not_run
- Problem and user impact:
- Acceptance condition:
- Proposed method:
- Work performed:
- Observed result:
- Evidence:
- Remaining limitation or cause:
- Next method for this problem:
```

## Decision boundaries

- A static or unit test result does not prove browser execution, rendering, deployment, or user acceptance. Label the layer that was actually tested.
- A backend candidate does not prove that a browser found or wrote a control. Require an explicit browser observation before claiming locator or submission metrics.
- A failed holdout is evidence about generalization, not a reason to tune against the holdout. Fix calibration or regression inputs, freeze again, and run a new sealed holdout.
- A missing fixture, service, or dependency is an environmental blocker. Record it separately from a model or product failure and do not fabricate a score.
- A safety gate failure blocks release even when an average accuracy metric improves.

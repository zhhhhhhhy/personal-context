# Skill evaluation

Evaluate this Skill on three separate dimensions instead of treating a good final answer as proof that the workflow ran:

1. **Activation:** In a fresh thread, test an explicit `$engineering-project-workflow` request and an implicit multi-step engineering request. Record whether the Skill was selected and whether `SKILL.md` was read. The upstream selector does not expose a reliable winner/suppressed event to the local controller, so a controller state can mark activation only as `indeterminate`; do not claim implicit triggering from the final answer alone.
2. **Process:** Inspect the controller event order. `scripts/workflow_eval.py` checks initialization, preflight, route and execution gates, bounded attempt logging, verification gate, acceptance verification, and the report gate.
3. **Outcome:** Check that the controller ends `completed` and that every acceptance condition has passed evidence. A successful model response, a launched command, or a partial proxy metric is not an outcome pass.

Run the local checks with:

```text
python scripts/workflow_eval.py --state docs/WORKFLOW_STATE.json
python scripts/workflow_eval.py --state docs/WORKFLOW_STATE.json --strict
```

Run the evaluator after a task reaches a checkpoint, after compaction or handoff recovery, and before reporting completion. If process or outcome fails, keep the transaction `verifying`, `reduced`, or `blocked` and fix the missing stage rather than rewriting the report.

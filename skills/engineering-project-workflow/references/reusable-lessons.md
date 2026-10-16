# Consolidated planning and iteration methods

Merged from existing scoped memories on 2026-10-16. These methods complement the controller and do not require extra reviews, fixed document counts or automatic delegation.

- Plan around the actual deliverable: objective, constraints, step inputs/outputs and acceptance. Reuse the project's current plan and revise it when evidence changes. `PLAN.md`, SDD and nine separate documents are historical examples, not mandatory templates.
- For a failure that affects the result, retain the failing case, cause hypothesis, chosen change and comparable before/after evidence. Separate environment blockers from product failures; report a blocker when it affects delivery. Do not mix readiness logs into the failure analysis by default.
- For browser acceptance, inspect the actual visible result in the authorized browser channel. Backend/static checks alone do not establish a user-visible outcome. Dataset layout, demo IDs and old coverage numbers remain project-specific.
- Before an expensive experiment, resolve the task's root, inputs, model/training needs, resource availability, runtime and stop conditions. A small diagnostic run precedes a planned full run when it can catch setup errors; preserve required full acceptance. Release only resources started/owned by the current authorized run. Old GPU pauses, API skips, chosen model sizes and requests to wait are not current permission.

Original project constraints remain in `D:/worker/personal-context/references/projects/index.md`: AutoFill language/delegation/topology, DemoPilot testdata, and distinct research task versions. Read those only when continuing the matching project. No source task is treated as another project's version merely because both mention AutoFill or JEV.

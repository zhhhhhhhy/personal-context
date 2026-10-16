# Task Graph: scoped design decisions

Identity: project key `taskgraph`; verified source family `019f92c5-1c9c-78a3-acb0-c23a892d49c1`; source workspace `D:/worker/codex-visual`; E145–E149 at 2026-07-24 06:21–06:31 UTC. That root identifies the historical task, not an assertion about today's implementation commit.

Agreed design: **Workspace → Run → Task Graph**, independent history for each run, HTTP/JSON first. Use mixed acceptance: the backend verifies what it can; other tasks wait for human acceptance in the existing AI application, which reports `complete_task` or `reject_task`.

An observer child Agent updating the task graph through a Skill was a desired interaction, **not verified implemented by this evidence**.

## Current local specification check, 2026-10-16

`D:/worker/codex-visual/docs/MVP_SPEC.md` still specifies Workspace → Run → Task Graph and HTTP/JSON, but defines a **read-only observability service**. It explicitly excludes executing commands/tests, verifying repository artifacts, and editing/approving tasks from its dashboard. It describes a cooperative observer receiving explicit progress summaries, rather than intercepting hidden reasoning or every tool call.

This differs from the earlier mixed-acceptance design. Preserve that older agreement as historical intent; do not assume `complete_task`/`reject_task` or automatic artifact verification exist in the current MVP. The directory is not a Git checkout, so the file hash recorded in `docs/memory-refinement/version-checks.json` anchors this check; it does not establish runtime implementation. On continuation, inspect the actual schema/endpoints and user's current goal. Do not turn this project's architecture into a default for other products.

Destination of original memory 19. Evidence: E145–E149, preserved in `project.taskgraph-design`.

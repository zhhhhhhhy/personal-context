# GAIA Claude test：未跑数据按三级各取三道

- id: `project.gaia-new-data-nine`
- kind: project
- status: active
- scope: 来源cwd为D:/worker/gaia_claude_test的该次测试请求；与其它批次及gaia_claude_code版本分开
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T04:52:48+00:00

历史gaia_claude_test任务先测试项目连通性，再重新挑选未跑过的数据：level1、level2、level3各3道，共9道，再运行一次。

## Boundaries

- 这是选择和运行要求，不是运行成功、正确率或完整验收证据。
- 每级3道和总计9道仅限该次请求，不替代既有历史5题联调记录或成为固定配额。
- 虽然cwd对应既有gaia-claude-test项目键，提交版本与跨线程先后关系未核，不合并或替代旧任务；不能并入gaia_claude_code。
- review_after: 2027-01-16
- target: references/projects/gaia-new-data-nine.md

## Evidence pointers

- R014-M053: `019dbe91-4bb2-7aa1-a063-602802df9c2e` / `rollout-2026-04-24T16-18-06-019dbe91-4bb2-7aa1-a063-602802df9c2e.jsonl:L6` — 用户的历史项目请求；完整对象、条件、数量和待核边界保存在本条claim/scope/exception与本地观察账本。
- R014-M054: `019dbe91-4bb2-7aa1-a063-602802df9c2e` / `rollout-2026-04-24T16-18-06-019dbe91-4bb2-7aa1-a063-602802df9c2e.jsonl:L148` — 用户的历史项目请求；完整对象、条件、数量和待核边界保存在本条claim/scope/exception与本地观察账本。

- candidates: none

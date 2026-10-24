# 合同研究：比较边界与任务约束入口

## 续接摘要

对应合同研究版本区分Direct、JEV-A、JEV-B 0.6B及组合，区分答案盲的前置判断与可见候选的支持判断；按匹配任务保留工程/论文分离、稿件范围及定向外部编辑的确认条件。旧开发集提议和零散分数不作当前协议。2026-10-17用户要求Trust-SFT训练来源未核实时保留旧结果，暂不纳入训练效果结论；本次只保存该约束，不核实或执行科研任务。

- 不同任务的论文同步、局部编辑与启动约定分别保留，不按消息日期跨任务覆盖。
- 继续原定向编辑任务时，外发编辑Prompt先确认、只改指定位置等原约定仍需遵守；本次不派发任务。
- 历史样本数、重复次数和方差问题只在来源细节中追溯，不推断为已完成结果。

本次只整理已有Context，没有读取项目运行状态。先用本节确认范围，只有相关任务需要时才读取下面的版本细节；旧约定未因摘要精简而取消。

## Trust-SFT来源待核条件（2026-10-17用户约定）

- 同一研究比较任务中，用户要求把Trust-SFT标为**训练来源未核实**，保留旧结果，暂不纳入训练效果结论。待核不等于已经证实未训练，README或模型名称也不能证明真实训练。
- 用户原请求范围是重新汇总Direct、JEV-A-Gate和SC-Gate在**26题P–F**上的结果，并要求先不跑新模型。这里保存范围与限制，不表示重新汇总、来源核查或任何实验已经完成，也不构成本维护任务执行科研的授权。
- 需要续接这个任务时，先核对真实训练会话、执行证据和之后的明确指令；本次没有检查科研进度，不推断后续核查结论。
- 来源：父对话`01a134f8-4858-77f0-9b71-6e9c7a96f06c`，用户消息`2026-10-17T06:38:11.054Z`、`2026-10-17T06:52:08.627Z`（证据`D20261017-021`、`D20261017-022`）。旧来源与版本细节继续保留下文。

## 来源版本与历史细节（按需追溯）

### Contract research: versioned project material

Project key: `contract-research`. These are separate task/artifact versions, not one global current execution prompt. No remote checkout, experiment or human-review record was rerun here. Before continuation, identify the target root, current commit/manifest, draft and active assignment; consult only the matching sections. A later source message in a different task does not silently cancel another assignment.

## JEV comparison (original memory 11)

E136/E137/E135, 2026-10-06 through 2026-10-10 UTC, source family `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3`, source workspace `2026-10-06/lian`: distinguish Direct, JEV-A, JEV-B 0.6B and their combination. Distinguish an answer-blind pre-generation decision from a support judgment that sees candidate answer, field value and cited evidence. The proposed shared **83-item development set** is a historical proposal, not the default frozen protocol. Questions about **135/200 vs 136/200**, and whether **164/200** was one run or a mean with variance, remain questions; they do not establish reruns or averages.

## Core200 open evidence issue (original memory 12; project residue from 13)

2026-10-16新增来源把原始构造、后续审核和新版Agent标注分开，当前续接见[Core200追溯](core200-provenance.md)；下列原人审待核边界仍保留。

E131 (2026-10-08), family `01a116a5-96a5-7cb3-8150-3c62ba850e3f`, requested a fixed **200-item** evaluation set and a development set for model/threshold choice. The writing request described **all 200 human-reviewed, two independent reviewers, a third arbitrator, no model suggestions**. E134 (2026-10-13), family `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3`, identified incomplete mapping between item IDs and original human-review records, plus some model-assisted answer scoring.

Status: **claims pending source verification**. Find per-item records, reviewer identities/independence, arbitration and reference/scoring provenance before using those process claims as facts. Do not infer Core200 was never used for development/diagnosis. A summary does not prove every model output received independent human scoring. The reusable artifact/label audit method is in the academic-write Skill; unresolved project gaps remain here until actual evidence resolves them.

## Paper synchronization boundary (preserved from archived original 16)

- E078, **2026-10-04 07:42:41.159Z**, family `01a0f292-cdfe-7463-ad96-65832ab94c06`: specified a separate chapter-three ICML draft at `2026-10-03/pdf-latex-latex-icml-paper/outputs/icml_chinese`; requested a copy on the server and localized updates to that draft, leaving the main thesis body aside. This does not prove the copy/update happened.
- E068, **2026-10-06 09:55:09.534Z**, family `01a10644-aeb3-74b3-abac-f511ead2e049`: subsequent engineering assignment separates project and paper, records goals/state/acceptance inside the project, and does **not automatically synchronize the paper**. Preserve this limit when resuming that engineering assignment. A new explicit paper-edit task has its own target/scope.

The dates above are source-message timestamps; an earlier report had reversed the order. They do not make "never update papers" a general rule. Source current root/revision remains to be checked when execution resumes.

## Localized editing delegation (preserved from archived original 15)

E129, **2026-10-08 07:04:58.055Z**, then E128, **2026-10-08 13:42:37.262Z**; family `01a116a5-96a5-7cb3-8150-3c62ba850e3f`; source workspace `2026-10-07/qi`. The already-stable ICML draft was to receive changes only at identified problem locations, via **Claude Code**; the earlier message requested **user confirmation of the outgoing editing Prompt before dispatch**. The later message did not expressly cancel that condition. Current completion/supersession was not verified, so retain these conditions if continuing that same assignment. Do not apply them to unrelated future paper tasks or treat archival as new dispatch permission.

## Historical startup choices (residue from merged original 17)

E077 (2026-10-01), family `01a0f292-cdfe-7463-ad96-65832ab94c06`, source workspace `2026-09-30/zhy-f3b-u4-b9b-yxl`: Qwen3-4B, small trial before the agreed full run, sequential execution, stop when GPU is unavailable or the planned main run ends, API work could be skipped. E158 (2026-09-26), **different family** `01a0de32-f9d8-7691-9871-af57b35b13fd`, requested no immediate startup before explaining root/new-or-reused directory, downloads, training, model size, expected runtime and needed inputs. These are separate startup versions, not a standing pause or GPU authorization for today's task. Generic preflight/resource/small-run guidance is in engineering-project-workflow.

Historical human-review batch sizes **10 then 20** remain in the superseded `research.human-review` record; current progress and batch plan must come from the current ledger. Evidence pointers are preserved in lifecycle histories and the two active project records.

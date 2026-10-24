# 工程项目README：进展与问题修复入口

- id: `engineering.readme-progress-history`
- kind: memory
- status: active
- scope: 用户要求工程项目介绍、进展交接或持续迭代记录时的README组织偏好
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-19T11:11:25+00:00

持续维护的工程项目以README作为首次接触者的进展入口：说明项目目的、主要流程、已实现和未完成事项；涉及数据与评测时区分数据集和测试样例规模，并以版本摘要或链接串起问题、解决办法、验证结果与有依据的代价。沿用项目现有问题修复日志持续更新这个入口。

## Boundaries

- 底层迭代、验收和问题分析仍按engineering-project-workflow及现有日志执行，不另造重复流程或流水账。
- 不是每次代码改动都重写README；只维护相关版本摘要和需要反映的进展，不能把尝试或未验证数据写成已完成成果。
- 更新文档不自动授权提交或推送；历史仓库、密钥、登录及本地环境信息不因此获得发布许可。

## Evidence pointers

- D20261019-005: `01a1065a-38b3-74f0-b70a-b05d3e7c9c9c` / `rollout-2026-10-08T18-21-55-01a1065a-38b3-74f0-b70a-b05d3e7c9c9c_01a11b08-aae5-7623-8390-f7097213ea18.jsonl:L10458` — 用户要求README面向首次接触项目的人说明目标、流程、数据与测试规模、当前进展，并以版本记录问题与解决方案。
- D20261019-006: `01a1087d-3246-7ec3-a3a0-f49546b4c391` / `rollout-2026-10-07T14-04-46-01a1087d-3246-7ec3-a3a0-f49546b4c391_01a114f6-e3d4-7ad1-9c6e-2c63ce7e1efa.jsonl:L17295` — 另一父对话也要求持续更新问题修复记录，并让README展示当前进展。
- D20261019-031: `01a1087d-3246-7ec3-a3a0-f49546b4c391` / `rollout-2026-10-07T14-04-46-01a1087d-3246-7ec3-a3a0-f49546b4c391_01a114f6-e3d4-7ad1-9c6e-2c63ce7e1efa.jsonl:L20183` — 在相关工程迭代中要求问题、修复办法、结果与成本继续记录到README；本次不复测或执行原任务。

- candidates: none

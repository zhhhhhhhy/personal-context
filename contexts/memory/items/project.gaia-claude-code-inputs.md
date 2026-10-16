# 项目：GAIA Claude Code输入与prompt边界

- id: `project.gaia-claude-code-inputs`
- kind: project
- status: active
- scope: 历史gaia_claude_code项目的GAIA输入、prompt与模型通道核对
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T04:29:06+00:00

原D:/worker/gaia_claude_code任务指定Gaia_agent_team的去答案split_validation题目和prompt_gaia；允许略改prompt，但保留创建AGENT TEAM的核心。要求完整轨迹、token、tool与subagent调用信息。用户表示历史经第三方API调用OpenAI模型，配置在litellm目录。

## Boundaries

- 全部是历史用户要求/陈述：当前数据是否确已去答案、provider/model、运行和日志完整性均未重核。
- Claude Code是工具/编排名称，不能据它认定实际模型为原生Claude；地域可用性描述不作当前事实。
- 与上一轮gaia_claude_test来源cwd不同，项目合并/版本关系未核，不能合并或替代那条记忆。
- 不在本轮启动LiteLLM、修改prompt或重跑评测；原启动授权不延续。
- review_after: 2027-01-16
- target: references/projects/gaia-claude-code-inputs.md

## Evidence pointers

- R012-M012: `019dc367-2e64-7281-b9fb-d1c54b16a4f0` / `rollout-2026-04-25T14-50-12-019dc367-2e64-7281-b9fb-d1c54b16a4f0.jsonl:L97` — 原来源cwd为gaia_claude_code；用户指定输入/核心prompt边界、采集要求和历史模型通道。

- candidates: none

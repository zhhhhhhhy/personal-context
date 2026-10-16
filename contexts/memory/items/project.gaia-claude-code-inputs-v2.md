# GAIA Claude Code：输入与prompt契约

- id: `project.gaia-claude-code-inputs-v2`
- kind: project
- status: active
- scope: 历史gaia_claude_code项目的GAIA输入、prompt与模型通道核对
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T06:33:13+00:00

对应gaia_claude_code版本定位Gaia_agent_team的去答案split_validation输入及prompt_gaia，保留创建Agent Team的核心和完整调用轨迹要求。实际provider/model需从对应配置核对，不能根据工具名称推断。

## Boundaries

- 与gaia_claude_test的版本关系未确认，不合并项目或采样协议。
- 历史调用通道只留线索，不能证明当前配置、数据去答案或日志完整性；不保存凭据。
- 本条不授权启动LiteLLM、修改prompt或运行评测。
- 2026-10-16此次仅整理已有Context，未重新核验项目状态；保留详细来源版本约定，不撤销仍适用的条件。
- review_after: 2027-01-16
- target: references/projects/gaia-claude-code-inputs.md

## Evidence pointers

- R012-M012: `019dc367-2e64-7281-b9fb-d1c54b16a4f0` / `rollout-2026-04-25T14-50-12-019dc367-2e64-7281-b9fb-d1c54b16a4f0.jsonl:L97` — 原来源cwd为gaia_claude_code；用户指定输入/核心prompt边界、采集要求和历史模型通道。

- candidates: none

# GAIA Claude Code：输入与prompt契约

## 续接摘要

对应gaia_claude_code版本定位Gaia_agent_team的去答案split_validation输入及prompt_gaia，保留创建Agent Team的核心和完整调用轨迹要求。实际provider/model需从对应配置核对，不能根据工具名称推断。

- 与gaia_claude_test的版本关系未确认，不合并项目或采样协议。
- 历史调用通道只留线索，不能证明当前配置、数据去答案或日志完整性；不保存凭据。
- 本条不授权启动LiteLLM、修改prompt或运行评测。

本次只整理已有Context，没有读取项目运行状态。先用本节确认范围，只有相关任务需要时才读取下面的版本细节；旧约定未因摘要精简而取消。

## 来源版本与历史细节（按需追溯）

### 项目：GAIA Claude Code输入与prompt边界

原D:/worker/gaia_claude_code任务指定Gaia_agent_team的去答案split_validation题目和prompt_gaia；允许略改prompt，但保留创建AGENT TEAM的核心。要求完整轨迹、token、tool与subagent调用信息。用户表示历史经第三方API调用OpenAI模型，配置在litellm目录。

适用：历史gaia_claude_code项目的GAIA输入、prompt与模型通道核对。

- 全部是历史用户要求/陈述：当前数据是否确已去答案、provider/model、运行和日志完整性均未重核。
- Claude Code是工具/编排名称，不能据它认定实际模型为原生Claude；地域可用性描述不作当前事实。
- 与上一轮gaia_claude_test来源cwd不同，项目合并/版本关系未核，不能合并或替代那条记忆。
- 不在本轮启动LiteLLM、修改prompt或重跑评测；原启动授权不延续。

来源是历史用户任务，当前文件和实现未重核；不产生执行授权。

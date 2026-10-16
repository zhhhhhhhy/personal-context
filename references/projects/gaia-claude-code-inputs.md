# 项目：GAIA Claude Code输入与prompt边界

原D:/worker/gaia_claude_code任务指定Gaia_agent_team的去答案split_validation题目和prompt_gaia；允许略改prompt，但保留创建AGENT TEAM的核心。要求完整轨迹、token、tool与subagent调用信息。用户表示历史经第三方API调用OpenAI模型，配置在litellm目录。

适用：历史gaia_claude_code项目的GAIA输入、prompt与模型通道核对。

- 全部是历史用户要求/陈述：当前数据是否确已去答案、provider/model、运行和日志完整性均未重核。
- Claude Code是工具/编排名称，不能据它认定实际模型为原生Claude；地域可用性描述不作当前事实。
- 与上一轮gaia_claude_test来源cwd不同，项目合并/版本关系未核，不能合并或替代那条记忆。
- 不在本轮启动LiteLLM、修改prompt或重跑评测；原启动授权不延续。

来源是历史用户任务，当前文件和实现未重核；不产生执行授权。

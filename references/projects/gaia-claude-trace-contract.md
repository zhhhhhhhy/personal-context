# 项目：GAIA Claude联调与trace计量口径

原gaia_claude_test合并项目的联调先确认链路互通，答案正确率另评；需要完整trace/原始响应，说明token计数是否含system、subagent、hidden context、compaction、retry和工具相关模型调用，并统计代理数/深度、verification与recovery；LiteLLM数据按对话分开。

适用：历史D:/worker/gaia_claude_test项目的联调与Agent team日志核对。

- 这是用户提出的验收要求，原项目现版本与运行结果未核；没有证明上述日志或指标已具备。
- 链路优先仅适用于原联调阶段，不意味着正式评测忽略答案质量；不可观测计量保留未知。
- 原尝试5题与启动config.yaml是旧执行要求，不转为永久配额或本次运行授权。

来源为用户历史要求；原附件、项目代码、运行数据均未在本轮重新核实。完整证据只留本地，记录不是执行授权。

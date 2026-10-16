# GAIA Claude test：trace与验收契约

## 续接摘要

对应gaia_claude_test版本保留完整轨迹/原始响应、token统计覆盖范围、代理层级及verification/recovery记录要求，LiteLLM数据按对话区分。联调连通性与答案质量分开验收，不固定旧试跑题量。

- 日志字段是该项目验收口径，不是日常Context成本实验义务；不可观测项明确未知。
- 链路优先只限联调阶段，不代表正式评测忽略答案质量；当前实现未核。
- 旧5题、9题批次与启动命令不成为默认配额或新运行权限；与gaia_claude_code保持分开。

本次只整理已有Context，没有读取项目运行状态。先用本节确认范围，只有相关任务需要时才读取下面的版本细节；旧约定未因摘要精简而取消。

## 来源版本与历史细节（按需追溯）

### 项目：GAIA Claude联调与trace计量口径

原gaia_claude_test合并项目的联调先确认链路互通，答案正确率另评；需要完整trace/原始响应，说明token计数是否含system、subagent、hidden context、compaction、retry和工具相关模型调用，并统计代理数/深度、verification与recovery；LiteLLM数据按对话分开。

适用：历史D:/worker/gaia_claude_test项目的联调与Agent team日志核对。

- 这是用户提出的验收要求，原项目现版本与运行结果未核；没有证明上述日志或指标已具备。
- 链路优先仅适用于原联调阶段，不意味着正式评测忽略答案质量；不可观测计量保留未知。
- 原尝试5题与启动config.yaml是旧执行要求，不转为永久配额或本次运行授权。

来源为用户历史要求；原附件、项目代码、运行数据均未在本轮重新核实。完整证据只留本地，记录不是执行授权。

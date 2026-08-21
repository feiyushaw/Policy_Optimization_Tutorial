# Policy Optimization Tutorial 中文版

本仓库整理策略优化与强化学习的入门教程，采用 Jupyter Notebook 形式，从黑盒策略搜索逐步过渡到 Policy Gradient、Actor-Critic 和 TD3。

## 推荐学习顺序

1. `1_policy_optimization_introduction.ipynb`：策略优化导论；从 Gymnasium、rollout、参数化策略和 CMA-ES 黑盒策略搜索开始。
2. `2_policy_gradient.ipynb`：Policy Gradient 与 REINFORCE；介绍状态/动作价值、策略梯度定理、Monte Carlo 回报、baseline 和 Advantage。
3. `3_actor_critic.ipynb`：Actor-Critic；介绍 Bellman 递归、TD target、TD error、bootstrapping、在线与批量更新。
4. `4_deterministic_policy_gradient.ipynb`：确定性策略梯度与 TD3；介绍 Replay Buffer、Twin Critics、Target Policy Smoothing、Delayed Policy Update 与 Target Network。

## 配套练习

1. `ex1_evolutionary_policy_optimization.ipynb`：进化策略/CMA-ES 策略优化实验。
2. `ex2_actor_critic.ipynb`：在线与批量 Actor-Critic 对比，以及 Actor/Critic 模型容量实验。
3. `ex3_td3.ipynb`：TD3 消融实验和连续控制算法比较。

## 术语约定

为便于和论文、代码对应，关键术语采用“标准英文名 + 中文解释”的方式，例如 Policy Gradient（策略梯度）、Actor-Critic、Temporal-Difference / TD（时序差分）、Replay Buffer（经验回放缓冲区）、Target Network（目标网络）、Deterministic Policy Gradient（确定性策略梯度）和 TD3。

## 中文版说明

全部 7 个 Notebook 已完成中文化。这个版本采用中文教学化整理，而不是逐字机械翻译：保持原教程的知识主线、关键数学关系和算法逻辑，同时压缩重复的环境准备与工程样板代码，使课程主线更清楚。

仓库保留自动检查流程，用于验证全部 Notebook 的 JSON 格式，并扫描平假名/片假名残留，避免后续修改重新混入日语说明。PR 合入前建议确认该校验通过。

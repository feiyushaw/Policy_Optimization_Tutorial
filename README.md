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

本中文版本不是逐字机械翻译，而是在保持原教程知识主线、数学关系和算法逻辑的基础上进行中文教学化整理。重复代码和环境准备部分适当压缩，重点保留策略优化、价值估计、策略梯度、TD 学习和连续控制算法中最值得理解的内容，并补充了更清晰的章节衔接与实验建议。

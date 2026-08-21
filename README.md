# Policy_Optimization_Tutorial

这里公开一组用于学习策略优化（主要面向强化学习）的 Jupyter Notebook。

本教程强调通过数值实验理解策略优化：从进化策略开始，逐步学习策略梯度、Actor-Critic、确定性策略梯度以及 TD3，并配套练习 Notebook 用于比较算法、做消融实验和分析超参数影响。

## 学习用 Notebook

建议按照以下顺序学习：

1. `1_policy_optimization_introduction.ipynb`：策略优化导论与基于进化策略的策略搜索
2. `2_policy_gradient.ipynb`：策略梯度法（Policy Gradient）
3. `3_actor_critic.ipynb`：Actor-Critic 方法
4. `4_deterministic_policy_gradient.ipynb`：确定性策略梯度（Deterministic Policy Gradient）与 TD3

## 练习用 Notebook

1. `ex1_evolutionary_policy_optimization.ipynb`：完成第 1 个学习 Notebook 后的扩展实验
2. `ex2_actor_critic.ipynb`：完成第 2、3 个学习 Notebook 后的 Actor-Critic 对比实验
3. `ex3_td3.ipynb`：完成第 4 个学习 Notebook 后的 TD3 消融实验与算法比较

## 中文版说明

本分支将原仓库中的日语教学内容整理为简体中文，包括 Notebook 的 Markdown 说明、教学性代码注释和必要的 docstring。标准强化学习术语保留常用英文名称，例如 Policy Gradient、Actor-Critic、Deterministic Policy Gradient、TD3、Replay Buffer、Target Network 等；数学公式、变量名、算法结构和实验设置保持不变。

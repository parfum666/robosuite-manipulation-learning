# Robosuite Learning Notes

基于 robosuite 的机器人操作仿真学习记录。  
This repository records my learning process of robotic manipulation simulation using robosuite.

---

## Current Stage / 当前阶段

This is an early-stage learning project.  
At the current stage, I am learning how to create and run basic robosuite simulation environments.

这是一个早期学习项目。  
当前阶段主要用于学习如何创建和运行基础的 robosuite 机器人仿真环境。

---

## What I Have Done / 已完成内容

- Installed MuJoCo and robosuite  
  已安装 MuJoCo 和 robosuite

- Created a Panda robot Lift environment  
  创建了 Panda 机械臂的 Lift 抓取任务环境

- Ran random actions in the simulation  
  在仿真环境中运行随机动作

- Printed observation keys and action dimension  
  打印环境观测信息和动作维度

- Rendered the MuJoCo simulation window  
  成功打开 MuJoCo 仿真窗口

---

## Current Code / 当前代码

The current script is:

当前代码文件：

```text
01_env_test.py
```

It creates a basic robosuite environment:

它创建了一个基础 robosuite 环境：

```python
env = suite.make(
    env_name="Lift",
    robots="Panda",
    has_renderer=True,
    has_offscreen_renderer=False,
    use_camera_obs=False,
    control_freq=20,
)
```

The robot currently executes random actions.  
The goal of this script is not to solve the Lift task, but to test whether the simulation environment works correctly.

当前机器人执行的是随机动作。  
这个脚本的目标不是完成抓取任务，而是验证仿真环境能否正常运行。

---

## How to Run / 运行方法

```bash
python 01_env_test.py
```

---

## Next Steps / 下一步计划

- Learn how actions control the robot  
  学习 action 如何控制机器人

- Write a simple scripted policy  
  编写简单的规则控制策略

- Save observations and actions as trajectory data  
  保存 observation 和 action 作为轨迹数据

- Replay saved trajectories  
  回放保存的轨迹

- Gradually move toward imitation learning  
  逐步过渡到模仿学习
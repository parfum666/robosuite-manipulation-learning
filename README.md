# Robosuite Learning Notes

基于 robosuite 的机器人操作仿真学习记录。
This repository records my learning process of robotic manipulation simulation using robosuite.

---

## 1. Project Overview / 项目简介

This is an early-stage robotic manipulation simulation project based on robosuite.
At the current stage, I am learning how to create a robosuite environment, read observations, send actions to the robot, and implement a simple scripted control policy.

这是一个基于 robosuite 的早期机器人操作仿真学习项目。
当前阶段主要用于学习如何创建 robosuite 仿真环境、读取观测信息、向机器人发送动作，并实现一个简单的规则控制策略。

The current task is the Lift task with the Panda robot.
The robot is expected to approach a cube, close the gripper, and lift the cube upward.

当前任务是使用 Panda 机械臂完成 Lift 抓取任务。
目标是让机械臂接近木块、闭合夹爪，并尝试将木块向上夹起。

---

## 2. Current Learning Progress / 当前学习进度

So far, I have completed the following steps:

目前已经完成以下内容：

* Installed MuJoCo and robosuite
  已安装 MuJoCo 和 robosuite

* Ran the official robosuite random action demo
  已运行 robosuite 官方随机动作 demo

* Created a Panda robot Lift environment
  已创建 Panda 机械臂的 Lift 抓取任务环境

* Understood the basic simulation loop: `reset`, `step`, and `render`
  初步理解了 `reset`、`step`、`render` 构成的仿真循环

* Printed observation keys and action dimension
  已打印环境观测信息和动作维度

* Implemented a simple scripted policy for the Lift task
  已实现 Lift 任务的简单规则控制策略

* Used `cube_pos` and `robot0_eef_pos` to guide the robot motion
  已使用 `cube_pos` 和 `robot0_eef_pos` 引导机械臂运动

* Made the robot approach, contact, and lift the cube to some extent
  已使机械臂能够接近、接触并在一定程度上夹起木块

---

## 3. File Structure / 文件结构

```text
robosuite-learning/
├── 01_env_test.py              # Basic robosuite environment test
├── 02_scripted_policy.py       # Simple scripted policy for the Lift task
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── .gitignore                  # Files ignored by Git
```

中文说明：

```text
robosuite-learning/
├── 01_env_test.py              # robosuite 基础环境测试代码
├── 02_scripted_policy.py       # Lift 任务的简单规则控制策略
├── README.md                   # 项目说明文档
├── requirements.txt            # Python 依赖库列表
└── .gitignore                  # Git 忽略文件配置
```

---

## 4. Environment / 环境配置

The project is currently tested with:

当前项目使用以下环境进行测试：

```text
Python 3.10
MuJoCo
robosuite
NumPy
```

Install dependencies:

安装依赖库：

```bash
pip install -r requirements.txt
```

Or install them manually:

也可以手动安装：

```bash
pip install mujoco robosuite numpy h5py matplotlib tqdm opencv-python
```

---

## 5. How to Run / 运行方法

Run the basic environment test:

运行基础环境测试代码：

```bash
python 01_env_test.py
```

Run the scripted policy:

运行规则控制策略代码：

```bash
python 02_scripted_policy.py
```

---

## 6. Script 1: Environment Test / 环境测试

The first script is:

第一个脚本是：

```text
01_env_test.py
```

It creates a basic robosuite Lift environment with the Panda robot:

它创建了一个使用 Panda 机械臂的 robosuite Lift 任务环境：

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

This script uses random actions to test whether the environment can be created, stepped, and rendered correctly.

该脚本使用随机动作，主要用于测试环境是否能够正常创建、运行和显示。
这一阶段的目标不是完成抓取任务，而是确认 robosuite 和 MuJoCo 可以正常工作。

---

## 7. Script 2: Scripted Policy / 规则控制策略

The second script is:

第二个脚本是：

```text
02_scripted_policy.py
```

This script replaces random actions with a simple hand-written control policy.

该脚本将随机动作替换为人工编写的简单规则控制策略。

The policy reads the cube position and the robot end-effector position from the observation:

该策略从观测信息中读取木块位置和机械臂末端位置：

```python
cube_pos = obs["cube_pos"]
eef_pos = obs["robot0_eef_pos"]
```

Then it computes the movement direction:

然后计算机械臂末端应该移动的方向：

```python
direction = target_pos - eef_pos
```

The movement action is generated from this direction:

根据该方向生成移动动作：

```python
move_xyz = direction[:3] * 2.0
move_xyz = np.clip(move_xyz, -0.05, 0.05)
```

The current scripted policy is divided into four stages:

当前规则控制策略分为四个阶段：

```text
1. Move the end-effector above the cube
   将机械臂末端移动到木块上方

2. Move down toward the cube
   向下移动并接近木块

3. Close the gripper
   闭合夹爪

4. Lift the cube upward
   向上抬起木块
```

This allows the robot to move with a clear purpose instead of executing random actions.

这样机器人不再随机乱动，而是能够根据木块位置有目的地移动。

---

## 8. Key Concepts Learned / 已学习的核心概念

Through this project, I have learned the following basic concepts:

通过本项目，我已经学习了以下基础概念：

```text
env
The whole robosuite simulation environment.
整个 robosuite 仿真环境。

obs
The observation returned by the environment.
环境返回的当前观测信息。

action
The control command sent to the robot.
发送给机器人的控制指令。

reward
The task-related feedback returned by the environment.
环境返回的任务奖励值。

done
Whether the current episode has ended.
当前 episode 是否结束。

info
Additional information returned by the environment.
环境返回的额外信息。
```

The basic interaction loop is:

基础交互循环如下：

```python
obs = env.reset()

for step in range(500):
    action = policy(obs)
    obs, reward, done, info = env.step(action)
    env.render()
```

---

## 9. Current Limitations / 当前局限

This project is still at an early learning stage.

本项目仍处于早期学习阶段。

Current limitations include:

当前局限包括：

* The scripted policy is hand-designed and not learned from data
  当前规则策略是人工设计的，并不是通过数据训练得到的

* The grasping behavior is not yet fully stable
  当前抓取行为还不完全稳定

* No trajectory dataset has been saved yet
  目前还没有保存轨迹数据集

* No quantitative evaluation report has been generated yet
  目前还没有生成量化评测报告

These limitations will be addressed in the next stages.

这些问题将在后续阶段逐步改进。

---

## 10. Next Steps / 下一步计划

The next stage is to move from robot control to robot data collection and evaluation.

下一阶段将从机器人控制过渡到机器人数据采集与评测。

Planned next steps:

后续计划包括：

* Save observations, actions, rewards, and done flags as trajectory data
  保存 observation、action、reward、done 等轨迹数据

* Save cube position and end-effector position at each step
  保存每一步的木块位置和机械臂末端位置

* Record cube lifting height during each episode
  记录每个 episode 中木块的抬升高度

* Compute simple statistics such as episode length, reward, and maximum cube height
  统计 episode 长度、reward、最大木块高度等指标

* Generate a simple result report
  生成简单的结果报告

* Replay saved trajectories
  回放保存的轨迹

* Gradually move toward imitation learning and demonstration data evaluation
  逐步过渡到模仿学习和示范数据评测

---

## 11. Long-term Goal / 长期目标

The long-term goal of this project is to build a small robotic manipulation data pipeline based on robosuite.

本项目的长期目标是基于 robosuite 搭建一个小型机器人操作数据流程。

The planned pipeline is:

计划流程如下：

```text
Create simulation environment
创建仿真环境

Implement scripted control policy
实现规则控制策略

Collect trajectory data
采集轨迹数据

Evaluate trajectory quality
评估轨迹质量

Generate simple evaluation reports
生成简单评测报告

Move toward imitation learning
逐步过渡到模仿学习
```

This repository will be updated as I continue learning robotic simulation, data collection, and evaluation.

后续我会随着对机器人仿真、数据采集和评测的学习继续更新本项目。

# Perception-Guided Robotic Manipulation

A ROS 2 project for detecting and moving objects with a 7-DOF **MyArm 300 Pi** robot and an **Intel RealSense D435i** camera.

**Georgios Paspalakis and Dimitrios Giannopoulos**  
University of Patras, 2026

[Demo video](https://www.youtube.com/shorts/BuSqtGto4cE) · [Project report](docs/Project_Report.pdf)

## Project

We built a system that detects red cubes on a table and moves them using a suction gripper. The ROS 2 software runs on a laptop, handling object detection, motion planning, and task execution. It communicates over TCP with two Python servers on the robot's Raspberry Pi, which control the arm joints and suction system.

## How it works

- **Camera calibration — ArUco, PnP:** An ArUco marker at a known position is used to determine the transformation between the camera and robot coordinate frames.
- **Cube localization — HSV, RGB-D:** Color thresholding identifies red regions. Depth measurements isolate each cube's top face; its center is estimated in 3D and transformed into the robot frame.
- **Pre-grasp motion — quadratic programming:** An iterative inverse-kinematics solver uses the geometric Jacobian to reduce position and tool-axis errors, subject to joint position and velocity limits. It tries multiple initial joint configurations.
- **Final alignment — visual servoing, Jacobian IK:** The camera detects a blue marker on the end effector and measures its offset from the cube. A damped Jacobian-based solver computes a small correction before grasping.
- **Pick and place — TCP:** Joint and suction commands are sent to the Raspberry Pi. The robot grasps the cube, lifts it, moves to a preset drop pose, and releases it.

## Repository structure

- `project3-team3_workspace/src/perception_pkg/` — camera calibration, cube detection and visual feedback
- `project3-team3_workspace/src/control_pkg/` — inverse kinematics, motion control and pick-and-place sequence
- `myarm_workspace/` — Raspberry Pi joint and suction servers
- `suction_kit_base_stl/` — 3D-printable suction mount
- `docs/Project_Report.pdf` — project report

Setup and execution instructions are available in [INSTRUCTIONS.md](INSTRUCTIONS.md).

This was a joint university project. The hardware setup has not been retested for this repository, and no reuse license has been assigned.

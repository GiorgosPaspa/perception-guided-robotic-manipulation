# Perception-Guided Robotic Manipulation

A ROS 2 project for detecting and moving objects with a 7-DOF **MyArm 300 Pi** robot and an **Intel RealSense D435i** camera.

**Georgios Paspalakis and Dimitrios Giannopoulos**  
University of Patras, 2026

[Demo video](https://www.youtube.com/shorts/BuSqtGto4cE) · [Project report](docs/Project_Report.pdf)

## Project

The robot detects red cubes on a table and moves them using a suction gripper. The RealSense camera supplies color and depth images. We use ArUco markers to calibrate the camera position relative to the robot, then estimate each cube's location from the images.

For motion control, we use quadratic-programming inverse kinematics and a final visual-servoing correction before grasping. The ROS 2 nodes run on a computer, while two TCP servers on the robot's Raspberry Pi handle joint movement and suction.

## Repository structure

- `project3-team3_workspace/src/perception_pkg/` — camera calibration, cube detection and visual feedback
- `project3-team3_workspace/src/control_pkg/` — inverse kinematics, motion control and pick-and-place sequence
- `myarm_workspace/` — Raspberry Pi joint and suction servers
- `suction_kit_base_stl/` — 3D-printable suction mount
- `docs/Project_Report.pdf` — project report

## Running the project

You will need the MyArm hardware, RealSense camera, ROS 2, `colcon`, and the Python dependencies in [requirements-laptop.txt](requirements-laptop.txt).

Start the joint and suction servers on the Raspberry Pi. Then, on the ROS 2 computer:

```bash
cd project3-team3_workspace
colcon build
source install/setup.bash
ros2 run perception_pkg aruco_extrinsic_calibrator
ros2 run control_pkg task_automation_node
```

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for setup details. The code uses calibration and network settings from our lab, so check those and the robot's operating limits before running it.

This was a joint university project. The hardware setup has not been retested for this repository, and no reuse license has been assigned.

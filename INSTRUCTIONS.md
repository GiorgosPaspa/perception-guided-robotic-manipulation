# Original team running instructions (transcribed)

## Structure
- project3-team3_workspace/: ROS 2 host workspace
- myarm_workspace/: two TCP servers on the robotic arm's Raspberry Pi
- suction_kit_base_stl/: printable suction mounts

## Laptop dependencies
```bash
pip install numpy opencv-contrib-python pyrealsense2 scipy 'qpsolvers[osqp]'
sudo apt install ros-$ROS_DISTRO-cv-bridge ros-$ROS_DISTRO-realsense2-camera
```

## Run
1. On the Raspberry Pi, in two terminals, run `python3 joint_tcp_server.py` and `python3 suction_tcp_server.py`.
2. Build the workspace: `cd project3-team3_workspace && colcon build && source install/setup.bash`.
3. Place an ArUco marker at the known table position and run `ros2 run perception_pkg aruco_extrinsic_calibrator`.
4. After safety and calibration checks, run `ros2 run control_pkg task_automation_node`.

Calibration is written to `~/.ros/myarm_camera_extrinsic.json`. A RealSense D435i must be attached. Example Pi address `192.168.0.103`, joints port `5017`, suction port `5018`.

The project is hardware-specific. Confirm end-effector wiring, emergency stop, workspace and joint limits before operation.

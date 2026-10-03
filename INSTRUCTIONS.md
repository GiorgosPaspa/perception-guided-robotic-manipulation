# Running instructions

## Files

| Path | Contents |
|---|---|
| `project3-team3_workspace/` | ROS 2 packages for the computer |
| `myarm_workspace/` | Joint and suction TCP servers for the Raspberry Pi |
| `suction_kit_base_stl/` | Printable suction mount |
| `docs/Project_Report.pdf` | Project report |

## Dependencies

Install a compatible ROS 2 distribution, `colcon`, `cv_bridge`, and the RealSense ROS camera package. ROS and Python dependency compatibility varies by system.

```bash
python3 -m pip install -r requirements-laptop.txt
sudo apt install ros-$ROS_DISTRO-cv-bridge ros-$ROS_DISTRO-realsense2-camera
```

The robot Raspberry Pi requires its compatible `pymycobot` and GPIO support.

## Run

1. Connect the RealSense D435i to the computer.
2. On the Raspberry Pi, start the servers in separate terminals from `myarm_workspace/`:

   ```bash
   python3 joint_tcp_server.py
   python3 suction_tcp_server.py
   ```

3. On the computer:

   ```bash
   cd project3-team3_workspace
   colcon build
   source install/setup.bash
   ros2 run perception_pkg aruco_extrinsic_calibrator
   ```

4. Check camera calibration, the reachable workspace, suction equipment, joint limits, and the emergency stop. Then run:

   ```bash
   ros2 run control_pkg task_automation_node
   ```

The calibration file is stored at `~/.ros/myarm_camera_extrinsic.json`. Example TCP settings are Raspberry Pi `192.168.0.103`, joint port `5017` and suction port `5018`; adjust them for your trusted local network. These instructions are hardware-specific and have not been independently retested for this repository.

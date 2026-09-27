---
title: "ROS 2 Commands I Use Every Day"
tags: [ROS 2, Tools]
---

A living list of ROS 2 CLI commands for debugging nodes, topics and TF. <!--more-->

## Workspace

```bash
colcon build --symlink-install --packages-select my_pkg
source install/setup.bash
```

## Topics

```bash
ros2 topic list -t                 # list with message types
ros2 topic echo /odom --once       # print a single message
ros2 topic hz /scan                # check publish rate
```

## TF

```bash
ros2 run tf2_ros tf2_echo map base_link
ros2 run tf2_tools view_frames      # generates frames.pdf
```

## Notes

- Use `--symlink-install` so Python and launch file edits take effect without rebuilding.
- `ros2 doctor --report` is a quick sanity check when something feels off.

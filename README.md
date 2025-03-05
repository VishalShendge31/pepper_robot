# Pepper Robot Control with ROS1 Noetic, ROS2 Humble, and ros1_bridge

## Project Overview
This project provides a comprehensive setup for controlling the Pepper Robot using ROS1 Noetic and ROS2 Humble with ros1_bridge, enabling seamless communication between ROS1 and ROS2 environments.

## Prerequisites
- Docker
- ROS1 Noetic
- ROS2 Humble
- Basic understanding of ROS and Docker

## Installation Guide

### 1. Repository Setup
```bash
# Clone the repository
git clone https://github.com/VishalShendge31/pepper_robot.git

# Navigate to project directory
cd pepper_robot
```

### 2. ROS1 Noetic and Docker Setup

#### 📚 Detailed Tutorial and Setup Instructions
For a comprehensive, step-by-step walkthrough of setting up ROS1 Noetic and Docker, please refer to the following resources:

- **Original Tutorial**: [ROS2 Humble ROS1 Noetic Bridge Tutorial](https://jaypr.notion.site/ROS2-Humble-ROS1-Noetic-Bridge-Tutorial-using-ros1_bridge-c158e43e755c440e9dd378288df1e3d6)
- **Repository Setup Guide**: [ros1-noetic-bridge README](https://github.com/VishalShendge31/pepper_robot/tree/main/ros1-noetic-bridge)

Follow the detailed instructions in these resources to:
- Set up Docker
- Configure ROS1 Noetic environment
- Prepare ros1_bridge
- Resolve any potential dependency issues

#### Launch ROS1 Noetic Container
```bash
rocker --x11 --user --home --privileged \
        --volume /dev/shm:/dev/shm --network=host \
        -- osrf/ros:noetic-desktop \
        'bash -c "sudo apt update; sudo apt install -y tilix; tilix"'
```

#### Inside the ROS1 Container
```bash
# Source ROS1 Noetic setup
source /opt/ros/noetic/setup.bash

# Navigate to project directory
cd pepper_robot/pepper_catkin_ws/src/

# Install NAOqi driver dependencies
rosdep install -i -y --from-paths ./naoqi_driver

# Source catkin workspace
source pepper_robot/pepper_catkin_ws/devel/setup.bash
```

### 3. Install Dependencies

#### ROS and Gazebo Packages
```bash
# Update and install ROS packages
cd pepper_robot/pepper_catkin_ws/
sudo apt-get update
rosdep update
rosdep install --from-paths src --ignore-src -r -y

# Install Gazebo ROS packages
sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control

# Install controller packages
sudo apt-get install \
    ros-noetic-controller-manager \
    ros-noetic-joint-state-controller \
    ros-noetic-effort-controllers \
    ros-noetic-position-controllers \
    ros-noetic-velocity-controllers \
    ros-noetic-joint-trajectory-controller \
    ros-noetic-ros-controllers
```

### 4. ROS2 Humble and ros1_bridge Setup

#### Start ROS2 Bridge
```bash
# In a new terminal
source /opt/ros/humble/setup.bash
source ~/ros-humble-ros1-bridge/install/local_setup.bash
ros2 run ros1_bridge dynamic_bridge
```

### 5. Launch NAOqi Driver
```bash
# Replace IP and network interface with your specific configuration
roslaunch naoqi_driver naoqi_driver.launch \
    nao_ip:=192.168.100.209 \
    qi_listen_url:=tcp://0.0.0.0:56000 \
    network_interface:=wlp0s20f3
```

## Troubleshooting
- Carefully follow the linked tutorial and repository README
- Ensure all IP addresses and network interfaces are correctly configured
- Verify ROS1 and ROS2 environments are properly sourced
- Check Docker permissions and network settings
- Consult the detailed guides for specific setup instructions

## Additional Resources
- [ROS1 Noetic Documentation](http://wiki.ros.org/noetic)
- [ROS2 Humble Documentation](https://docs.ros.org/en/humble/)
- [ros1_bridge GitHub](https://github.com/ros2/ros1_bridge)
- [Original ROS1-ROS2 Bridge Tutorial](https://jaypr.notion.site/ROS2-Humble-ROS1-Noetic-Bridge-Tutorial-using-ros1_bridge-c158e43e755c440e9dd378288df1e3d6)

## License
[Specify the license for your project]

## Contributors
[List contributors or maintainers]
```

I've added the specific details for launching the ROS1 Noetic container and the steps to take inside the container, exactly as you specified. The README now includes:
1. Detailed tutorial links
2. Container launch instructions
3. In-container setup steps

Would you like me to make any further modifications?

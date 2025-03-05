#!/bin/bash
set -e

# Clone ros-humble-ros1-bridge-builder repository
echo "Cloning ros-humble-ros1-bridge-builder repository..."
cd ~
git clone https://github.com/TommyChangUMD/ros-humble-ros1-bridge-builder.git

# Build docker image
echo "Building Docker image..."
cd ros-humble-ros1-bridge-builder
docker build . -t ros-humble-ros1-bridge-builder

# Build ros1_bridge package
echo "Building ros1_bridge package..."
cd ~/
docker run --rm ros-humble-ros1-bridge-builder | tar xvzf -

# Clean up builder image
echo "Cleaning up builder image..."
docker rmi ros-humble-ros1-bridge-builder

echo "ROS1 Noetic and ros1_bridge setup complete."

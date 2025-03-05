# ROS1 Noetic and ros1_bridge Docker Setup

## Credits
**Prepared by:**
- Prof. Tommy Chang
- Jay Prajapati

📚 **Original Tutorial**
For a detailed, step-by-step walkthrough, visit:
https://jaypr.notion.site/ROS2-Humble-ROS1-Noetic-Bridge-Tutorial-using-ros1_bridge-c158e43e755c440e9dd378288df1e3d6

## System Requirements
- **Operating System**: Ubuntu 22.04 LTS
- **ROS Distributions**: 
  - ROS2 Humble (pre-installed)
  - ROS1 Noetic (will be installed via Docker)
- **Hardware**: 
  - Minimum 4GB RAM
  - 20GB free disk space
  - Active internet connection

## Prerequisites
Before starting the installation, ensure you have:
- Sudo access on your Ubuntu system
- ROS2 Humble already installed
- Basic understanding of ROS and Docker concepts

## Quick Installation Guide

### 1. Clone the Repository
```bash
# Clone the repository
git clone https://github.com/Vishal_shendge31/ros1-noetic-bridge.git

# Navigate to project directory
cd ros1-noetic-bridge
```

### 2. Prepare Installation Scripts
```bash
# Make all scripts executable
chmod +x scripts/*.sh
```

### 3. Run Installation Scripts in Order
```bash
# Step 1: Install Docker
./scripts/install_docker.sh

# Step 2: Install Rocker
./scripts/install_rocker.sh

# Step 3: Setup ROS1 Bridge
./scripts/setup_ros_bridge.sh
```

## Detailed Installation Steps

### Docker Installation
- Installs Docker.io package
- Adds current user to docker group
- Verifies Docker installation
- Requires log out/log in for group changes

### Rocker Installation
- Installs Rocker package
- Verifies installation with test command
- Provides fallback instructions if standard installation fails

### ROS1 Bridge Setup
- Clones ros-humble-ros1-bridge-builder repository
- Builds Docker image
- Compiles ros1_bridge package
- Cleans up temporary build image

## Troubleshooting

### Common Installation Issues
1. **Docker Permission Errors**
   - Symptom: `docker: permission denied`
   - Solution: 
     ```bash
     # Log out completely and log back in
     # Or restart your system
     ```

2. **Rocker Installation Failures**
   - Potential solutions:
     ```bash
     # Try manual installation
     pip install rocker
     
     # Or use Python 3.8 virtual environment
     python3.8 -m venv rocker_env
     source rocker_env/bin/activate
     pip install rocker
     ```

3. **Network or Download Issues**
   - Ensure stable internet connection
   - Check firewall settings
   - Verify GitHub access

## Post-Installation Verification
```bash
# Verify Docker installation
docker info

# Verify Rocker installation
rocker --version

# Check ROS1 bridge package
# [Add specific verification command]
```

## Useful Resources
- [ROS1 Noetic Documentation](http://wiki.ros.org/noetic)
- [ROS2 Humble Documentation](https://docs.ros.org/en/humble/)
- [Docker Documentation](https://docs.docker.com/)

## License
[Specify your project's license, e.g., MIT License]


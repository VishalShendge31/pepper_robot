#!/bin/bash
set -e

# Update package list
sudo apt update

# Install Docker
sudo apt install -y docker.io

# Add current user to docker group
sudo usermod -aG docker $USER

# Start Docker service
sudo service docker start

# Verify Docker installation
echo "Verifying Docker installation..."
docker info
docker run -it --rm hello-world

echo "Docker installation complete. Please log out and log back in for group changes to take effect."

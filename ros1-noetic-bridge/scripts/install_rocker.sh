#!/bin/bash
set -e

# Attempt to install rocker
echo "Attempting to install rocker..."
sudo apt install -y python3-rocker

# Verify rocker installation
echo "Verifying rocker installation..."
rocker --version
rocker alpine echo "hello-world"

# If rocker installation fails, provide alternative instructions
if [ $? -ne 0 ]; then
    echo "Standard rocker installation failed. Please consider setting up a Python 3.8 virtual environment."
    echo "Suggested alternative installation method:"
    echo "1. Install Python 3.8"
    echo "2. Create a virtual environment"
    echo "3. pip install rocker"
fi

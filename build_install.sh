#!/bin/bash

# Update package list and install Python and pip if not already installed
sudo apt update
sudo apt install -y python3 python3-pip python3-pyqt5

# Install PyInstaller
pip3 install pyinstaller

# Navigate to the directory containing your stopwatch.py script
# Change this to your actual script path
cd /path/to/your/script || exit 1

# Create the standalone executable using PyInstaller
pyinstaller --onefile --noconsole stopwatch.py

echo "Build complete. Executable is located in the dist folder."

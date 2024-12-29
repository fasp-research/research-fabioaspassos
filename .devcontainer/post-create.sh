#bin/bash
# This script will be run as the default user (vscode) when the container is created.
pip install --upgrade pip
pip install --user -r requirements.txt 

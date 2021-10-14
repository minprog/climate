#!/bin/bash

# Installs jupyter and sets configuration for compatibility with CS50 IDE

# Set CFLAGS to something less restricted
CFLAGS=""

# Installing jupyter and initialzing the config
yes | pip install --user jupyter
jupyter notebook -y --generate-config

# Os is required to get the C9_PID later
echo "import os" >> /home/ubuntu/.jupyter/jupyter_notebook_config.py

# Settings for the CS50 IDE
echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/ubuntu/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.port = 8080" >> /home/ubuntu/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.open_browser = False" >> /home/ubuntu/.jupyter/jupyter_notebook_config.py

# Setting the displayed URL to the correct amazonaws URL
echo "c.NotebookApp.custom_display_url = 'https://' + os.environ['C9_PID'] + '.vfs.cloud9.us-west-2.amazonaws.com'" >> /home/ubuntu/.jupyter/jupyter_notebook_config.py

FROM python:3.11-slim

WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install development tools
RUN pip install --no-cache-dir black isort pylint

# Create a non-root user
RUN useradd -m -s /bin/bash vscode
USER vscode

# Set Python path
ENV PYTHONPATH=/workspace

# Add /home/vscode/.local/bin to PATH
ENV PATH=/home/vscode/.local/bin:$PATH

# SPDX-License-Identifier: AGPL-3.0-or-later

FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04

LABEL maintainer="Aatif Qmr"
LABEL description="Heretic - Fully automatic censorship removal for language models"
LABEL org.opencontainers.image.source="https://github.com/Aatif-qmr/Uncensored-AI"

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.12 \
    python3.12-venv \
    python3-pip \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock README.md ./
COPY src/ src/

# Create virtual environment and install dependencies
RUN uv venv && \
    uv sync --frozen --all-extras

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV HF_HUB_ENABLE_HF_TRANSFER=1

# Create directory for user configs and checkpoints
RUN mkdir -p /data/configs /data/checkpoints /data/output
VOLUME ["/data"]

# Default command
ENTRYPOINT ["uv", "run", "heretic"]
CMD ["--help"]

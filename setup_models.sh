#!/bin/bash
# Script to download necessary models

mkdir -p models

# Download Whisper Base Model (handled by faster-whisper automatically, but we can pre-download if needed)
# faster-whisper downloads to ~/.cache/huggingface/hub/... by default

# Download Llama-3-8B-Instruct-GGUF (Quantized)
# Default Model: Mistral-7B-Instruct-v0.2 (Quantized Q4_K_M)
# Size: ~4.37 GB
# Good balance of speed and quality for CPU inference
MODEL_URL="https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf"
DEFAULT_MODEL_PATH="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

if [ ! -f "$DEFAULT_MODEL_PATH" ]; then
    echo "Downloading Llama model..."
    curl -L -o "$DEFAULT_MODEL_PATH" "$MODEL_URL"
    echo "Model downloaded to $DEFAULT_MODEL_PATH"
else
    echo "Model already exists at $DEFAULT_MODEL_PATH"
fi

echo "Setup complete!"

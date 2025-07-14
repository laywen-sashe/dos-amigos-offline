#!/usr/bin/env python3
"""
Dos Amigos Offline Setup Script
Sets up the environment and dependencies for Whisper and Parakeet MLX models.
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Error running: {cmd}")
        sys.exit(1)

def main():
    print("🚀 Setting up Dos Amigos for offline use...")
    
    # Create virtual environment
    print("Creating virtual environment...")
    run_command("uv venv .venv")
    
    # Install core dependencies
    print("Installing core dependencies...")
    core_deps = [
        "sounddevice",
        "numpy", 
        "scipy",
        "pynput",
        "mlx"
    ]
    
    for dep in core_deps:
        run_command(f"uv pip install {dep}")
    
    # Install model-specific dependencies
    print("Installing model dependencies...")
    
    # Try to install Parakeet MLX
    try:
        run_command("uv pip install parakeet-mlx")
        print("✅ Parakeet MLX installed")
    except:
        print("⚠️ Parakeet MLX installation failed - Parakeet model will not work")
    
    # Try to install Whisper MLX
    try:
        run_command("uv pip install mlx-whisper")
        print("✅ MLX-Whisper installed")
    except:
        print("⚠️ MLX-Whisper installation failed - Whisper model will not work")
    
    # Install HuggingFace Hub for model management
    run_command("uv pip install huggingface_hub")
    
    print("\n✅ Setup complete!")
    print("\nTo run Dos Amigos:")
    print("1. Activate the virtual environment: source .venv/bin/activate")
    print("2. For Amigo El Ligero (Whisper Small), run: python dos_amigos.py")
    print("4. For Amigo El Preciso (Parakeet), run: python dos_amigos.py --model preciso")
    print("5. List available models: python dos_amigos.py --list-models")
    print("\nOr use: uv run python dos_amigos.py [options]")

if __name__ == "__main__":
    main()

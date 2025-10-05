#!/usr/bin/env python3
"""
Download models to local src/models directory for offline packaging
"""

import sys
from pathlib import Path
from huggingface_hub import snapshot_download

def download_model(repo_id, local_dir):
    """Download a model from HuggingFace to local directory"""
    print(f"Downloading {repo_id} to {local_dir}...")

    snapshot_download(
        repo_id=repo_id,
        local_dir=local_dir,
        local_dir_use_symlinks=False,  # Copy files instead of symlinks for portability
    )

    print(f"✅ {repo_id} downloaded successfully!")

def main():
    # Get the script directory and set up models path
    script_dir = Path(__file__).parent.parent
    models_dir = script_dir / "models"
    models_dir.mkdir(exist_ok=True)

    print("📦 Downloading models for offline packaging...\n")

    # Download Whisper Small MLX
    whisper_dir = models_dir / "whisper-small-mlx"
    if not whisper_dir.exists():
        download_model("mlx-community/whisper-small-mlx", whisper_dir)
    else:
        print(f"⏭️  Whisper model already exists at {whisper_dir}")

    # Download Parakeet v3
    parakeet_dir = models_dir / "parakeet-tdt-0.6b-v3"
    if not parakeet_dir.exists():
        download_model("mlx-community/parakeet-tdt-0.6b-v3", parakeet_dir)
    else:
        print(f"⏭️  Parakeet model already exists at {parakeet_dir}")

    print("\n✅ All models downloaded!")
    print(f"Models location: {models_dir}")

    # Show model sizes
    print("\n📊 Model sizes:")
    for model_path in models_dir.iterdir():
        if model_path.is_dir():
            size_mb = sum(f.stat().st_size for f in model_path.rglob("*") if f.is_file()) / (1024*1024)
            print(f"  {model_path.name}: {size_mb:.1f} MB")

if __name__ == "__main__":
    main()

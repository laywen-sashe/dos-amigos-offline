# 🎙️ Dos Amigos Offline

Two powerful amigos for automatic speech recognition! Run push-to-talk, auto-paste ASR from terminal, using offline open source MLX models (Whisper Small and Parakeet).

## 🎯 The Two Amigos

- **🪽 El Ligero**
	- Lightweight & fast
	- Model: whisper-small-mlx (~500MB)
- **🎯 El Preciso**
	- Precise & fast, maximum accuracy
	- Model: parakeet-tdt-0.6b-v2-mlx (~2GB)

## 🚀 Quick Download & Use

**Want to use it right now?** 

👉 **[Download dos-amigos-offline.zip](releases/dos-amigos-offline.zip)** 

1. Extract the ZIP
2. Run `uv run python scripts/setup_offline.py`  
3. Run `uv run python dos_amigos.py`
4. Press Right Option to record.
5. Press Right Option again to stop recording and paste your recorded text!

## 📸 Demo
(Coming next push)
![Demo GIF](assets/demo.gif)

## 🛠️ For Developers

See the `src/` directory for source code. Full documentation coming soon in `docs/`.

## 📄 License

MIT License - see [LICENSE](LICENSE) file.
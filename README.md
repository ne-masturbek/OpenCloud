# OpenCloud

OpenCloud is a terminal-based SoundCloud audio downloader built with Python and Textual.

## Screenshot

<img width="1192" height="868" alt="{A72CA3B6-9899-428B-803C-32FDABBA513A}" src="https://github.com/user-attachments/assets/f188824a-4a56-4c77-a388-d2fa17e5c88d" />

---

<img width="1189" height="870" alt="{84E9D069-CAFE-4B04-B3C1-DBCA5D7ABBAA}" src="https://github.com/user-attachments/assets/8b7b2873-1b36-467b-8b5d-0eb3d83817aa" />

## Features

- Download audio from SoundCloud using a URL
- Supported formats: MP3, OGG, OPUS, FLAC, WAV, M4A, AAC
- Custom download directory
- Real-time download progress
- Activity and error logs

## Installation

**Requirements:**
- Python 3.10+
- Git
- FFmpeg

**1. Clone the repository**

```bash
git clone https://github.com/USERNAME/OpenCloud.git
cd OpenCloud
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Install FFmpeg**

Windows:
```powershell
winget install Gyan.FFmpeg
```

Linux (Ubuntu/Debian):
```bash
sudo apt install ffmpeg
```

macOS:
```bash
brew install ffmpeg
```

## Usage

Run the application:

```bash
python main.py
```

1. Paste a SoundCloud track URL.
2. Select an audio format.
3. Choose a download directory.
4. Click **Download**.

Files are saved to the `Downloads` folder by default.

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+D` | Start download |
| `Ctrl+L` | Clear logs |
| `Ctrl+Q` | Exit |

## Dependencies

- [Textual](https://github.com/Textualize/textual)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)

## Disclaimer

OpenCloud is an unofficial project and is not affiliated with SoundCloud. Only download audio you have permission to use.

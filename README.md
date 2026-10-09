# OpenCloud

OpenCloud is a terminal-based SoundCloud audio downloader built with Python and Textual.

Download audio in multiple formats directly from your terminal.

## Screenshots

<img width="1192" height="868" alt="OpenCloud interface" src="https://github.com/user-attachments/assets/f188824a-4a56-4c77-a388-d2fa17e5c88d" />

---

<img width="1189" height="870" alt="OpenCloud download interface" src="https://github.com/user-attachments/assets/8b7b2873-1b36-467b-8b5d-0eb3d83817aa" />

## Features

- Download SoundCloud audio using a URL
- Supported formats: MP3, OGG, OPUS, FLAC, WAV, M4A, AAC
- Custom download directory
- Real-time download progress
- Activity and error logs
- Terminal-based interface

## Installation

**Requirements:**
- Python 3.10+
- Git
- FFmpeg
- pipx

### 1. Install pipx

Windows (PowerShell):

```powershell
py -m pip install --user pipx
py -m pipx ensurepath
```

Restart PowerShell after installation.

### 2. Install FFmpeg

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

### 3. Install OpenCloud

```powershell
pipx install git+https://github.com/ne-masturbek/OpenCloud.git
```

## Usage

Launch OpenCloud from any terminal:

```powershell
opencloud
```

1. Paste a SoundCloud track URL.
2. Select an audio format.
3. Choose a download directory.
4. Click **Download**.

Downloaded files are saved to the `Downloads` folder by default.

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+D` | Start download |
| `Ctrl+L` | Clear logs |
| `Ctrl+Q` | Exit |

## Update

```powershell
pipx upgrade opencloud-tui
```

## Uninstall

```powershell
pipx uninstall opencloud-tui
```

## Dependencies

- [Textual](https://github.com/Textualize/textual)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)

## Disclaimer

OpenCloud is an unofficial project and is not affiliated with SoundCloud. Only download audio you have permission to download.

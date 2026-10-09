
from pathlib import Path
from urllib.parse import urlparse
import os
import shutil

import yt_dlp

from textual import work
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import (
    Header,
    Footer,
    Static,
    Input,
    Select,
    Button,
    ProgressBar,
    RichLog,
)


class OpenCloud(App):
    TITLE = "OpenCloud"
    SUB_TITLE = "SoundCloud Audio Downloader | ne_masturbek"

    BINDINGS = [
        ("ctrl+d", "start_download", "Download"),
        ("ctrl+l", "clear_logs", "Clear logs"),
        ("ctrl+q", "quit", "Quit"),
    ]

    CSS = """
    Screen {
        background: #0b0f17;
    }

    #panel {
        width: 100%;
        max-width: 100%;
        height: auto;
        max-height: 100%;
        margin: 1 0;
        align-horizontal: center;
        padding: 1 2;
        background: #151b26;
        border: round #ff8533;
        overflow-y: auto;
    }

    #logo {
        width: 100%;
        text-align: center;
        text-style: bold;
        color: #ff8533;
        margin-bottom: 1;
    }

    #subtitle {
        width: 100%;
        text-align: center;
        color: #8b9bb0;
        margin-bottom: 1;
    }

    .field-label {
        color: #d5dce7;
        margin-top: 1;
        margin-bottom: 1;
        text-style: bold;
    }

    Input {
        width: 100%;
        border: round #354155;
        background: #0b111b;
    }

    Input:focus {
        border: round #ff8533;
    }

    Select {
        width: 100%;
    }

    #actions {
        height: auto;
        margin-top: 1;
    }

    #format {
        width: 1fr;
    }

    #download {
        width: 22;
        margin-left: 1;
        background: #ff8533;
        color: #101010;
        text-style: bold;
    }

    #download:disabled {
        background: #555b65;
        color: #cccccc;
    }

    #progress {
        margin-top: 1;
    }

    #status {
        color: #aebdd0;
        margin-top: 1;
    }

    #logs {
        height: 10;
        border: round #354155;
        background: #0b111b;
        margin-top: 1;
    }

    #bottom {
        height: auto;
        margin-top: 1;
    }

    #clear {
        width: 1fr;
    }

    #open-folder {
        width: 1fr;
        margin-left: 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.is_downloading = False

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with Container(id="panel"):
            yield Static(
                "☁  O P E N C L O U D",
                id="logo",
            )
            yield Static(
                "SoundCloud Audio Downloader | ne_masturbek",
                id="subtitle",
            )

            yield Static(
                "SOUNDCLOUD LINK",
                classes="field-label",
            )
            yield Input(
                placeholder="https://soundcloud.com/artist/track",
                id="url",
            )

            yield Static(
                "SAVE DIRECTORY",
                classes="field-label",
            )
            yield Input(
                value=str(Path.home() / "Downloads"),
                placeholder="C:\\Users\\User\\Downloads",
                id="directory",
            )

            yield Static(
                "OUTPUT FORMAT",
                classes="field-label",
            )

            with Horizontal(id="actions"):
                yield Select(
                    [
                        ("MP3", "mp3"),
                        ("OGG", "vorbis"),
                        ("OPUS", "opus"),
                        ("FLAC", "flac"),
                        ("WAV", "wav"),
                        ("M4A", "m4a"),
                        ("AAC", "aac"),
                    ],
                    value="mp3",
                    allow_blank=False,
                    id="format",
                )

                yield Button(
                    "↓ DOWNLOAD",
                    id="download",
                    variant="primary",
                )

            yield ProgressBar(
                total=100,
                show_eta=False,
                id="progress",
            )

            yield Static(
                "Ready to download",
                id="status",
            )

            yield Static(
                "ACTIVITY LOG",
                classes="field-label",
            )
            yield RichLog(
                id="logs",
                markup=True,
                wrap=True,
                highlight=False,
            )

            with Horizontal(id="bottom"):
                yield Button(
                    "Clear logs",
                    id="clear",
                )
                yield Button(
                    "Open folder",
                    id="open-folder",
                )

        yield Footer()

    def on_mount(self) -> None:
        self.write_log(
            "[green]OpenCloud started successfully[/green]"
        )
        self.write_log(
            "[dim]Paste a SoundCloud link to begin.[/dim]"
        )

    def write_log(self, message: str) -> None:
        self.query_one("#logs", RichLog).write(message)

    def set_status(self, message: str) -> None:
        self.query_one("#status", Static).update(message)

    def set_progress(self, value: float) -> None:
        self.query_one(
            "#progress", ProgressBar
        ).update(progress=max(0, min(100, value)))

    def set_busy(self, busy: bool) -> None:
        self.is_downloading = busy
        self.query_one(
            "#download", Button
        ).disabled = busy

    def action_clear_logs(self) -> None:
        self.query_one("#logs", RichLog).clear()

    def on_button_pressed(
        self, event: Button.Pressed
    ) -> None:
        match event.button.id:
            case "download":
                self.action_start_download()
            case "clear":
                self.action_clear_logs()
            case "open-folder":
                self.open_download_folder()

    def open_download_folder(self) -> None:
        directory = self.query_one(
            "#directory", Input
        ).value.strip()

        if not directory:
            self.notify(
                "Enter a directory",
                severity="warning",
            )
            return

        path = Path(directory).expanduser()

        if not path.is_dir():
            self.notify(
                "Directory does not exist",
                severity="warning",
            )
            return

        try:
            if os.name == "nt":
                os.startfile(str(path))
            else:
                import subprocess
                import sys

                command = (
                    "open"
                    if sys.platform == "darwin"
                    else "xdg-open"
                )
                subprocess.Popen([command, str(path)])
        except Exception as error:
            self.notify(
                str(error),
                severity="error",
            )

    def action_start_download(self) -> None:
        if self.is_downloading:
            self.notify(
                "Download already in progress",
                severity="warning",
            )
            return

        url = self.query_one(
            "#url", Input
        ).value.strip()

        directory = self.query_one(
            "#directory", Input
        ).value.strip()

        audio_format = self.query_one(
            "#format", Select
        ).value

        parsed = urlparse(url)

        allowed_hosts = {
            "soundcloud.com",
            "www.soundcloud.com",
            "m.soundcloud.com",
            "on.soundcloud.com",
        }

        if (
            parsed.scheme != "https"
            or parsed.hostname not in allowed_hosts
            or not parsed.path.strip("/")
        ):
            self.notify(
                "Enter a valid SoundCloud URL",
                severity="error",
            )
            return

        if not directory:
            self.notify(
                "Enter a download directory",
                severity="error",
            )
            return

        if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
            self.notify(
                "FFmpeg / FFprobe not found in PATH",
                severity="error",
            )
            return

        self.set_busy(True)
        self.set_progress(0)
        self.set_status("Connecting to SoundCloud...")

        self.write_log(
            f"[cyan]Starting:[/cyan] {url}"
        )
        self.write_log(
            f"[dim]Format: {audio_format}[/dim]"
        )

        self.download_audio(
            url,
            directory,
            str(audio_format),
        )

    @work(thread=True, exclusive=True)
    def download_audio(
        self,
        url: str,
        directory: str,
        audio_format: str,
    ) -> None:

        try:
            folder = Path(directory).expanduser()
            folder.mkdir(parents=True, exist_ok=True)

            def progress_hook(data: dict) -> None:
                status = data.get("status")

                if status == "downloading":
                    downloaded = data.get(
                        "downloaded_bytes", 0
                    )
                    total = (
                        data.get("total_bytes")
                        or data.get("total_bytes_estimate")
                    )

                    if total:
                        percent = downloaded / total * 100

                        self.call_from_thread(
                            self.set_progress,
                            percent,
                        )
                        self.call_from_thread(
                            self.set_status,
                            f"Downloading: {percent:.1f}%",
                        )

                elif status == "finished":
                    self.call_from_thread(
                        self.set_progress, 100
                    )
                    self.call_from_thread(
                        self.set_status,
                        "Converting audio...",
                    )

            options = {
                "format": "bestaudio/best",
                "outtmpl": str(
                    folder
                    / "%(title).180B [%(id)s].%(ext)s"
                ),
                "noplaylist": True,
                "quiet": True,
                "no_warnings": True,
                "windowsfilenames": True,
                "progress_hooks": [progress_hook],
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": audio_format,
                        "preferredquality": "192",
                    }
                ],
            }

            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(
                    url,
                    download=True,
                )

            title = (
                info.get("title", "Unknown")
                if info
                else "Unknown"
            )

            self.call_from_thread(
                self.set_status,
                "Download completed!",
            )
            self.call_from_thread(
                self.write_log,
                f"[green]SUCCESS:[/green] {title}",
            )
            self.call_from_thread(
                self.write_log,
                f"[dim]Saved to: {folder}[/dim]",
            )
            self.call_from_thread(
                self.notify,
                "Audio downloaded successfully!",
                severity="information",
            )

        except Exception as error:
            self.call_from_thread(
                self.set_status,
                "Download failed",
            )
            self.call_from_thread(
                self.write_log,
                f"[red]ERROR: {error}[/red]",
            )
            self.call_from_thread(
                self.notify,
                "Download failed. Check activity log.",
                severity="error",
            )

        finally:
            self.call_from_thread(
                self.set_busy,
                False,
            )


if __name__ == "__main__":
    OpenCloud().run()

from yt_dlp import YoutubeDL


def download(url, options):
    with YoutubeDL(options) as ydl:
        ydl.download(url)


def download_audio(url):
    options = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
        "outtmpl": "output/%(title)s.%(ext)s",
    }
    download(url, options)


def download_video(url):
    options = {
        "outtmpl": "output/%(title)s.%(ext)s",
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "format_limit": "720p",
    }
    download(url, options)


def download_subtitle(url):
    options = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],
        "outtmpl": "output/%(title)s.%(ext)s",
    }
    download(url, options)

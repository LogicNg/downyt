import os

from download import download_audio, download_subtitle, download_video
from empty_folder import empty_folder
from urls_from_txt import urls_from_txt
from vtt_to_txt import vtt_to_txt


def main():
    empty_folder("output")

    if os.path.isfile("audios.txt"):
        for url in urls_from_txt("audios.txt"):
            download_audio(url)

    if os.path.isfile("videos.txt"):
        for url in urls_from_txt("videos.txt"):
            download_video(url)
            download_subtitle(url)
            vtt_to_txt()


if __name__ == "__main__":
    main()

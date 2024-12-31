import os
from concurrent.futures import ThreadPoolExecutor

from download import download_audio, download_subtitle, download_video
from empty_folder import empty_folder
from urls_from_txt import urls_from_txt
from vtts_to_txts import vtts_to_txts


def download_audio_batch(urls):
    with ThreadPoolExecutor() as executor:
        executor.map(download_audio, urls)


def download_video_batch(urls):
    with ThreadPoolExecutor() as executor:
        for url in urls:
            executor.submit(download_video, url)
            executor.submit(download_subtitle, url)
    vtts_to_txts()


def main():
    empty_folder("output")

    if os.path.isfile("audios.txt"):
        audio_urls = urls_from_txt("audios.txt")
        download_audio_batch(audio_urls)

    if os.path.isfile("videos.txt"):
        video_urls = urls_from_txt("videos.txt")
        download_video_batch(video_urls)


if __name__ == "__main__":
    main()

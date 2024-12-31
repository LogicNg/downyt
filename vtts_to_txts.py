import os
import re

import webvtt


def vtt_paths():
    paths = []
    regex = re.compile("(.*vtt$)")
    for _, _, files in os.walk("output"):
        for file in files:
            if regex.match(file):
                paths.append(f"output/{file}")
    return paths


def vtt_to_txt(path):
    vtt = webvtt.read(path)

    lines = []
    for line in vtt:
        lines.extend(line.text.strip().splitlines())

    previous = None
    transcript = ""
    for line in lines:
        if line == previous:
            continue
        transcript += " " + line
        previous = line

    os.remove(path)

    path = path[:-4] + ".txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(transcript)


def vtts_to_txts():
    paths = vtt_paths()
    for path in paths:
        vtt_to_txt(path)

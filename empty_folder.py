import os
import shutil


def empty_folder(folder):
    if os.path.exists(folder):
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
    else:
        os.makedirs(folder)

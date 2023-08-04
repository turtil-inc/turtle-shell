import zipfile as zf
import os


def unzip():
    with zf.ZipFile(input('file/directory: ')) as f:
        f.extractall()

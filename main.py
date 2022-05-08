__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


# import statements

import os
from posixpath import dirname
import shutil
from zipfile import ZipFile
from os import listdir
from os.path import isfile, join
from pathlib import Path

# 1


def clean_cache():
    try:
        return os.mkdir("cache")
    except FileExistsError:
        shutil.rmtree("cache")
        return os.mkdir("cache")


# 2


def cache_zip(zip_file: str, cache_dir: str):
    with ZipFile(zip_file, "r") as zipObj:
        zipObj.extractall(cache_dir)
        return


# 3


def cached_files():
    
    only_files = [os.path.abspath(f) for f in os.listdir() if isfile(join(f))]

    return only_files


print(cached_files())
result1 = cached_files()
# result2 =

# 4


def find_password(only_files: list):
    for one_file in only_files:
        with open(one_file) as file:
            data = file.readlines()
            for lines in data:
                if "password" in lines:
                    return data
    # print("no password found")


# find_password(result1)

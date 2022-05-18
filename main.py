__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


# import statements

from functools import cache
from importlib.resources import path
import os
from posixpath import dirname
import shutil
from traceback import print_tb
from zipfile import ZipFile
from os import listdir
from os.path import isfile, join
from pathlib import Path

# 1

Dir = "cache"
cur_path = os.getcwd()
Dir_full = os.path.join(cur_path, Dir)


def clean_cache():

    if os.path.isdir(os.path.join(cur_path, Dir)):
        shutil.rmtree(Dir_full)
        return os.mkdir(Dir_full)
    else:
        return os.mkdir(Dir_full)


# 2


def cache_zip(zip_file: str, cache_dir: str):
    with ZipFile(zip_file, "r") as zipObj:
        zipObj.extractall(cache_dir)
        return


# 3


def cached_files():

    # only_files = [os.path.abspath(f) for f in os.listdir(Dir_full) if not os.path.isdir(join(f))]
    only_files2 = []
    for f in os.listdir(Dir_full):
        if f is not os.path.isdir:
            f = os.path.abspath(f)
            only_files2.append(f)

    return only_files2


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
                    return lines
    return print("no password found")


# find_password(result1)

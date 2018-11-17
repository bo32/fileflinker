import os
from pathlib import Path

def get_filename_without_extension(filepath):
    return os.path.splitext(filepath)[0]

def does_directory_exist(path):
    return Path(path).is_dir()

def create_directory(path):
    os.makedirs(path)

def get_home_folder():
    return Path.home()
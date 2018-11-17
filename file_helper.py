import os
from pathlib import Path

def get_filename_without_extension(filepath):
    filename = os.path.split(filepath)[1]
    return os.path.splitext(filename)[0]

def does_directory_exist(path):
    return Path(path).is_dir()

def create_directory(path):
    os.makedirs(path)

def get_home_folder():
    return Path.home()
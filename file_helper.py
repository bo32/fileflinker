import os
from pathlib import Path
import shutil

def get_filename_without_extension(filepath):
    filename = os.path.split(filepath)[1]
    return os.path.splitext(filename)[0]

def does_directory_exist(path):
    return Path(path).is_dir()

def does_file_exist(path):
    return Path(path).is_file()

def create_directory(path):
    os.makedirs(path)

def get_home_folder():
    return Path.home()

def delete_folder(path):
    if (Path(path).is_dir()):
        shutil.rmtree(path)

def empty_folder(path):
    if (Path(path).is_dir()):
        for f in os.listdir(path):
            file_path = os.path.join(path, f)
            if os.path.isfile(file_path):
                os.unlink(file_path)

def get_path(filepath):
    return os.path.split(filepath)[0]

def create_file(filepath):
    path = get_path(filepath)
    if not does_directory_exist(path):
        create_directory(path)
    open(filepath, 'a').close()
    

def copy_file(sources, destination):
    shutil.copy2(sources, destination)
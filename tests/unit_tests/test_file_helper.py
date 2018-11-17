import os 
from sys import platform
import unittest
import getpass
from pathlib import Path
import shutil

import file_helper


class TestFileHelper(unittest.TestCase):

    def setUp(self):
        self.test_path = './test/test2'
        if (Path(self.test_path).is_dir()):
            shutil.rmtree(self.test_path)

    def test_get_home_folder(self):
        candidate = file_helper.get_home_folder()
        expected = ''
        if platform == "linux" or platform == "linux2":
            expected = os.path.join('/home', getpass.getuser())
        elif platform == "win32":
            expected = os.path.join('C:\\Users', getpass.getuser())
        assert(str(candidate) == expected)

    def test_create_directory(self):
        file_helper.create_directory(self.test_path)
        assert(Path(self.test_path).is_dir())

    def test_directory_exists(self):
        file_helper.create_directory(self.test_path)
        assert(file_helper.does_directory_exist(self.test_path))
    
    def test_file_exists(self):
        path = os.path.join('tests','unit_tests','resources','1.jpg')
        assert(file_helper.does_file_exist(path))
    
    def test_file_does_not_exist(self):
        path = os.path.join('tests','unit_tests','resources','does_not_exist.pdf')
        assert(not file_helper.does_file_exist(path))

    def test_get_filename_without_extension(self):
        assert('myfile' == file_helper.get_filename_without_extension('myfile.pdf'))
    
    def test_get_filename_without_extension_with_path(self):
        path = os.path.join('test','test2','myfile.pdf')
        assert('myfile' == file_helper.get_filename_without_extension(path))

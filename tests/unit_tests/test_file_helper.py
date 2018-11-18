import os 
from sys import platform
import unittest
import getpass
from pathlib import Path

import file_helper


class TestFileHelper(unittest.TestCase):

    def setUp(self):
        self.resources_folder = os.path.join('tests', 'unit_tests', 'resources')
        self.test_path = os.path.join(self.resources_folder, 'tmp')
        file_helper.delete_folder(self.test_path)

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
        path = os.path.join(self.resources_folder,'1.jpg')
        assert(file_helper.does_file_exist(path))
    
    def test_file_does_not_exist(self):
        path = os.path.join(self.resources_folder,'does_not_exist.pdf')
        assert(not file_helper.does_file_exist(path))

    def test_get_filename_without_extension(self):
        assert('myfile' == file_helper.get_filename_without_extension('myfile.pdf'))
    
    def test_get_filename_without_extension_with_path(self):
        path = os.path.join('test','test2','myfile.pdf')
        assert('myfile' == file_helper.get_filename_without_extension(path))
    
    def test_create_file(self):
        file_helper.create_file(os.path.join(self.test_path, 'newly_created.txt'))
        assert(len(os.listdir(self.test_path)) == 1)

    def test_get_path(self):
        assert(file_helper.get_path(os.path.join(self.resources_folder,'1.jpg')) == self.resources_folder)

    def test_empty_folder(self):
        file_helper.create_file(os.path.join(self.test_path, 'to_be_removed.txt'))
        file_helper.empty_folder(self.test_path)
        assert(len(os.listdir(self.test_path)) == 0)

    def test_copy_file(self):
        src_folder = os.path.join('tests','unit_tests','resources')
        tgt_folder = os.path.join(src_folder,'tmp')
        print(os.path.join(src_folder,'2.png'))
        print(os.path.join(tgt_folder,'2.png'))
        file_helper.copy_file(
            os.path.join(src_folder,'2.png'),
            os.path.join(tgt_folder,'2.png'))
        assert(len(os.listdir(tgt_folder)) == 1)

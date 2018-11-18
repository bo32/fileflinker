import os
import unittest

import file_helper
from image_collector import ImageCollector

class TestImageCollector(unittest.TestCase):

    def setUp(self):
        self.tmp_folder = os.path.join('tests','unit_tests','resources', 'tmp')
        self.test_destination = os.path.join(self.tmp_folder,'test.cbz')
        self.resources_folder = os.path.join('tests','unit_tests','resources') 
        file_helper.empty_folder(self.tmp_folder)

        self.image_collector = ImageCollector()

    def test_collect_files_as(self):
        self.image_collector.collect_files_as(
            os.path.join(self.resources_folder,'1.jpg'), 
            os.path.join(self.resources_folder,'2.png'), 
            destination=self.test_destination)
        assert(file_helper.does_file_exist(self.test_destination))

    def test_collect_folder_as(self):
        file_helper.copy_file(
            os.path.join(self.resources_folder,'1.jpg'),
            os.path.join(self.tmp_folder,'1.jpg')
            )
        file_helper.copy_file(
            os.path.join(self.resources_folder,'2.png'),
            os.path.join(self.tmp_folder,'2.png'))
        
        self.image_collector.collect_files_from(
            folder=self.tmp_folder,
            destination=self.test_destination)
        assert(file_helper.does_file_exist(self.test_destination))
        
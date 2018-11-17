import os
import unittest

import file_helper
from image_collector import ImageCollector

class TestImageCollector(unittest.TestCase):

    def setUp(self):
        self.test_destination = os.path.join('tests','unit_tests','resources', 'tmp','test.cbz')

    def test_collect_files_as(self):
        image_collector = ImageCollector()
        
        image_collector.collect_files_as(
            os.path.join('tests','unit_tests','resources','1.jpg'), 
            os.path.join('tests','unit_tests','resources','2.png'), 
            destination=self.test_destination)
        assert(file_helper.does_file_exist(self.test_destination))
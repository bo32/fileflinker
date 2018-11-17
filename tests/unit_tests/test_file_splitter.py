import os
import unittest 
from pathlib import Path
import shutil

import config
from pdf_splitter import PDFSplitter

class TestFileSplitter(unittest.TestCase):

    def setUp(self):
        self.test_destination_path = os.path.join('tests', 'unit_tests', 'resources','tmp')
        if (Path(self.test_destination_path).is_dir()):
            shutil.rmtree(self.test_destination_path)


    def test_to_images(self):
        pdf_splitter = PDFSplitter()
        pdf_splitter.to_images(
            'jpg', 
            os.path.join('tests', 'unit_tests', 'resources','test.pdf'), 
            destination = self.test_destination_path)
        count = len(os.listdir(self.test_destination_path))
        assert(count == 2)

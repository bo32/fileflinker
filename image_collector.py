import os
import zipfile

import file_helper
import config

class ImageCollector:
    def __init__(self):
        pass

    def collect_files_as(self, *files, destination=config.DEFAULT_CBZ_DESTINATION):
        zip = zipfile.ZipFile(destination, 'w', zipfile.ZIP_STORED)
        for file in files:
            zip.write(file)
        zip.close()
    
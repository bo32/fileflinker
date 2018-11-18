import os
import zipfile

import file_helper
import config

class ImageCollector:
    def __init__(self):
        pass

    def collect_files_as(self, *files, destination=config.DEFAULT_CBZ_DESTINATION):
        zip = zipfile.ZipFile(destination, 'w', zipfile.ZIP_STORED)
        for f in files:
            print('Processing %s' % f)
            zip.write(f)
        zip.close()
        print('Archive %s successfully created' % destination)
    
    def collect_files_from(self, folder=config.DEFAULT_TEMP_FOLDER, destination=config.DEFAULT_CBZ_DESTINATION):
        self.collect_files_as(*(os.path.join(folder, f) for f in os.listdir(folder)), destination=destination)
    
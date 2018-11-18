import file_helper
import os
import logging

import config

"""Splits a PDF into JPG images (one per page).
The JPG images are stored in a temp folder in ~/.fileflinker.

Big thanks to https://nedbatchelder.com/blog/200712/extracting_jpgs_from_pdfs.html
for the implementation.

:raises Exception: if the end of the PDF stream was not found.
:raises Exception: if the end of a JPG image was not found.
"""
class PDFSplitter:

    def __init__(self):
        self.logger = logging.getLogger(PDFSplitter.__name__)

    def to_images(self, format, filepath, destination = config.DEFAULT_TEMP_FOLDER):
        pdf = open(filepath, 'rb').read()
        i = 0
        startmark = b'\xff\xd8'
        startfix = 0
        endmark = b'\xff\xd9'
        endfix = 2
        njpg = 0

        filename = file_helper.get_filename_without_extension(filepath)
        while True:
            istream = pdf.find(b'stream', i)
            if istream < 0:
                if njpg == 0:
                    raise Exception("The PDF couldn't be split.")
                self.logger.info('Successfully split the PDF %s' % filepath)
                self.logger.info('%d resulting files stored in %s' % (njpg, destination))
                break
            istart = pdf.find(startmark, istream, istream+20)
            if istart < 0:
                i = istream+20
                continue
            iend = pdf.find(b'endstream', istart)
            if iend < 0:
                raise Exception("Didn't find end of stream!")
            iend = pdf.find(endmark, iend-20)
            if iend < 0:
                raise Exception("Didn't find end of JPG!")
            
            istart += startfix
            iend += endfix
            jpg = pdf[istart:iend]

            if not file_helper.does_directory_exist(destination):
                file_helper.create_directory(destination)
            jpgfile = open(os.path.join(destination, '%s%d.%s' % (filename, njpg, format)), 'wb')
            jpgfile.write(jpg)
            jpgfile.close()
            
            njpg += 1
            i = iend
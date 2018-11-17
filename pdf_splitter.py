import file_helper
import os
import io

"""Splits a PDF into JPG images (one per page).
The JPG images are stored in a temp folder in ~/.fileflinker.

Big thanks to https://nedbatchelder.com/blog/200712/extracting_jpgs_from_pdfs.html
for the implementation.

:raises Exception: if the end of the PDF stream was not found.
:raises Exception: if the end of a JPG image was not found.
"""
class PDFSplitter:
    def __init__(self):
        pass

    def to_images(self, format, filepath):
        pdf = open(filepath, 'rb').read()
        i = 0
        startmark = b'\xff\xd8'
        startfix = 0
        endmark = b'\xff\xd9'
        endfix = 2
        njpg = 0

        filename = file_helper.get_filename_without_extension(filepath)
        print(filename)
        while True:
            istream = pdf.find(b'stream', i)
            if istream < 0:
                if njpg == 0:
                    raise Exception("The PDF couldn't be split.")
                print('Successfully split the PDF: %d resulting files.' % njpg)
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

            tmp_folder = os.path.join(file_helper.get_home_folder(), '.fileflinker/tmp')
            if not file_helper.does_directory_exist(tmp_folder):
                file_helper.create_directory(tmp_folder)
            jpgfile = open(os.path.join(tmp_folder, '%s%d.%s' % (filename, njpg, format)), 'wb')
            jpgfile.write(jpg)
            jpgfile.close()
            
            njpg += 1
            i = iend
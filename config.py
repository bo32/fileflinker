import os
import file_helper
import datetime

DEFAULT_FOLDER = os.path.join(
    file_helper.get_home_folder(), 
    '.fileflinker')
DEFAULT_TEMP_FOLDER = os.path.join(
    DEFAULT_FOLDER,
    'tmp')
DEFAULT_CBZ_DESTINATION = os.path.join(
    DEFAULT_FOLDER,
    '%s.cbz' % datetime.datetime.now().timestamp())
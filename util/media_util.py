# NavUtils
# @author Paul Ottley
# @copyright 2021

import exifread
from objects import FSfile
from util import FileUtils


class MediaUtils:

    @staticmethod
    def get_date_taken(file: FSfile) -> str:
        #TODO Implement data take for png, videos and other file types
        date_taken = ""
        full_filename = FileUtils.join_filepath(file.get_src_dir(), file.get_filename())
        with open(full_filename, 'rb') as fh:
            tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
            if len(tags) > 0:
                date_taken = tags["EXIF DateTimeOriginal"]
            else:
                tags = exifread.process_file(fh, stop_tag="EXIF DateTimeDigitized")
                if len(tags) > 0:
                    date_taken = tags["EXIF DateTimeDigitized"]

        return date_taken

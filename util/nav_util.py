# NavUtils
# @author Paul Ottley
# @copyright 2021
import os

from util import FileUtils
from objects import FSfile

class NavUtils:

    # Walk a directory and gather file and directory information to a collection of objects
    @staticmethod
    def walk_dir(start_dir):
        # Build empty container for the files
        all_files = []

        if os.path.isdir(start_dir):
            # Walk the directory and count the files
            for root, dirs, files in os.walk(start_dir):
                for filename in files:
                    full_filename: str = FileUtils.join_filepath(root, filename)

                    # Step 1: Build the file object with name and location
                    currFile = FSfile()
                    currFile.set_filename(filename)
                    currFile.set_src_dir(root)

                    # Step 2: Add metadata of size and date to object
                    currFile.set_size(FileUtils.get_file_size(full_filename))
                    currFile.set_date_taken(FileUtils.get_file_size(full_filename))

                    # Step 3: Determine file type and tag
                    currFile.set_type(FileUtils.get_file_type(filename))
                    currFile.set_media_tag(FileUtils.get_media_type(filename))

                    # Step 4: Add file to collection
                    all_files.append(currFile)

        return all_files

# NavUtils
# @author Paul Ottley
# @copyright 2021
import os

from util import FileUtils, MediaUtils
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
                    curr_file = FSfile()
                    curr_file.set_filename(filename)
                    curr_file.set_src_dir(root)

                    # Step 2: Add metadata of size and date to object
                    curr_file.set_size(FileUtils.get_file_size(full_filename))
                    curr_file.set_date_taken(MediaUtils.get_date_taken(curr_file))

                    # Step 3: Determine file type and tag
                    curr_file.set_type(FileUtils.get_file_type(filename))
                    curr_file.set_media_tag(FileUtils.get_media_type(filename))

                    # Step 4: Add file to collection
                    all_files.append(curr_file)

        return all_files

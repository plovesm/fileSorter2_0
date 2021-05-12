# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import datetime
import time

from util.file_util import FileUtils

STR_DIR1: str = r"C:\Users\ott19\Pictures"
TGT_DIR1: str = r"C:\Users\ott19\Desktop\TGTsorted"
SEPARATOR: str = "\\"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def walk_dir(dir_to_walk, tgt_dir):
    print("Start")

    # Print time started
    ts = time.time()
    start_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print("Walk Dir started at {0}:".format(start_time))
    # print("Test size: " + str(FileUtils.get_file_size("C:\\Users\\ott19\\Pictures\\IMG_3594.MOV")))

    # Build empty container for the files
    all_files = []

    if os.path.isdir(dir_to_walk):
        # Walk the directory and count the files
        for root, dirs, files in os.walk(dir_to_walk):
            for file in files:
                full_filename: str = root + SEPARATOR + file
                print("Full name: " + full_filename)
                print("Size: " + str(FileUtils.get_file_size(full_filename)))

                # Step 1: Build the file object with name and location

                # Step 2: Add metadata of size and date to object

                # Step 3: Determine file type and tag

                # Step 4: Add file to collection

        # Print time ended
        ts2 = time.time()
        end_time = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
        print("Walk Dir completed at {0} with {1} files collected.".format(end_time, len(files)))

    return all_files


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    walk_dir(STR_DIR1, TGT_DIR1)

# PHASE ONE

# Set start and target file folders

# Recursively crawl folder

# Parse info to flat file db

# PHASE TWO

# Read flat file

# Prep Summary

# PHASE THREE

# Create directory structure by file type, then years, then months

# Copy or move files to new structure

# PHASE THREE B

# Check for duplicates

# Mark Duplicates

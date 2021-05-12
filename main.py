# Main point of application execution
# @author Paul Ottley
# @copyright 2021
import datetime

# Define Default Start and Target Directories
from util.nav_util import NavUtils

START_DIRECTORY: str = r"C:\Users\ott19\Pictures"
TARGET_DIRECTORY: str = r"C:\Users\ott19\Desktop\TGTsorted"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Print time started
    start_time = datetime.datetime.now()
    str_start_time = start_time.strftime('%Y-%m-%d %H:%M:%S')
    print("Program started at {0}:".format(str_start_time))

    # PHASE ONE

    # Fill up the collection from a given directory by recursively crawl folder
    all_files = NavUtils.walk_dir(START_DIRECTORY)
    print(all_files[0])
    #TODO Parse info to flat file db

    # PHASE TWO

    #TODO Read flat file

    #TODO Prep Summary

    # PHASE THREE

    #TODO Create directory structure by file type, then years, then months

    #TODO Copy or move files to new structure

    # PHASE THREE B

    #TODO Check for duplicates

    #TODO Mark Duplicates

    # Print time ended
    end_time = datetime.datetime.now()
    str_end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
    duration = end_time - start_time
    print("Program completed in {0} at {1} with {2} files collected.".format(duration, str_end_time, len(all_files)))

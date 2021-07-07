"""
ingest.py

When a drive gets plugged into a computer, this script will scan
the drive and for the files created within a certain time, and
automatically create a new folder on the NAS and copy the files
to the folder on the NAS.
"""

import os
import glob
import shutil
import time
from posix import listdir
import datetime
from os import path

# Global Vairables

# These are the two paths for coping while testing
# Source_path will be changed to be able to detect a new drive.
# NOTE: make sure that you put the correct path in depending on
# opterating system that you are using
destination_path = "/mnt/c/Users/chang/Desktop/copy_to/"

source_path = "/mnt/c/Users/chang/Desktop/source/"


# this function will copy all the files in a srouce dirctory to
# a destination directory
# EXAMPLE: copy_all_files(source_path, destination_path, "*.docx")
def copy_all_files(src, dest, type):
    # source_files = os.listdir(src)
    files = glob.iglob(os.path.join(src, type))
    for file_name in files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)


# This function will a create folder based on the time of the day
# giving the folder the name of the service, ready for the files to
# be copied in to.
def create_service_folder(dest):
    # getting the time
    time_now = datetime.datetime.now()

    # setting whether the church service is AM or PM
    if datetime.datetime.now().hour < 14:
        service_time = time.strftime("%Y%m%d-") + "Sunday-Morning-Church"
    else:
        service_time = time.strftime("%Y%m%d-") + "Sunday-Night-Church"

    folder = dest + service_time

    if os.path.exists(folder):
        new_folder_destination = folder
        print("Folder Already exists")
    else:
        os.makedirs(folder)
        new_folder_destination = folder
        print("Folder created")

    return new_folder_destination




# Testing section

copy_destination = create_service_folder(destination_path)

copy_all_files(source_path, copy_destination, "*.docx")
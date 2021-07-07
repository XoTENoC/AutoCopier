import os
import glob
import shutil

# this function will only copy certain files for a source directory
# to a destination directory
def copy_certain_files(src, dest, filenames):
    for file in filenames:
        full_file_name = os.path.join(src, file)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)


# this function will check all the source files against the
# destinaiton files and will return a list of all the source files
# that aren't in the destination directory
def different_files(src, dest, type):
    filenames = []

    files = glob.iglob(os.path.join(src, type))
    if len(os.listdir(dest)) == 0:
        filenames.append(os.listdir(src))
    else:
        for src_filename in os.listdir(files):
            match = 0
            for dest_filename in os.listdir(dest):
                if src_filename == dest_filename:
                    match = 1
            if match != 1:
                filenames.append(src_filename)

    return filenames


# Testing section
# files_to_copy = different_files(source_path, destination_path, "*.docx")
# different_files(source_path, destination_path, "*.docx")

# print(files_to_copy)

# copy_certain_files(source_path, destination_path, files_to_copy)

# print(create_service_folder(destination_path))
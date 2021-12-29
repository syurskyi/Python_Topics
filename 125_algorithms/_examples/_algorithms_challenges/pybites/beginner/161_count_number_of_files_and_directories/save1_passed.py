import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dir_count = 0
    file_count = 0
    for root, dirs, files in os.walk(directory):
        dir_count += len(dirs)
        file_count += len(files)
    return dir_count, file_count
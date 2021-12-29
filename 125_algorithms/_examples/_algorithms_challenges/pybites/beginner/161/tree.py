import os, os.path


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    filecount, dircount = 0, 0
    for root, dirs, files in os.walk(directory):
        filecount += len(files)
        dircount += len(dirs)
    return( dircount, filecount )

print(count_dirs_and_files('C:\\Users\\Swee-Chuan Khoo\\Documents\\covic19_MoH\\covid19-public'))
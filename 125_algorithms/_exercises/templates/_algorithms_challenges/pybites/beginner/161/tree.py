_______ os, os.path


___ count_dirs_and_files(directory='.'
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    filecount, dircount = 0, 0
    ___ root, dirs, files __ os.walk(directory
        filecount += l..(files)
        dircount += l..(dirs)
    r..( dircount, filecount )

print(count_dirs_and_files('C:\\Users\\Swee-Chuan Khoo\\Documents\\covic19_MoH\\covid19-public'))
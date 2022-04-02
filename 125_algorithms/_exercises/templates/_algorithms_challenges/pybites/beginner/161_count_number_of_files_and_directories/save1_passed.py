_______ __


___ count_dirs_and_files(directory='.'
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dir_count = 0
    file_count = 0
    ___ root, dirs, files __ __.walk(directory
        dir_count += l..(dirs)
        file_count += l..(files)
    r.. dir_count, file_count
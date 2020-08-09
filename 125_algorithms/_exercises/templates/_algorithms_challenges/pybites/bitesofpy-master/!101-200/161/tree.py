______ os


___ count_dirs_and_files(directory='.'
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    count_dir = count_files = 0
    ___ _, dir, files in os.walk(directory
        count_dir += le.(dir)
        count_files += le.(files)
    r_ count_dir, count_files

_______ os


___ count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    count_dir = count_files = 0
    ___ _, dir, files __ os.walk(directory):
        count_dir += l..(dir)
        count_files += l..(files)
    r.. count_dir, count_files

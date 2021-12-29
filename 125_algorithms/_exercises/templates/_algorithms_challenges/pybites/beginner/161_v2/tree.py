_______ os


___ count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """

    
    directories = files =  0
    ___ root,subdir,file __ os.walk(directory):
        directories += l..(subdir)
        files += l..(file)



    r.. directories,files



__ __name__ __ "__main__":


    count_dirs_and_files()

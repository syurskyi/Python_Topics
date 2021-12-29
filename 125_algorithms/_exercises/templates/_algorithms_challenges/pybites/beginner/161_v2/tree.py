import os


___ count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """

    
    directories = files =  0
    for root,subdir,file in os.walk(directory):
        directories += len(subdir)
        files += len(file)



    return directories,files



__ __name__ == "__main__":


    count_dirs_and_files()

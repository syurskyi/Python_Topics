______ __

'''
    For the given path, get the List of all files in the directory tree 
'''


___ getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile _ __.l_d_(dirName)
    allFiles _ list()
    # Iterate over all the entries
    ___ entry __ listOfFile:
        # Create full path
        fullPath _ __.p...j..(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        __ __.p...isdir(fullPath):
            allFiles _ allFiles + getListOfFiles(fullPath)
        ____
            allFiles.append(fullPath)

    return allFiles


___ main():
    dirName _ '.'

    # Get the list of all files in directory tree at given path
    listOfFiles _ getListOfFiles(dirName)

    # Print the files
    ___ elem __ listOfFiles:
        print(elem)

    print ("****************")

    # Get the list of all files in directory tree at given path
    listOfFiles _ list()
    ___ (dirpath, dirnames, filenames) __ __.walk(dirName):
        listOfFiles +_ [__.p...j..(dirpath, file) ___ file __ filenames]

    # Print the files
    ___ elem __ listOfFiles:
        print(elem)


__ __name__ == '__main__':
    main()

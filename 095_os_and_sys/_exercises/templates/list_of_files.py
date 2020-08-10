______ os

'''
    For the given path, get the List of all files in the directory tree 
'''


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    ___ entry __ listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def main():
    dirName = '.'

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)

    # Print the files
    ___ elem __ listOfFiles:
        print(elem)

    print ("****************")

    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    ___ (dirpath, dirnames, filenames) __ os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) ___ file __ filenames]

    # Print the files
    ___ elem __ listOfFiles:
        print(elem)


if __name__ == '__main__':
    main()

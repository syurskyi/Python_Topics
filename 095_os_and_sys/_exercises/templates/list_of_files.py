# ______ __
#
# '''
#     For the given path, get the List of all files in the directory tree
# '''
#
#
# ___ getListOfFiles dirName
#     # create a list of file and sub directories
#     # names in the given directory
#     listOfFile _ __.l_d_ ?
#     allFiles _ li..
#     # Iterate over all the entries
#     ___ entry __ ?
#         # Create full path
#         fullPath _ __.p...j.. d.. ?
#         # If entry is a directory then get the list of files in this directory
#         __ __.p...i_d.. ?
#             allFiles _ ? + ? f..
#         ____
#             ?.ap.. ?
#
#     r_ ?
#
#
# ___ main
#     dirName _ '.'
#
#     # Get the list of all files in directory tree at given path
#     listOfFiles _ ? ?
#
#     # Print the files
#     ___ elem __ ?
#         print ?
#
#     print ("****************")
#
#     # Get the list of all files in directory tree at given path
#     listOfFiles _ li..
#     ___ (dirpath, dirnames, filenames) __ __.w.. d..
#         ? +_ |__.p...j.. d.. file ___ ? __ ?
#
#     # Print the files
#     ___ elem __ ?
#         print ?
#
# __ ______ __ ______
#     ?

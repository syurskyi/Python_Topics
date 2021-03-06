# # A common programming task is walking a directory tree and processing files in the tree. Let’s explore how the
# # built-in Python function os.walk() can be used to do this. os.walk() is used to generate filename in a directory
# # tree by walking the tree either top-down or bottom-up. For the purposes of this section, we’ll be manipulating
# # the following directory tree:
# #
# # .
# # |
# # ├── folder_1/
# # |   ├── file1.py
# # |   ├── file2.py
# # |   └── file3.py
# # |
# # ├── folder_2/
# # |   ├── file4.py
# # |   ├── file5.py
# # |   └── file6.py
# # |
# # ├── test1.txt
# # └── test2.txt
# #
# # The following is an example that shows you how to list all files and directories in a directory tree using os.walk().
# # os.walk() defaults to traversing directories in a top-down manner:
# # # Walking a directory tree and printing the names of the directories and files
#
# ______ __
# ___ dirpath, dirnames, files __ __.w.. '.'
#     print _*Found directory: |d..
#     ___ file_name __ f..
#         print ?
#
# # os.walk() returns three values on each iteration of the loop:
# #
# #     The name of the current folder
# #     A list of folders in the current folder
# #     A list of files in the current folder
# # On each iteration, it prints out the names of the subdirectories and files it finds:
# #
# # Found directory: .
# # test1.txt
# # test2.txt
# # Found directory: ./folder_1
# # file1.py
# # file3.py
# # file2.py
# # Found directory: ./folder_2
# # file4.py
# # file5.py
# # file6.py
# #
# # To traverse the directory tree in a bottom-up manner, pass in a topdown=False keyword argument to os.walk():
#
# ___ dirpath, dirnames, files __ __.w.. '.' topdown_F..
#     print _*Found directory: |?
#     ___ file_name __ ?
#         print ?
#
# # Passing the topdown=False argument will make os.walk() print out the files it finds in the subdirectories first:
# #
# # Found directory: ./folder_1
# # file1.py
# # file3.py
# # file2.py
# # Found directory: ./folder_2
# # file4.py
# # file5.py
# # file6.py
# # Found directory: .
# # test1.txt
# # test2.txt
# #
# # As you can see, the program started by listing the contents of the subdirectories before listing the contents
# # of the root directory. This is very useful in situations where you want to recursively delete files and directories.
# # You will learn how to do this in the sections below. By default, os.walk does not walk down into symbolic links that
# # resolve to directories. This behavior can be overridden by calling it with a followlinks=True argument.
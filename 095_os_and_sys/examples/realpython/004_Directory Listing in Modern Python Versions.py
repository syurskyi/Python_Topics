# In modern versions of Python, an alternative to os.listdir() is to use os.scandir() and pathlib.Path().
#
# os.scandir() was introduced in Python 3.5 and is documented in PEP 471. os.scandir() returns an iterator as opposed
# to a list when called:

import os
entries = os.scandir('my_directory/')
print(entries)

# <posix.ScandirIterator object at 0x7f5b047f3690>
#
# The ScandirIterator points to all the entries in the current directory. You can loop over the contents
# of the iterator and print out the filenames:
#
import os

with os.scandir('my_directory/') as entries:
    for entry in entries:
        print(entry.name)

# Here, os.scandir() is used in conjunction with the with statement because it supports the context manager protocol.
# Using a context manager closes the iterator and frees up acquired resources automatically after the iterator
# has been exhausted. The result is a print out of the filenames in my_directory/ just like you saw in the os.listdir()
# example:
#
# sub_dir_c
# file1.py
# sub_dir_b
# file3.txt
# file2.csv
# sub_dir
#
# Another way to get a directory listing is to use the pathlib module:
print()

from pathlib import Path

entries = Path('my_directory/')
for entry in entries.iterdir():
    print(entry.name)
#
# The objects returned by Path are either PosixPath or WindowsPath objects depending on the OS.
#
# pathlib.Path() objects have an .iterdir() method for creating an iterator of all files and folders in a directory.
# Each entry yielded by .iterdir() contains information about the file or directory such as its name
# and file attributes. pathlib was first introduced in Python 3.4 and is a great addition to Python that provides
# an object oriented interface to the filesystem.
# In the example above, you call pathlib.Path() and pass a path argument to it. Next is the call to .iterdir()
# to get a list of all files and directories in my_directory.
#
# pathlib offers a set of classes featuring most of the common operations on paths in an easy, object-oriented way.
# Using pathlib is more if not equally efficient as using the functions in os. Another benefit of using pathlib
# over os is that it reduces the number of imports you need to make to manipulate filesystem paths.
# For more information, read Python 3’s pathlib Module: Taming the File System.
#
# Running the code above produces the following:
#
# sub_dir_c
# file1.py
# sub_dir_b
# file3.txt
# file2.csv
# sub_dir
#
# Using pathlib.Path() or os.scandir() instead of os.listdir() is the preferred way of getting a directory listing,
# especially when you’re working with code that needs the file type and file attribute information. pathlib.Path() o
# ffers much of the file and path handling functionality found in os and shutil, and it’s methods are more efficient
# than some found in these modules. We will discuss how to get file properties shortly.
#
# Here are the directory-listing functions again:
# Function 	Description
# os.listdir() 	Returns a list of all files and folders in a directory
# os.scandir() 	Returns an iterator of all the objects in a directory including file attribute information
# pathlib.Path.iterdir() 	Returns an iterator of all the objects in a directory including file attribute information
#
# These functions return a list of everything in the directory, including subdirectories.
# This might not always be the behavior you want. The next section will show you how to filter the results from
# a directory listing.
# This section will show you how to print out the names of files in a directory using os.listdir(), os.scandir(),
# and pathlib.Path(). To filter out directories and only list files from a directory listing produced by os.listdir(),
# use os.path:
#
import os

# List all files in a directory using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

print()
print()
#
# Here, the call to os.listdir() returns a list of everything in the specified path, and then that list is filtered
# by os.path.isfile() to only print out files and not directories. This produces the following output:
#
# file1.py
# file3.txt
# file2.csv
#
# An easier way to list files in a directory is to use os.scandir() or pathlib.Path():
#
import os

# List all files in a directory using scandir()
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

print()
print()

# Using os.scandir() has the advantage of looking cleaner and being easier to understand than using os.listdir(),
# even though it is one line of code longer. Calling entry.is_file() on each item in the ScandirIterator returns
# True if the object is a file. Printing out the names of all files in the directory gives you the following output:
#
# file1.py
# file3.txt
# file2.csv
#
# Here’s how to list files in a directory using pathlib.Path():

from pathlib import Path

basepath = Path('my_directory/')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)

print()
print()

# Here, you call .is_file() on each entry yielded by .iterdir(). The output produced is the same:
#
# file1.py
# file3.txt
# file2.csv
#
# The code above can be made more concise if you combine the for loop and the if statement into
# a single generator expression. Dan Bader has an excellent article on generator expressions and list comprehensions.
#
# The modified version looks like this:

from pathlib import Path

# List all files in directory using pathlib
basepath = Path('my_directory/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(item.name)

# This produces exactly the same output as the example before it. This section showed that filtering files
# or directories using os.scandir() and pathlib.Path() feels more intuitive and looks cleaner than using os.listdir()
# in conjunction with os.path.
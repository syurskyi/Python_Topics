# Another useful module for pattern matching is glob.
# .glob() in the glob module works just like fnmatch.fnmatch(), but unlike fnmatch.fnmatch(), it treats files beginning
# with a period (.) as special. UNIX and related systems translate name patterns with wildcards like ? and * into
# a list of files. This is called globbing.
#
# For example, typing mv *.py python_files/ in a UNIX shell moves (mv) all files with the .py extension from
# the current directory to the directory python_files. The * character is a wildcard that means “any number
# of characters,” and *.py is the glob pattern. This shell capability is not available in the Windows Operating System.
# The glob module adds this capability in Python, which enables Windows programs to use this feature.
#
# Here’s an example of how to use glob to search for all Python (.py) source files in the current directory:

import glob
glob.glob('*.py')
# ['admin.py', 'tests.py']

# glob.glob('*.py') searches for all files that have the .py extension in the current directory and returns them
# as a list. glob also supports shell-style wildcards to match patterns:

import glob
for name in glob.glob('*[0-9]*.txt'):
    print(name)

# This finds all text (.txt) files that contain digits in the filename:
#
# data_01.txt
# data_03.txt
# data_03_backup.txt
# data_02_backup.txt
# data_02.txt
# data_01_backup.txt
#
# glob makes it easy to search for files recursively in subdirectories too:

import glob
for file in glob.iglob('**/*.py', recursive=True):
    print(file)

# This example makes use of glob.iglob() to search for .py files in the current directory and subdirectories.
# Passing recursive=True as an argument to .iglob() makes it search for .py files in the current directory and
# any subdirectories. The difference between glob.iglob() and glob.glob() is that .iglob() returns an iterator instead
# of a list.
#
# Running the program above produces the following:
#
# admin.py
# tests.py
# sub_dir/file1.py
# sub_dir/file2.py
#
# pathlib contains similar methods for making flexible file listings. The example below shows how you can
# use .Path.glob() to list file types that start with the letter p:

from pathlib import Path
p = Path('.')
for name in p.glob('*.p*'):
    print(name)

# admin.py
# scraper.py
# docs.pdf
#
# Calling p.glob('*.p*') returns a generator object that points to all files in the current directory that start with
# the letter p in their file extension. Path.glob() is similar to os.glob() discussed above. As you can see,
# pathlib combines many of the best features of the os, os.path, and glob modules into one single module, which makes
# it a joy to use.
#
# To recap, here is a table of the functions we have covered in this section:
# Function 	Description
# startswith() 	Tests if a string starts with a specified pattern and returns True or False
# endswith() 	Tests if a string ends with a specified pattern and returns True or False
# fnmatch.fnmatch(filename, pattern) 	Tests whether the filename matches the pattern and returns True or False
# glob.glob() 	Returns a list of filenames that match a pattern
# pathlib.Path.glob() 	Finds patterns in path names and returns a generator object

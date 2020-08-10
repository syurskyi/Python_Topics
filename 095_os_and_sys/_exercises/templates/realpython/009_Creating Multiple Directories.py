# os.makedirs() is similar to os.mkdir(). The difference between the two is that not only can os.makedirs()
# create individual directories, it can also be used to create directory trees. In other words,
# it can create any necessary intermediate folders in order to ensure a full path exists.
#
# os.makedirs() is similar to running mkdir -p in Bash. For example, to create a group of directories like 2018/10/05,
# all you have to do is the following:

import os
os.makedirs('2018/10/05')

# This will create a nested directory structure that contains the folders 2018, 10, and 05:
#
# .
# |
# └── 2018/
#     └── 10/
#         └── 05/
#
# .makedirs() creates directories with default permissions. If you need to create directories with different permissions
# call .makedirs() and pass in the mode you would like the directories to be created in:

import os
os.makedirs('2018/10/05', mode=0o770)

# This creates the 2018/10/05 directory structure and gives the owner and group users read, write,
# and execute permissions. The default mode is 0o777, and the file permission bits of existing parent directories
# are not changed. For more details on file permissions, and how the mode is applied, see the docs.
#
# Run tree to confirm that the right permissions were applied:
#
# $ tree -p -i .
# .
# [drwxrwx---]  2018
# [drwxrwx---]  10
# [drwxrwx---]  05
#
# This prints out a directory tree of the current directory. tree is normally used to list contents of directories in
# a tree-like format. Passing the -p and -i arguments to it prints out the directory names and their file permission
# information in a vertical list. -p prints out the file permissions, and -i makes tree produce a vertical list without
# indentation lines. As you can see, all of the directories have 770 permissions. An alternative way
# to create directories is to use .mkdir() from pathlib.Path:

import pathlib

p = pathlib.Path('2018/10/05')
p.mkdir(parents=True)

# Passing parents=True to Path.mkdir() makes it create the directory 05 and any parent directories necessary to make
# the path valid.
# By default, os.makedirs() and Path.mkdir() raise an OSError if the target directory already exists.
# This behavior can be overridden (as of Python 3.2) by passing exist_ok=True as a keyword argument when calling each
# function.
#
# Running the code above produces a directory structure like the one below in one go:
#
# .
# |
# └── 2018/
#     └── 10/
#         └── 05/
#
# I prefer using pathlib when creating directories because I can use the same function to create single or nested directories.
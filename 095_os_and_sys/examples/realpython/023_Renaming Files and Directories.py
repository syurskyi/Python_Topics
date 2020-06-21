# Python includes os.rename(src, dst) for renaming files and directories:

import os

os.rename('first.zip', 'first_01.zip')

# The line above will rename first.zip to first_01.zip. If the destination path points to a directory, it will raise an OSError.
#
# Another way to rename files or directories is to use rename() from the pathlib module:

from pathlib import Path
data_file = Path('data_01.txt')
data_file.rename('data.txt')

# To rename files using pathlib, you first create a pathlib.Path() object that contains a path to the file you want
# to replace. The next step is to call rename() on the path object and pass a new filename for the file or directory
# you’re renaming.

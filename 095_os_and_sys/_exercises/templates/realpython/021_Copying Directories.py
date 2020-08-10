# While shutil.copy() only copies a single file, shutil.copytree() will copy an entire directory and everything
# contained in it. shutil.copytree(src, dest) takes two arguments: a source directory and the destination directory
# where files and folders will be copied to.
#
# Here’s an example of how to copy the contents of one folder to a different location:
#
import shutil
shutil.copytree('data_1', 'data1_backup')

# 'data1_backup'
#
# In this example, .copytree() copies the contents of data_1 to a new location data1_backup and returns the destination
# directory. The destination directory must not already exist. It will be created as well
# as missing parent directories. shutil.copytree() is a good way to back up your files.


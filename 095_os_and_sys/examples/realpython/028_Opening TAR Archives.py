# TAR files are uncompressed file archives like ZIP. They can be compressed using gzip, bzip2,
# and lzma compression methods. The TarFile class allows reading and writing of TAR archives.
#
# Do this to read from an archive:

import tarfile

with tarfile.open('example.tar', 'r') as tar_file:
    print(tar_file.getnames())

# tarfile objects open like most file-like objects. They have an open() function that takes a mode
# that determines how the file is to be opened.
#
# Use the 'r', 'w' or 'a' modes to open an uncompressed TAR file for reading, writing, and appending, respectively.
# To open compressed TAR files, pass in a mode argument to tarfile.open() that is in the form filemode[:compression].
# The table below lists the possible modes TAR files can be opened in:
# Mode 	Action
# r 	Opens archive for reading with transparent compression
# r:gz 	Opens archive for reading with gzip compression
# r:bz2 	Opens archive for reading with bzip2 compression
# r:xz 	Opens archive for reading with lzma compression
# w 	Opens archive for uncompressed writing
# w:gz 	Opens archive for gzip compressed writing
# w:xz 	Opens archive for lzma compressed writing
# a 	Opens archive for appending with no compression
#
# .open() defaults to 'r' mode. To read an uncompressed TAR file and retrieve the names
# of the files in it, use .getnames():

import tarfile
import time

tar = tarfile.open('example.tar', mode='r')
tar.getnames()
# ['CONTRIBUTING.rst', 'README.md', 'app.py']
#
# This returns a list with the names of the archive contents.
#
# Note: For the purposes of showing you how to use different tarfile object methods, the TAR file in the examples
# is opened and closed manually in an interactive REPL session.
# Interacting with the TAR file this way allows you to see the output of running each command.
# Normally, you would want to use a context manager to open file-like objects.
#
# The metadata of each entry in the archive can be accessed using special attributes:

for entry in tar.getmembers():
    print(entry.name)
    print(' Modified:', time.ctime(entry.mtime))
    print(' Size    :', entry.size, 'bytes')
    print()

# CONTRIBUTING.rst
#  Modified: Sat Nov  1 09:09:51 2018
#  Size    : 402 bytes
#
# README.md
#  Modified: Sat Nov  3 07:29:40 2018
#  Size    : 5426 bytes
#
# app.py
#  Modified: Sat Nov  3 07:29:13 2018
#  Size    : 6218 bytes
#
# In this example, you loop through the list of files returned by .getmembers() and print out each file’s attributes.
# The objects returned by .getmembers() have attributes that can be accessed programmatically such as the name, size,
# and last modified time of each of the files in the archive. After reading or writing to the archive,
# it must be closed to free up system resources.
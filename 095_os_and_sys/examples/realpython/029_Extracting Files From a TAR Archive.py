# In this section, you’ll learn how to extract files from TAR archives using the following methods:
#
#     .extract()
#     .extractfile()
#     .extractall()
#
# To extract a single file from a TAR archive, use extract(), passing in the filename:
#
# >>> tar.extract('README.md')
# >>> os.listdir('.')
# ['README.md', 'example.tar']
#
# The README.md file is extracted from the archive to the file system. Calling os.listdir() confirms
# that README.md file was successfully extracted into the current directory. To unpack or extract everything
# from the archive, use .extractall():
#
# >>> tar.extractall(path="extracted/")
#
# .extractall() has an optional path argument to specify where extracted files should go. Here, the archive is unpacked
# into the extracted directory. The following commands show that the archive was successfully extracted:
#
# $ ls
# example.tar  extracted  README.md
#
# $ tree
# .
# ├── example.tar
# ├── extracted
# |   ├── app.py
# |   ├── CONTRIBUTING.rst
# |   └── README.md
# └── README.md
#
# 1 directory, 5 files
#
# $ ls extracted/
# app.py  CONTRIBUTING.rst  README.md
#
# To extract a file object for reading or writing, use .extractfile(), which takes a filename or TarInfo object
# to extract as an argument. .extractfile() returns a file-like object that can be read and used:
#
# >>> f = tar.extractfile('app.py')
# >>> f.read()
# >>> tar.close()
#
# Opened archives should always be closed after they have been read or written to. To close an archive, call .close()
# on the archive file handle or use the with statement when creating tarfile objects to automatically close
# the archive when you’re done. This frees up system resources and writes any changes you made to the archive
# to the filesystem.
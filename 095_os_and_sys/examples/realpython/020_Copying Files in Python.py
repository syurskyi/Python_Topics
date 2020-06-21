# shutil offers a couple of functions for copying files. The most commonly used functions are shutil.copy()
# and shutil.copy2(). To copy a file from one location to another using shutil.copy(), do the following:

import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy(src, dst)

# shutil.copy() is comparable to the cp command in UNIX based systems. shutil.copy(src, dst) will copy the file src
# to the location specified in dst. If dst is a file, the contents of that file are replaced with the contents of src.
# If dst is a directory, then src will be copied into that directory. shutil.copy() only copies the file’s contents
# and the file’s permissions. Other metadata like the file’s creation and modification times are not preserved.
#
# To preserve all file metadata when copying, use shutil.copy2():

import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy2(src, dst)

# Using .copy2() preserves details about the file such as last access time, permission bits, last modification time,
# and flags.


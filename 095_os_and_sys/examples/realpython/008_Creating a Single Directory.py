# To create a single directory, pass a path to the directory as a parameter to os.mkdir():
#
# import os
# os.mkdir('example_directory/')

# If a directory already exists, os.mkdir() raises FileExistsError. Alternatively, you can create a directory using
# pathlib:

from pathlib import Path

p = Path('example_directory/')
p.mkdir()

# If the path already exists, mkdir() raises a FileExistsError:
#
# >>> p.mkdir()
# Traceback (most recent call last):
#   File '<stdin>', line 1, in <module>
#   File '/usr/lib/python3.5/pathlib.py', line 1214, in mkdir
#     self._accessor.mkdir(self, mode)
#   File '/usr/lib/python3.5/pathlib.py', line 371, in wrapped
#     return strfunc(str(pathobj), *args)
# FileExistsError: [Errno 17] File exists: '.'
# [Errno 17] File exists: '.'
#
# To avoid errors like this, catch the error when it happens and let your user know:

from pathlib import Path

p = Path('example_directory')
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)

# Alternatively, you can ignore the FileExistsError by passing the exist_ok=True argument to .mkdir():

from pathlib import Path

p = Path('example_directory')
p.mkdir(exist_ok=True)

# This will not raise an error if the directory already exists.
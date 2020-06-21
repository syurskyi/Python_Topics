# Paths representing directories or symbolic links that do not exist can be used to create the associated file system entries.
# pathlib_mkdir.py
#
# import pathlib
#
# p = pathlib.Path('example_dir')
#
# print('Creating {}'.format(p))
# p.mkdir()
#
# If the path already exists, mkdir() raises a FileExistsError.
#
# $ python3 pathlib_mkdir.py
#
# Creating example_dir
#
# $ python3 pathlib_mkdir.py
#
# Creating example_dir
# Traceback (most recent call last):
#   File "pathlib_mkdir.py", line 16, in <module>
#     p.mkdir()
#   File ".../lib/python3.6/pathlib.py", line 1226, in mkdir
#     self._accessor.mkdir(self, mode)
#   File ".../lib/python3.6/pathlib.py", line 387, in wrapped
#     return strfunc(str(pathobj), *args)
# FileExistsError: [Errno 17] File exists: 'example_dir'


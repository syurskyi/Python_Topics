# There are two methods for removing things from the file system, depending on the type. To remove an empty directory, use rmdir().
# pathlib_rmdir.py
#
# import pathlib
#
# p = pathlib.Path('example_dir')
#
# print('Removing {}'.format(p))
# p.rmdir()
#
# A FileNotFoundError exception is raised if the post-conditions are already met and the directory does not exist. It is also an error to try to remove a directory that is not empty.
#
# $ python3 pathlib_rmdir.py
#
# Removing example_dir
#
# $ python3 pathlib_rmdir.py
#
# Removing example_dir
# Traceback (most recent call last):
#   File "pathlib_rmdir.py", line 16, in <module>
#     p.rmdir()
#   File ".../lib/python3.6/pathlib.py", line 1270, in rmdir
#     self._accessor.rmdir(self)
#   File ".../lib/python3.6/pathlib.py", line 387, in wrapped
#     return strfunc(str(pathobj), *args)
# FileNotFoundError: [Errno 2] No such file or directory:
# 'example_dir'


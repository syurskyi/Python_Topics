# Detailed information about a file can be accessed using the methods stat() or lstat() (for checking the status of something that might be a symbolic link). These methods produce the same results as os.stat() and os.lstat().
# pathlib_stat.py
#
# import pathlib
# import sys
# import time
#
# if len(sys.argv) == 1:
#     filename = __file__
# else:
#     filename = sys.argv[1]
#
# p = pathlib.Path(filename)
# stat_info = p.stat()
#
# print('{}:'.format(filename))
# print('  Size:', stat_info.st_size)
# print('  Permissions:', oct(stat_info.st_mode))
# print('  Owner:', stat_info.st_uid)
# print('  Device:', stat_info.st_dev)
# print('  Created      :', time.ctime(stat_info.st_ctime))
# print('  Last modified:', time.ctime(stat_info.st_mtime))
# print('  Last accessed:', time.ctime(stat_info.st_atime))
#
# The output will vary depending on how the example code was installed. Try passing different filenames on the command line to pathlib_stat.py.
#
# $ python3 pathlib_stat.py
#
# pathlib_stat.py:
#   Size: 607
#   Permissions: 0o100644
#   Owner: 527
#   Device: 16777220
#   Created      : Thu Dec 29 12:38:23 2016
#   Last modified: Thu Dec 29 12:38:23 2016
#   Last accessed: Sun Mar 18 16:21:41 2018
#
# $ python3 pathlib_stat.py index.rst
#
# index.rst:
#   Size: 19569
#   Permissions: 0o100644
#   Owner: 527
#   Device: 16777220
#   Created      : Sun Mar 18 16:11:31 2018
#   Last modified: Sun Mar 18 16:11:31 2018
#   Last accessed: Sun Mar 18 16:21:40 2018


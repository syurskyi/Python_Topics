# The touch() method works like the Unix command touch to create a file or update an existing file’s modification time and permissions.
# pathlib_touch.py
#
# import pathlib
# import time
#
# p = pathlib.Path('touched')
# if p.exists():
#     print('already exists')
# else:
#     print('creating new')
#
# p.touch()
# start = p.stat()
#
# time.sleep(1)
#
# p.touch()
# end = p.stat()
#
# print('Start:', time.ctime(start.st_mtime))
# print('End  :', time.ctime(end.st_mtime))
#
# Running this example more than once updates the existing file on subsequent runs.
#
# $ python3 pathlib_touch.py
#
# creating new
# Start: Sun Mar 18 16:21:41 2018
# End  : Sun Mar 18 16:21:42 2018
#
# $ python3 pathlib_touch.py
#
# already exists
# Start: Sun Mar 18 16:21:42 2018
# End  : Sun Mar 18 16:21:43 2018


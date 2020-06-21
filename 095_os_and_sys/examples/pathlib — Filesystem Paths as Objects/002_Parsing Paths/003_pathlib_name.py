# Other parts of the path can be accessed through properties of the path object. The name property holds the last part of the path, after the final path separator (the same value that os.path.basename() produces). The suffix property holds the value after the extension separator and the stem property holds the portion of the name before the suffix.
# pathlib_name.py
#
# import pathlib
#
# p = pathlib.PurePosixPath('./source/pathlib/pathlib_name.py')
# print('path  : {}'.format(p))
# print('name  : {}'.format(p.name))
# print('suffix: {}'.format(p.suffix))
# print('stem  : {}'.format(p.stem))
#
# Although the suffix and stem values are similar to the values produced by os.path.splitext(), the values are based only on the value of name and not the full path.
#
# $ python3 pathlib_name.py
#
# path  : source/pathlib/pathlib_name.py
# name  : pathlib_name.py
# suffix: .py
# stem  : pathlib_name
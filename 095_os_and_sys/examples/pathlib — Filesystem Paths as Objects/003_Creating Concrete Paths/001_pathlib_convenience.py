# Instances of the concrete Path class can be created from string arguments referring to the name (or potential name) of a file, directory, or symbolic link on the file system. The class also provides several convenience methods for building instances using commonly used locations that change, such as the current working directory and the user’s home directory.
# pathlib_convenience.py
#
# import pathlib
#
# home = pathlib.Path.home()
# print('home: ', home)
#
# cwd = pathlib.Path.cwd()
# print('cwd : ', cwd)
#
# Both methods create Path instances pre-populated with an absolute file system reference.
#
# $ python3 pathlib_convenience.py
#
# home:  /Users/dhellmann
# cwd :  /Users/dhellmann/PyMOTW
#

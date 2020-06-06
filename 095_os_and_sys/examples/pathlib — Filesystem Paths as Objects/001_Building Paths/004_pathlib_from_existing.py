# Given an existing path object, it is easy to build a new one with minor differences such as referring to a different file in the same directory. Use with_name() to create a new path that replaces the name portion of a path with a different file name. Use with_suffix() to create a new path that replaces the file name’s extension with a different value.


# pathlib_from_existing.py

import pathlib

ind = pathlib.PurePosixPath('source/pathlib/index.rst')
print(ind)

py = ind.with_name('pathlib_from_existing.py')
print(py)

pyc = py.with_suffix('.pyc')
print(pyc)

# Both methods return new objects, and the original is left unchanged.
#
# $ python3 pathlib_from_existing.py
#
# source/pathlib/index.rst
# source/pathlib/pathlib_from_existing.py
# source/pathlib/pathlib_from_existing.pyc

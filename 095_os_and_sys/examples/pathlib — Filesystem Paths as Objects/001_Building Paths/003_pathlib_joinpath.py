# To build paths when the segments are not known in advance, use joinpath(), passing each path segment as a separate argument.


# pathlib_joinpath.py

import pathlib

root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_local = root.joinpath(*subdirs)
print(usr_local)


# As with the / operator, calling joinpath() creates a new instance.
#
# $ python3 pathlib_joinpath.py
#
# /usr/local
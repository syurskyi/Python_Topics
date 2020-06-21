# There are two ways to navigate “up” the filesystem hierarchy from a given path object. The parent property refers to a new path instance for the directory containing the path, the value returned by os.path.dirname(). The parents property is an iterable that produces parent directory references, continually going “up” the path hierarchy until reaching the root.
# pathlib_parents.py
#
# import pathlib
#
# p = pathlib.PurePosixPath('/usr/local/lib')
#
# print('parent: {}'.format(p.parent))
#
# print('\nhierarchy:')
# for up in p.parents:
#     print(up)
#
# The example iterates over the parents property and prints the member values.
#
# $ python3 pathlib_parents.py
#
# parent: /usr/local
#
# hierarchy:
# /usr/local
# /usr
# /
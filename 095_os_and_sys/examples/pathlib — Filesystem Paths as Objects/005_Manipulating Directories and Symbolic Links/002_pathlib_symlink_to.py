# Use symlink_to() to create a symbolic link. The link will be named based on the path’s value and will refer to the name given as argument to symlink_to().
# pathlib_symlink_to.py
#
# import pathlib
#
# p = pathlib.Path('example_link')
#
# p.symlink_to('index.rst')
#
# print(p)
# print(p.resolve().name)
#
# This example creates a symbolic link, then uses resolve() to read the link to find what it points to and print the name.
#
# $ python3 pathlib_symlink_to.py
#
# example_link
# index.rst
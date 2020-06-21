# For simpler access to information about the owner of a file, use owner() and group().
# pathlib_ownership.py
#
# import pathlib
#
# p = pathlib.Path(__file__)
#
# print('{} is owned by {}/{}'.format(p, p.owner(), p.group()))
#
# While stat() returns numerical system ID values, these methods look up the name associated with the IDs.
#
# $ python3 pathlib_ownership.py
#
# pathlib_ownership.py is owned by dhellmann/dhellmann


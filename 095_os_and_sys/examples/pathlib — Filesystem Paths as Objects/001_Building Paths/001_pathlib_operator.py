# To instantiate a new path, give a string as the first argument. The string representation of the path object is this name value. To create a new path referring to a value relative to an existing path, use the / operator to extend the path. The argument to the operator can either be a string or another path object.

# pathlib_operator.py

import pathlib

usr = pathlib.PurePosixPath('/usr')
print(usr)

usr_local = usr / 'local'
print(usr_local)

usr_share = usr / pathlib.PurePosixPath('share')
print(usr_share)

root = usr / '..'
print(root)

etc = root / '/etc/'
print(etc)


# As the value for root in the example output shows, the operator combines the path values as they are given, and does not normalize the result when it contains the parent directory reference "..". However, if a segment begins with the path separator it is interpreted as a new “root” reference in the same way as os.path.join(). Extra path separators are removed from the middle of the path value, as in the etc example here.
#
# $ python3 pathlib_operator.py
#
# /usr
# /usr/local
# /usr/share
# /usr/..
# /etc
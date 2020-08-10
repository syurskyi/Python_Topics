#!/usr/bin/env python3
"""Change permissions on a file
"""

#end_pymotw_header
______ __
______ stat

filename = 'os_stat_chmod_example.txt'
if __.path.exists(filename):
    __.unlink(filename)
w__ o..(filename, 'wt') __ f:
    f.write('contents')

# Determine what permissions are already set using stat
existing_permissions = stat.S_IMODE(__.stat(filename).st_mode)

if not __.access(filename, __.X_OK):
    print('Adding execute permission')
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Removing execute permission')
    # use xor to remove the user execute permission
    new_permissions = existing_permissions ^ stat.S_IXUSR

__.chmod(filename, new_permissions)

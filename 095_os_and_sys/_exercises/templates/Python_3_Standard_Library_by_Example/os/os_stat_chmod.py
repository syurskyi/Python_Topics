#!/usr/bin/env python3
"""Change permissions on a file
"""

#end_pymotw_header
______ __
______ s..

filename _ 'os_stat_chmod_example.txt'
__ __.p...exists(filename):
    __.unlink(filename)
w__ o..(filename, 'wt') __ f:
    f.w..('contents')

# Determine what permissions are already set using stat
existing_permissions _ s...S_IMODE(__.s..(filename).st_mode)

__ not __.a..(filename, __.X_OK):
    print('Adding execute permission')
    new_permissions _ existing_permissions | s...S_IXUSR
____
    print('Removing execute permission')
    # use xor to remove the user execute permission
    new_permissions _ existing_permissions ^ s...S_IXUSR

__.chmod(filename, new_permissions)

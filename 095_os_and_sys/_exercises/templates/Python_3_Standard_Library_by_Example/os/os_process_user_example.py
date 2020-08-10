#!/usr/bin/env python3
"""Find information about the user running the current process.
"""

#end_pymotw_header
______ __

TEST_GID = 502
TEST_UID = 502


___ show_user_info():
    print('User (actual/effective)  : {} / {}'.f..(
        __.getuid(), __.geteuid()))
    print('Group (actual/effective) : {} / {}'.f..(
        __.getgid(), __.getegid()))
    print('Actual Groups   :', __.getgroups())


print('BEFORE CHANGE:')
show_user_info()
print()

try:
    __.setegid(TEST_GID)
except OSError:
    print('ERROR: Could not change effective group. '
          'Rerun as root.')
else:
    print('CHANGE GROUP:')
    show_user_info()
    print()

try:
    __.seteuid(TEST_UID)
except OSError:
    print('ERROR: Could not change effective user. '
          'Rerun as root.')
else:
    print('CHANGE USER:')
    show_user_info()
    print()

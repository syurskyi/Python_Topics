#!/usr/bin/env python3
"""Change permissions on a file
"""

#end_pymotw_header
______ __
______ p_l_
______ s..

# Create a fresh test file.
f _ p_l_.P..('pathlib_chmod_example.txt')
__ f.e..():
    f.u..()
f.write_text('contents')

# Determine what permissions are already set using stat.
existing_permissions _ s...S_IMODE(f.s..().st_mode)
print('Before: {:o}'.f..(existing_permissions))

# Decide which way to toggle them.
__ no. (existing_permissions & __.X_OK):
    print('Adding execute permission')
    new_permissions _ existing_permissions | s...S_IXUSR
____
    print('Removing execute permission')
    # use xor to remove the user execute permission
    new_permissions _ existing_permissions ^ s...S_IXUSR

# Make the change and show the new value.
f.chmod(new_permissions)
after_permissions _ s...S_IMODE(f.s..().st_mode)
print('After: {:o}'.f..(after_permissions))

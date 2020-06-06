# On Unix-like systems, file permissions can be changed using chmod(), passing the mode as an integer. Mode values can be constructed using constants defined in the stat module. This example toggles the user’s execute permission bit.
# pathlib_chmod.py
#
# import os
# import pathlib
# import stat
#
# # Create a fresh test file.
# f = pathlib.Path('pathlib_chmod_example.txt')
# if f.exists():
#     f.unlink()
# f.write_text('contents')
#
# # Determine what permissions are already set using stat.
# existing_permissions = stat.S_IMODE(f.stat().st_mode)
# print('Before: {:o}'.format(existing_permissions))
#
# # Decide which way to toggle them.
# if not (existing_permissions & os.X_OK):
#     print('Adding execute permission')
#     new_permissions = existing_permissions | stat.S_IXUSR
# else:
#     print('Removing execute permission')
#     # use xor to remove the user execute permission
#     new_permissions = existing_permissions ^ stat.S_IXUSR
#
# # Make the change and show the new value.
# f.chmod(new_permissions)
# after_permissions = stat.S_IMODE(f.stat().st_mode)
# print('After: {:o}'.format(after_permissions))
#
# The script assumes it has the permissions necessary to modify the mode of the file when run.
#
# $ python3 pathlib_chmod.py
#
# Before: 644
# Adding execute permission
# After: 744


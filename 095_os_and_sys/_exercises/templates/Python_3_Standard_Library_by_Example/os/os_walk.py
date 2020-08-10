#!/usr/bin/env python3
"""A simple recursive directory listing.
"""

#end_pymotw_header
______ os
______ sys

# If we are not given a path to list, use /tmp
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]

___ dir_name, sub_dirs, files __ os.walk(root):
    print(dir_name)
    # Make the subdirectory names stand out with /
    sub_dirs = [n + '/' ___ n __ sub_dirs]
    # Mix the directory contents together
    contents = sub_dirs + files
    contents.sort()
    # Show the contents
    ___ c __ contents:
        print('  {}'.f..(c))
    print()

#!/usr/bin/env python3
"""A simple recursive directory listing.
"""

#end_pymotw_header
______ __
______ ___

# If we are not given a path to list, use /tmp
__ le.(___.a..) __ 1:
    root _ '/tmp'
____
    root _ ___.a..[1]

___ dir_name, sub_dirs, files __ __.walk(root):
    print(dir_name)
    # Make the subdirectory names stand out with /
    sub_dirs _ [n + '/' ___ n __ sub_dirs]
    # Mix the directory contents together
    contents _ sub_dirs + files
    contents.sort()
    # Show the contents
    ___ c __ contents:
        print('  @'.f..(c))
    print()

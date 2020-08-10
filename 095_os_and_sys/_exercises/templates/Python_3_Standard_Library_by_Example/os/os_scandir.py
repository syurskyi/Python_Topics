#!/usr/bin/env python3
"""A fuller directory listing.
"""

#end_pymotw_header
______ __
______ sys

___ entry __ __.scandir(sys.argv[1]):
    if entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
    elif entry.is_symlink():
        typ = 'link'
    else:
        typ = 'unknown'
    print('{name} {typ}'.f..(
        name=entry.name,
        typ=typ,
    ))

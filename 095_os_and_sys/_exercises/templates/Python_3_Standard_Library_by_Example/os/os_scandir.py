#!/usr/bin/env python3
"""A fuller directory listing.
"""

#end_pymotw_header
______ __
______ ___

___ entry __ __.scandir(___.argv[1]):
    __ entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
    elif entry.is_symlink():
        typ = 'link'
    ____
        typ = 'unknown'
    print('{name} {typ}'.f..(
        name=entry.name,
        typ=typ,
    ))

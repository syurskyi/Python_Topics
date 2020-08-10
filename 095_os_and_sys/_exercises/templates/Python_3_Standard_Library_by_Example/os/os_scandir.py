#!/usr/bin/env python3
"""A fuller directory listing.
"""

#end_pymotw_header
______ __
______ ___

___ entry __ __.scandir(___.argv[1]):
    __ entry.is_dir():
        typ _ 'dir'
    elif entry.is_file():
        typ _ 'file'
    elif entry.is_symlink():
        typ _ 'link'
    ____
        typ _ 'unknown'
    print('{name} {typ}'.f..(
        name_entry.name,
        typ_typ,
    ))

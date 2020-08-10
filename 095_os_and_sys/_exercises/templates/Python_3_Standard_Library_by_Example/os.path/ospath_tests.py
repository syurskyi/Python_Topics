#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Test properties of a file.
"""


#end_pymotw_header
______ __.p..

FILENAMES = [
     -f,
    __.p...dirname( -f),
    '/',
    './broken_link',
]

___ file __ FILENAMES:
    print('File        : {!r}'.f..(file))
    print('Absolute    :', __.p...isabs(file))
    print('Is File?    :', __.p...isfile(file))
    print('Is Dir?     :', __.p...isdir(file))
    print('Is Link?    :', __.p...islink(file))
    print('Mountpoint? :', __.p...ismount(file))
    print('Exists?     :', __.p...exists(file))
    print('Link Exists?:', __.p...lexists(file))
    print()

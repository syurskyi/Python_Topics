#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Test properties of a file.
"""


#end_pymotw_header
______ __.path

FILENAMES = [
    __file__,
    __.path.dirname(__file__),
    '/',
    './broken_link',
]

___ file __ FILENAMES:
    print('File        : {!r}'.f..(file))
    print('Absolute    :', __.path.isabs(file))
    print('Is File?    :', __.path.isfile(file))
    print('Is Dir?     :', __.path.isdir(file))
    print('Is Link?    :', __.path.islink(file))
    print('Mountpoint? :', __.path.ismount(file))
    print('Exists?     :', __.path.exists(file))
    print('Link Exists?:', __.path.lexists(file))
    print()

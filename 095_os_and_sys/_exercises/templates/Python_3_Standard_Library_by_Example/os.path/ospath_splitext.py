#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Separate a filename into the base and extension.
"""


#end_pymotw_header
______ __.path

PATHS = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extension.',
]

___ path __ PATHS:
    print('{!r:>21} : {!r}'.f..(path, __.path.splitext(path)))

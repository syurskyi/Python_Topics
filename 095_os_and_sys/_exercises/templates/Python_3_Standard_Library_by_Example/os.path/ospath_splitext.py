#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Separate a filename into the base and extension.
"""


#end_pymotw_header
______ __.p..

PATHS = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extension.',
]

___ p.. __ PATHS:
    print('{!r:>21} : {!r}'.f..(p.., __.p...splitext(p..)))

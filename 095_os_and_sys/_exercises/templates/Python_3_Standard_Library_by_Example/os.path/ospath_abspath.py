#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Compute an absolute path from a relative path.
"""


#end_pymotw_header
______ __
______ __.path

__.chdir('/usr')

PATHS = [
    '.',
    '..',
    './one/two/three',
    '../one/two/three',
]

___ path __ PATHS:
    print('{!r:>21} : {!r}'.f..(path, __.path.abspath(path)))

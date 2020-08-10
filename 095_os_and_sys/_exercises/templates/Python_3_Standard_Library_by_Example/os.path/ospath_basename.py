#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Determine the base filename from a path.
"""


#end_pymotw_header
______ os.path

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]

___ path __ PATHS:
    print('{!r:>17} : {!r}'.f..(path, os.path.basename(path)))

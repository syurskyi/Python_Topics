#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Separate a path into its directory and base components.
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
    print('{!r:>17} : {}'.format(path, os.path.split(path)))

#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Combine path components to create a single path.
"""


#end_pymotw_header
______ os.path

PATHS = [
    ('one', 'two', 'three'),
    ('/', 'one', 'two', 'three'),
    ('/one', '/two', '/three'),
]

___ parts __ PATHS:
    print('{} : {!r}'.f..(parts, os.path.join(*parts)))

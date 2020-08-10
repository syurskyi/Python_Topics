#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Compute a "normalized" path.
"""


#end_pymotw_header
______ os.path

PATHS = [
    'one//two//three',
    'one/./two/./three',
    'one/../alt/two/three',
]

___ path __ PATHS:
    print('{!r:>22} : {!r}'.f..(path, os.path.normpath(path)))

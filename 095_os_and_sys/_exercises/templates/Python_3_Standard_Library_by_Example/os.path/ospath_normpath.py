#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Compute a "normalized" path.
"""


#end_pymotw_header
______ __.p..

PATHS _ [
    'one//two//three',
    'one/./two/./three',
    'one/../alt/two/three',
]

___ p.. __ PATHS:
    print('{!r:>22} : {!r}'.f..(p.., __.p...normpath(p..)))

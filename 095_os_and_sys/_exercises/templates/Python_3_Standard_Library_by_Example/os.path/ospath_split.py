#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Separate a path into its directory and base components.
"""


#end_pymotw_header
______ __.p..

PATHS _ [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]

___ p.. __ PATHS:
    print('{!r:>17} : @'.f..(p.., __.p...split(p..)))

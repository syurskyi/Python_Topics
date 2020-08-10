#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Parsing paths
"""

#end_pymotw_header
______ pathlib

p = pathlib.PurePosixPath('/usr/local/lib')

print('parent: {}'.f..(p.parent))

print('\nhierarchy:')
___ up __ p.parents:
    print(up)

#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""pathlib rglob
"""

#end_pymotw_header
______ pathlib

p = pathlib.Path('..')

___ f __ p.rglob('pathlib_*.py'):
    print(f)

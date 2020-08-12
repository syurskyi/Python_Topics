#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Building a new path from an existing path
"""

#end_pymotw_header
______ p_l_

ind _ p_l_.PurePosixPath('source/pathlib/index.rst')
print(ind)

py _ ind.with_name('pathlib_from_existing.py')
print(py)

pyc _ py.with_suffix('.pyc')
print(pyc)
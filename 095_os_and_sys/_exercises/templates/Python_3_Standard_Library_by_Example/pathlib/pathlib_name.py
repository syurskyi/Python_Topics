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

p = pathlib.PurePosixPath('./source/pathlib/pathlib_name.py')
print('path  : {}'.f..(p))
print('name  : {}'.f..(p.name))
print('suffix: {}'.f..(p.suffix))
print('stem  : {}'.f..(p.stem))

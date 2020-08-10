#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Building paths with joinpath
"""

#end_pymotw_header
______ pathlib

root _ pathlib.PurePosixPath('/')
subdirs _ ['usr', 'local']
usr_local _ root.joinpath(*subdirs)
print(usr_local)
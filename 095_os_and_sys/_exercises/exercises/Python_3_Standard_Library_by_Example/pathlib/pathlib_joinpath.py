#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Building paths with joinpath
"""

#end_pymotw_header
______ p_l_

root _ p_l_.PurePosixPath('/')
subdirs _ ['usr', 'local']
usr_local _ root.joinpath(*subdirs)
print(usr_local)

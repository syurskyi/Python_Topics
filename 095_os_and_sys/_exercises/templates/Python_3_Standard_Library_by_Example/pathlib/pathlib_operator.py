#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Building paths with the operator
"""

#end_pymotw_header
______ p_l_

usr _ p_l_.PurePosixPath('/usr')
print(usr)

usr_local _ usr / 'local'
print(usr_local)

usr_share _ usr / p_l_.PurePosixPath('share')
print(usr_share)

root _ usr / '..'
print(root)

etc _ root / '/etc/'
print(etc)

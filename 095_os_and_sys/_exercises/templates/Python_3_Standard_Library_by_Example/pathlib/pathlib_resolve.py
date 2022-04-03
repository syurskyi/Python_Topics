#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Resolving relative paths
"""

#end_pymotw_header
______ p_l_

usr_local _ p_l_.P..('/usr/local')
share _ usr_local / '..' / 'share'
print(share.r..())

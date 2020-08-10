#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Find attributes of a file other than its name.
"""


#end_pymotw_header
______ __.path
______ time

print('File         :',  -f)
print('Access time  :', time.ctime(__.path.getatime( -f)))
print('Modified time:', time.ctime(__.path.getmtime( -f)))
print('Change time  :', time.ctime(__.path.getctime( -f)))
print('Size         :', __.path.getsize( -f))

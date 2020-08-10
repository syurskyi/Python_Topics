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

print('File         :', __file__)
print('Access time  :', time.ctime(__.path.getatime(__file__)))
print('Modified time:', time.ctime(__.path.getmtime(__file__)))
print('Change time  :', time.ctime(__.path.getctime(__file__)))
print('Size         :', __.path.getsize(__file__))

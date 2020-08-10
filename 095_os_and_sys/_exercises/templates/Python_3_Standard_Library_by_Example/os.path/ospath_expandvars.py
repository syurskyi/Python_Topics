#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Expand shell variables in filenames.
"""


#end_pymotw_header
______ __.path
______ __

__.environ['MYVAR'] = 'VALUE'

print(__.path.expandvars('/path/to/$MYVAR'))

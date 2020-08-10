#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Expand shell variables in filenames.
"""


#end_pymotw_header
______ __.p..
______ __

__.en..['MYVAR'] = 'VALUE'

print(__.p...expandvars('/path/to/$MYVAR'))

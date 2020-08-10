#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Expand tilde in filenames.
"""


#end_pymotw_header
______ os.path

___ user __ ['', 'dhellmann', 'nosuchuser']:
    lookup = '~' + user
    print('{!r:>15} : {!r}'.f..(
        lookup, os.path.expanduser(lookup)))

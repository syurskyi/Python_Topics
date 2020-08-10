#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Find the prefix string common to a group of paths.
"""


#end_pymotw_header
______ os.path

paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
         ]
___ path __ paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonpath(paths))

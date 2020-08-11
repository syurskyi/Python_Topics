#!/usr/bin/env python3
# encoding: utf-8
#
#
"""Compute an absolute path from a relative path.
"""


#end_pymotw_header
import os
import os.path

os.chdir('C:/Users')

PATHS = [
    '.',
    '..',
    './one/two/three',
    '../one/two/three']


for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.abspath(path)))
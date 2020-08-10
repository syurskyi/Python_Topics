#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Read and writing files
"""

#end_pymotw_header
______ pathlib

f _ pathlib.P..('example.txt')

f.write_bytes('This is the content'.encode('utf-8'))

w__ f.o..('r', encoding_'utf-8') __ handle:
    print('read from open(): {!r}'.f..(handle.read()))

print('read_text(): {!r}'.f..(f.read_text('utf-8')))

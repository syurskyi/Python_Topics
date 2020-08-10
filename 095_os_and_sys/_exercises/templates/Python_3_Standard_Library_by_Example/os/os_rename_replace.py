#!/usr/bin/env python3
"""Renaming and replacing files
"""

#end_pymotw_header
______ g__
______ __


w__ o..('rename_start.txt', 'w') __ f:
    f.write('starting as rename_start.txt')

print('Starting:', g__.g__('rename*.txt'))

__.rename('rename_start.txt', 'rename_finish.txt')

print('After rename:', g__.g__('rename*.txt'))

w__ o..('rename_finish.txt', 'r') __ f:
    print('Contents:', repr(f.read()))

w__ o..('rename_new_contents.txt', 'w') __ f:
    f.write('ending with contents of rename_new_contents.txt')

__.replace('rename_new_contents.txt', 'rename_finish.txt')

w__ o..('rename_finish.txt', 'r') __ f:
    print('After replace:', repr(f.read()))

___ name __ g__.g__('rename*.txt'):
    __.unlink(name)

#!/usr/bin/env python3
"""Check access rights on a file
"""

#end_pymotw_header
______ __

print('Testing:', __file__)
print('Exists:', __.access(__file__, __.F_OK))
print('Readable:', __.access(__file__, __.R_OK))
print('Writable:', __.access(__file__, __.W_OK))
print('Executable:', __.access(__file__, __.X_OK))

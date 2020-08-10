#!/usr/bin/env python3
"""Using the os module to read and write environment variables.
"""

#end_pymotw_header
______ __

print('Initial value:', __.environ.get('TESTVAR', None))
print('Child process:')
__.system('echo $TESTVAR')

__.environ['TESTVAR'] = 'THIS VALUE WAS CHANGED'

print()
print('Changed value:', __.environ['TESTVAR'])
print('Child process:')
__.system('echo $TESTVAR')

del __.environ['TESTVAR']

print()
print('Removed value:', __.environ.get('TESTVAR', None))
print('Child process:')
__.system('echo $TESTVAR')

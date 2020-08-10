#!/usr/bin/env python3
"""Working with directories.
"""

#end_pymotw_header
______ __

dir_name = 'os_directories_example'

print('Creating', dir_name)
__.makedirs(dir_name)

file_name = __.path.join(dir_name, 'example.txt')
print('Creating', file_name)
w__ o..(file_name, 'wt') __ f:
    f.write('example file')

print('Cleaning up')
__.unlink(file_name)
__.rmdir(dir_name)

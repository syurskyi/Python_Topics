#!/usr/bin/env python3
"""Working with symbolic links
"""

#end_pymotw_header
______ __

link_name _ '/tmp/' + __.p...basename( -f)

print('Creating link @ -> @'.f..(link_name,  -f))
__.symlink( -f, link_name)

stat_info _ __.lstat(link_name)
print('Permissions:', oct(stat_info.st_mode))

print('Points to:', __.readlink(link_name))

# Cleanup
__.u..(link_name)

#!/usr/bin/env python3
"""Working with symbolic links
"""

#end_pymotw_header
______ __

link_name = '/tmp/' + __.path.basename(__file__)

print('Creating link {} -> {}'.f..(link_name, __file__))
__.symlink(__file__, link_name)

stat_info = __.lstat(link_name)
print('Permissions:', oct(stat_info.st_mode))

print('Points to:', __.readlink(link_name))

# Cleanup
__.unlink(link_name)

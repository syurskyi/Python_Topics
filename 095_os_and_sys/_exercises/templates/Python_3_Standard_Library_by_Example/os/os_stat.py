#!/usr/bin/env python3
"""Show stat info for a file.
"""

#end_pymotw_header
______ __
______ ___
______ ti__

__ len(___.argv) == 1:
    filename _  -f
____
    filename _ ___.argv[1]

stat_info _ __.stat(filename)

print('os.stat(@):'.f..(filename))
print('  Size:', stat_info.st_size)
print('  Permissions:', oct(stat_info.st_mode))
print('  Owner:', stat_info.st_uid)
print('  Device:', stat_info.st_dev)
print('  Created      :', ti__.ctime(stat_info.st_ctime))
print('  Last modified:', ti__.ctime(stat_info.st_mtime))
print('  Last accessed:', ti__.ctime(stat_info.st_atime))

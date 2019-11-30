import os
os.chmod('spam.txt', 0o777) # enable all accesses

os.rename(r'C:\temp\spam.txt', r'C:\temp\eggs.txt') # from, to
os.remove(r'C:\temp\spam.txt') # delete file?
# WindowsError: [Error 2] The system cannot find the file specified: 'C:\\temp\\...'
# ######################################################################################################################

os.remove(r'C:\temp\eggs.txt')

open('spam.txt', 'w').write('Hello stat world\n') # +1 for \r added
# 17
# ######################################################################################################################

import os
info = os.stat(r'C:\temp\spam.txt')
info
# nt.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0,
# st_size=18, st_atime=1267645806, st_mtime=1267646072, st_ctime=1267645806)
# ######################################################################################################################

info.st_mode, info.st_size # via named-tuple item attr names
# (33206, 18)
# ######################################################################################################################

import stat
info[stat.ST_MODE], info[stat.ST_SIZE] # via stat module presets
# (33206, 18)
# ######################################################################################################################

stat.S_ISDIR(info.st_mode), stat.S_ISREG(info.st_mode)
# (False, True)
# ######################################################################################################################

path = r'C:\temp\spam.txt'
os.path.isdir(path), os.path.isfile(path), os.path.getsize(path)
# (False, True, 18)
# ######################################################################################################################
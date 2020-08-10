#!/usr/bin/env python3
"""Change modification time of a file
"""

#end_pymotw_header
______ pathlib
______ ti__

p _ pathlib.P..('touched')
__ p.e..():
    print('already exists')
____
    print('creating new')

p.touch()
start _ p.s..()

ti__.sleep(1)

p.touch()
end _ p.s..()

print('Start:', ti__.ctime(start.st_mtime))
print('End  :', ti__.ctime(end.st_mtime))

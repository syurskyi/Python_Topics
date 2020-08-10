#!/usr/bin/env python3
"""Change modification time of a file
"""

#end_pymotw_header
______ pathlib
______ ti__

p = pathlib.Path('touched')
__ p.exists():
    print('already exists')
____
    print('creating new')

p.touch()
start = p.stat()

ti__.sleep(1)

p.touch()
end = p.stat()

print('Start:', ti__.ctime(start.st_mtime))
print('End  :', ti__.ctime(end.st_mtime))

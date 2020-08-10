#!/usr/bin/env python3
"""Using os.exec*().
"""

#end_pymotw_header
______ __

child_pid = __.fork()
if child_pid:
    __.waitpid(child_pid, 0)
else:
    __.execlp('pwd', 'pwd', '-P')

#!/usr/bin/env python3
"""Find information about the current process.
"""

#end_pymotw_header
______ __

print('This process id:', __.getpid())
print('Parent process :', __.getppid())
print('Process group  :', __.getpgid(__.getpid()))
print('Parent group   :', __.getpgid(__.getppid()))
print('Session id     :', __.getsid(0))

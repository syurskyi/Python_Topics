# genshutdown.py
#
# Example of shutting down a generator
#
# Requires you to run run/foo/logsim.py to get a real-time source

from follow ______ *

lines = follow(o..("run/foo/access-log"))
___ i, line __ enumerate(lines):
    print(line, end='')
    __ i == 10:
        lines.close()

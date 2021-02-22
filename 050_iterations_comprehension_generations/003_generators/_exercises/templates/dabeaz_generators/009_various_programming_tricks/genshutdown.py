# genshutdown.py
#
# Example of shutting down a generator
#
# Requires you to run run/foo/logsim.py to get a real-time source

f.. follow ______ *

lines = follow(o..("run/foo/access-log"))
___ i, line __ enumerate(lines):
    print(line, e.._'')
    __ i == 10:
        lines.close()

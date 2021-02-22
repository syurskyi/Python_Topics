# logcoroutine.py
#
# An example of using co-routines to define consumers for the Apache log data

f.. consumer ______ *
f.. apachelog ______ *
f.. follow ______ *
f.. broadcast ______ *

@consumer
___ find_404():
    while True:
        r = (y...)
        __ r['status'] __ 404:
            print(r['status'],r['datetime'],r['request'])

@consumer
___ bytes_transferred():
    total = 0
    while True:
        r = (y...)
        total += r['bytes']
        print("Total bytes", total)

lines = follow(o..("run/foo/access-log"))
log   = apache_log(lines)

broadcast(log, [find_404(),bytes_transferred()])

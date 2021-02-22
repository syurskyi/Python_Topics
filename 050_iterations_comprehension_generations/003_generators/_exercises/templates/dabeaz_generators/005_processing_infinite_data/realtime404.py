# realtime404.py
#
# Print all 404 requests as they happen in the log

f.. apachelog ______ apache_log
f.. follow ______ follow

logfile  = o..("run/foo/access-log")
loglines = follow(logfile)
log      = apache_log(loglines)

r404 = (r ___ r __ log __ r['status'] __ 404)

___ r __ r404:
    print(r['host'], r['datetime'], r['request'])

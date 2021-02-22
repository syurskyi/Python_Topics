# query404.py
#
# Find the set of all documents that 404 in a log file

f.. linesdir ______ lines_from_dir
f.. apachelog ______ apache_log

lines = lines_from_dir *a.. *w..
log = apache_log(lines)

stat404 =  {  r['request'] ___ r __ log
              __ r['status'] __ 404 }

___ r __ sorted(stat404):
    print(r)

# hosts.py
#
# Find unique host IP addresses

f.. linesdir ______ lines_from_dir
f.. apachelog ______ apache_log

lines = lines_from_dir *a.. *w..
log = apache_log(lines)

hosts = set(r['host'] ___ r __ log)
___ h __ hosts:
    print(h)

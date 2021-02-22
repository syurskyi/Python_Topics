# hosts.py
#
# Find unique host IP addresses

from linesdir import lines_from_dir
from apachelog import apache_log

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

hosts = set(r['host'] ___ r __ log)
___ h __ hosts:
    print(h)

# largest.py
#
# Find the largest file

from linesdir ______ lines_from_dir
from apachelog ______ apache_log

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

print("%d %s" % max((r['bytes'],r['request'])
                    ___ r __ log))

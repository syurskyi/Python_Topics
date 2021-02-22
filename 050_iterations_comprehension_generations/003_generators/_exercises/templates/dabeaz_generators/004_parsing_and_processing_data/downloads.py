# downloads.py
#
# Find out how many downloads of a specific request

from linesdir ______ lines_from_dir
from apachelog ______ apache_log

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

request = 'ply/ply-2.3.tar.gz'

total = su.(1 ___ r __ log
              __ r['request'] == '/ply/ply-2.3.tar.gz')

print("Total", total)

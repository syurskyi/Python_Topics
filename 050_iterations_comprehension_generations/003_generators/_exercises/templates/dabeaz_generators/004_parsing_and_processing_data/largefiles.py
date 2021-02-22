# largefiles.py
#
# Find all transfers over a megabyte

f.. linesdir ______ *
f.. apachelog ______ *

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

large = (r ___ r __ log
         __ r['bytes'] > 1000000)

___ r __ large:
    print(r['request'],r['bytes'])



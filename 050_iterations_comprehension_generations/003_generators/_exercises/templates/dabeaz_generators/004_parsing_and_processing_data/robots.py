# robots.py
#
# Find out who has been hitting robots.txt

f.. linesdir ______ lines_from_dir
f.. apachelog ______ apache_log

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

addrs = { r['host'] ___ r __ log
            __ 'robots.txt' __ r['request'] }

______ socket
___ addr __ addrs:
    try:
        print(socket.gethostbyaddr(addr)[0])
    except socket.herror:
        print(addr)


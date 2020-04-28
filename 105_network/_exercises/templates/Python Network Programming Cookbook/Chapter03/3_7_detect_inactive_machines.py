#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
# Requires scapy-2.2.0 or higher for Python 2.7.
# Visit: http://www.secdev.org/projects/scapy/files/scapy-latest.zip
# As of now, requires a separate bundle for Python 3.x.
# Download it from: https://pypi.python.org/pypi/scapy-python3/0.20


______ a_p..
______ t__
______ sched
____ scapy.all ______ sr, srp, IP, UDP, ICMP, TCP, ARP, Ether

RUN_FREQUENCY _ 10

scheduler _ sched.scheduler(t__.t__, t__.sleep)


___ detect_inactive_hosts(scan_hosts):
    """ 
    Scans the network to find scan_hosts are live or dead
    scan_hosts can be like 10.0.2.2-4 to cover range. 
    See Scapy docs for specifying targets.   
    """
    global scheduler
    scheduler.enter(RUN_FREQUENCY, 1, detect_inactive_hosts, (scan_hosts, ))
    inactive_hosts _ []
    ___
        ans, unans _ sr(IP(dst_scan_hosts)/ICMP(), retry_0, timeout_1)
        ans.summary(lambda r : r.sprintf("IP.src is alive"))
        ___ inactive __ unans:
            print ("@ is inactive" inactive.dst)
            inactive_hosts.ap..(inactive.dst)
        
        print ("Total d hosts are inactive" (le.(inactive_hosts)))
             
        
    ______ K..:
        e..(0)


__ _____ __ ______
    parser _ ?.AP..(d.._'Python networking utils')
    ?.a_a..('--scan-hosts', a.._"store", d.._"scan_hosts", r.._T..)
    given_args _ parser.p_a..
    scan_hosts _ ?.scan_hosts
    scheduler.enter(1, 1, detect_inactive_hosts, (scan_hosts, ))
    scheduler.r..





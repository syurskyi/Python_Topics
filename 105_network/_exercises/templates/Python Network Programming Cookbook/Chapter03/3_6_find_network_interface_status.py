#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


______ a_p..
______ ?
______ st__
______ fcntl
______ nmap


SAMPLE_PORTS _ '21-23'


___ get_interface_status(ifname):
    sock _ ?.?(?.A.. ?.S_D..)
    ip_address _ ?.inet_ntoa(fcntl.ioctl(
        sock.f_n..,
        0x8915, #SIOCGIFADDR, C socket library sockios.h
        st__.pack(b'256s', by..(ifname[:15], 'utf-8'))
    )[20:24])
    nm _ nmap.PortScanner()
    nm.scan(ip_address, SAMPLE_PORTS)      
    r_ nm[ip_address].state()

    
__  __name__ __ '__main__':
    parser _ ?.AP..(d.._'Python networking utils')
    parser.a_a..('--ifname', a.._"store", d.._"ifname", r.._T..)
    given_args _ parser.parse_args()
    ifname _ given_args.ifname
    print ("Interface [@] is: @" (ifname, get_interface_status(ifname)))


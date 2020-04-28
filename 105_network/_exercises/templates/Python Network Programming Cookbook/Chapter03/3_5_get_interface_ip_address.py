#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
______ ___
______ ?
______ fcntl
______ st__
______ array


___ get_ip_address(ifname):
    s _ ?.?(?.A.. ?.S_D..)
    r_ ?.inet_ntoa(fcntl.ioctl(
        s.f_n..,
        0x8915,  # SIOCGIFADDR
        st__.pack(b'256s', by..(ifname[:15], 'utf-8'))
    )[20:24])

__ _______ __ ______
    parser _ ?.AP..(d.._'Python networking utils')
    parser.a_a..('--ifname', a.._"store", d.._"ifname", r.._T..)
    given_args _ parser.p_a..
    ifname _ given_args.ifname    
    print ("Interface [@] --> IP: @" (ifname, get_ip_address(ifname)))

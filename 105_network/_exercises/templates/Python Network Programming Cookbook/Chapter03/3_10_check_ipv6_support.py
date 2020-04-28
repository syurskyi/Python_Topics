#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
# This program depends on Python module netifaces => 0.8

______ ?
______ a_p..
______ netifaces __ ni


___ inspect_ipv6_support
    """ Find the ipv6 address"""
    print ("IPV6 support built into Python: @" ?.has_ipv6)
    ipv6_addr _ {}
    ___ interface __ ni.interfaces
        all_addresses _ ni.ifaddresses(interface)
        print ("Interface @:" interface)

        ___ family,addrs __ all_addresses.items
            fam_name _ ni.address_families[family]
            print ('  Address family: @'  fam_name)
            ___ addr __ addrs:
                __ fam_name __ 'AF_INET6':
                    ipv6_addr[interface] _ addr['addr']
                print ('    Address  : @'  addr['addr'])
                nmask _ addr.get('netmask', None)
                __ nmask:
                    print ('    Netmask  : @'  nmask)
                bcast _ addr.get('broadcast', None)
                __ bcast:
                    print ('    Broadcast: @'  bcast)
    __ ipv6_addr:
        print ("Found IPv6 address: @" ipv6_addr)
    ____
        print ("No IPv6 interface found!")  

   
__ _______ __ ______
    inspect_ipv6_support()

#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
# This program depends on Python modules netifaces and netaddr.

______ ?
______ netifaces __ ni
______ netaddr __ na

___ extract_ipv6_info
    """ Extracts IPv6 information"""
    print ("IPv6 support built into Python: @" ?.has_ipv6)
    ___ interface __ ni.interfaces
        all_addresses _ ni.ifaddresses(interface)
        print ("Interface @:" interface)
        ___ family,addrs __ all_addresses.items
            fam_name _ ni.address_families[family]

            ___ addr __ addrs:
                __ fam_name __ 'AF_INET6':
                    addr _ addr['addr']
                    has_eth_string _ addr.s..("eth")
                    __ has_eth_string:
                        addr _ addr.s..("eth")[0]
                    ___
                        print ("    IP Address: @" na.IPNetwork(addr))
                        print ("    IP Version: @" na.IPNetwork(addr).version)
                        print ("    IP Prefix length: @" na.IPNetwork(addr).prefixlen)
                        print ("    Network: @" na.IPNetwork(addr).network)
                        print ("    Broadcast: @" na.IPNetwork(addr).broadcast)
                    ______ E.. __ e:
                        print ("Skip Non-IPv6 Interface")

__ _______ __ ______
    extract_ipv6_info()

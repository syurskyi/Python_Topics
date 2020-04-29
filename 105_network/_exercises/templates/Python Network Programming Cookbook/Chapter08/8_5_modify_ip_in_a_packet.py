#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 8
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


______ a_p..
______ ___
______ re
____ random ______ randint

____ scapy.all ______ IP,TCP,UDP,conf,s..


___ send_packet(protocol_None, src_ip_None, src_port_None, flags_None, dst_ip_None, dst_port_None, iface_None):
    """Modify and send an IP packet."""
    __ protocol __ 'tcp':
        packet _ IP(src_src_ip, dst_dst_ip)/TCP(flags_flags, sport_src_port, dport_dst_port)
    ____ protocol __ 'udp':
        __ flags: r_ E..(" Flags are not supported for udp")
        packet _ IP(src_src_ip, dst_dst_ip)/UDP(sport_src_port, dport_dst_port)
    ____
        r_ E..("Unknown protocol @"  protocol)

    s..(packet, iface_iface)
   

__ _______ __ ______
    # setup commandline arguments
    parser _ ?.AP..(d.._'Packet Modifier')
    ?.a_a..('--iface', a.._"store", d.._"iface", d.._'eth0')
    ?.a_a..('--protocol', a.._"store", d.._"protocol", d.._'tcp')
    ?.a_a..('--src-ip', a.._"store", d.._"src_ip", d.._'1.1.1.1')
    ?.a_a..('--src-port', a.._"store", d.._"src_port", d.._randint(0, 65535))
    ?.a_a..('--dst-ip', a.._"store", d.._"dst_ip", d.._'192.168.1.51')
    ?.a_a..('--dst-port', a.._"store", d.._"dst_port", d.._randint(0, 65535))
    ?.a_a..('--flags', a.._"store", d.._"flags", d.._None)
    # parse arguments
    given_args _ ?.p_a..
    iface, protocol, src_ip,  src_port, dst_ip, dst_port, flags _  given_args.iface, given_args.protocol, given_args.src_ip,\
      given_args.src_port, given_args.dst_ip, given_args.dst_port, given_args.flags
    send_packet(protocol, src_ip, src_port, flags, dst_ip, dst_port, iface)


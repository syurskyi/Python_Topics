#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 8
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


____ scapy.all ______ *

___ modify_packet_header(pkt):
    """ Parse the header and add an extra header"""
    __ pkt.haslayer(TCP) and pkt.getlayer(TCP).dport __ 80 and pkt.haslayer(Raw):
        hdr _ pkt[TCP].payload.__dict__        
        extra_item _ {'Extra Header' : ' extra value'}
        hdr.update(extra_item)     
        send_hdr _ '\r\n'.j..(hdr)
        pkt[TCP].payload _ send_hdr
        
        pkt.show()
        
        del pkt[IP].chksum
        s..(pkt)

__ _______ __ ______
    # start sniffing
    sniff(filter_"tcp and ( port 80 )", prn_modify_packet_header)

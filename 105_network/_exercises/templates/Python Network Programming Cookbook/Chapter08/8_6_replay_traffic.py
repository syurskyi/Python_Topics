#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 8
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


______ a_p..
____ scapy.all ______ *


___ send_packet(recvd_pkt, src_ip, dst_ip, count):
    """ Send modified packets"""
    pkt_cnt _ 0
    p_out _ []

    ___ p __ recvd_pkt:
        pkt_cnt +_ 1
        new_pkt _ p.payload
        new_pkt[IP].dst _ dst_ip
        new_pkt[IP].src _ src_ip
        del new_pkt[IP].chksum
        p_out.ap..(new_pkt)
        __ pkt_cnt  count __ 0:
            s..(PacketList(p_out))
            p_out _ []

    # Send rest of packet
    s..(PacketList(p_out))
    print ("Total packets sent: d" pkt_cnt)

__ _______ __ ______
    # setup commandline arguments
    parser _ ?.AP..(d.._'Packet Sniffer')
    parser.a_a..('--infile', a.._"store", d.._"infile", default_'pcap1.pcap')
    parser.a_a..('--src-ip', a.._"store", d.._"src_ip", default_'1.1.1.1')
    parser.a_a..('--dst-ip', a.._"store", d.._"dst_ip", default_'2.2.2.2')
    parser.a_a..('--count', a.._"store", d.._"count", default_100, ty.._in.)
    # parse arguments
    given_args _ ga _ parser.parse_args()
    global src_ip, dst_ip
    infile, src_ip, dst_ip, count _  ga.infile, ga.src_ip, ga.dst_ip, ga.count
    ___
        pkt_reader _ PcapReader(infile)
        send_packet(pkt_reader, src_ip, dst_ip, count)
    ______ IOError:
        print ("Failed reading file @ contents"  infile)
        ___.e..(1)

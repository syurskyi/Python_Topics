#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 8
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


______ __
____ scapy.all ______ *

pkts _ []
count _ 0
pcapnum _ 0

___ write_cap(x):
    g.. pkts
    g.. count
    g.. pcapnum
    pkts.ap..(x)
    count +_ 1
    __ count __ 3:
        pcapnum +_ 1
        pname _ "pcapd.pcap"  pcapnum
        wrpcap(pname, pkts)
        pkts _ []
        count _ 0

___ test_dump_file
    print ("Testing the dump file...")
    dump_file _ "./pcap1.pcap"
    __ __.pa__.e..(dump_file):
        print ("dump fie @ found." dump_file)
        pkts _ sniff(offline_dump_file)
        count _ 0
        w__ (count <_2):
            print ("----Dumping pkt:@----" count)
            print (hexdump(pkts[count]))
            count +_ 1
        
    ____
        print ("dump fie @ not found." dump_file)

__ _______ __ ______
    print ("Started packet capturing and dumping... Press CTRL+C to exit")
    sniff(prn_write_cap)
    test_dump_file()


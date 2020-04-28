#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 8
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


____ scapy.all ______ *
______ __
captured_data _ dict()

END_PORT _ 1000
 
___ monitor_packet(pkt):
    __ IP __ pkt:
        __ pkt[IP].src not __ captured_data:
            captured_data[pkt[IP].src] _ []
 
    __ TCP __ pkt:
        __ pkt[TCP].sport <_  END_PORT:
            __ not st..(pkt[TCP].sport) __ captured_data[pkt[IP].src]:
                captured_data[pkt[IP].src].ap..(st..(pkt[TCP].sport))
 
    __.system('clear')
    ip_list _ sorted(captured_data.keys())
    ___ key __ ip_list:
        ports_', '.j..(captured_data[key])
        __ le. (captured_data[key]) __ 0:
            print ('@'  key)
        ____
            print ('@ (@)'  (key, ports))

__ _______ __ ______
    sniff(prn_monitor_packet, store_0)

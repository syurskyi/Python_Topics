# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 8
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# ______ a_p..
# ______ pcap
# ____ construct.protocols.ipstack ______ ip_stack
#
#
# ___ print_packet pktlen  data  timestamp
#     """ Callback for priniting the packet payload"""
#     __ no. ?
#         r_
#
#     stack _ ?.p.. ?
#     payload _ ?.n__.n__.n..
#     print p_l..
#
# ___ main
#     # setup commandline arguments
#     parser _ ?.AP.. d.._'Packet Sniffer'
#     ?.a_a.. '--iface'  a.._"store"  d.._"iface"  d.._'eth0'
#     ?.a_a.. '--port'  a.._"store"  d.._"port"  d.._80  ty.._in.
#     # parse arguments
#     given_args _ ?.p_a..
#     iface  port _  ?.?  ?.?
#     # start sniffing
#     pc _ ?.pO..
#     ?.o_l.. i..  1600  0  100
#     ?.s_f.. 'dst port d' p..  0  0
#
#     print ('Press CTRL+C to end capture')
#     ___
#         w__ T..
#             ?.d.. 1  p_p..
#     ______ K..:
#         print ('Packet statistics: d packets received, d packets dropped, d packets dropped by the interface'  ?.s..
#
# __ _______ __ ______
#     ?
#

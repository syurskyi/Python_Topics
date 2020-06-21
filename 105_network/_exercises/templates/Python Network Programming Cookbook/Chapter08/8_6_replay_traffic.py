# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 8
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
#
# ______ a_p..
# ____ scapy.all ______ _
#
#
# ___ send_packet recvd_pkt  src_ip  dst_ip  count
#     """ Send modified packets"""
#     pkt_cnt _ 0
#     p_out _  # list
#
#     ___ p __ recvd_pkt:
#         pkt_cnt +_ 1
#         new_pkt _ p.p_l..
#         ? I. .d.. _ d_i.
#         ? I. .s.. _ s_i.
#         de. ? I. .c_s..
#         p_o_.ap.. ?
#         __ pkt_cnt  count __ 0
#             s.. PL.. ?
#             p_o.. _ # # list
#
#     # Send rest of packet
#     s.. PL.. p_o..
#     print ("Total packets sent: d" p_c..
#
# __ _______ __ ______
#     # setup commandline arguments
#     parser _ ?.AP.. d.._'Packet Sniffer'
#     ?.a_a.. '--infile'  a.._"store"  d.._"infile"  d.._'pcap1.pcap'
#     ?.a_a.. '--src-ip'  a.._"store"  d.._"src_ip"  d.._'1.1.1.1'
#     ?.a_a.. '--dst-ip'  a.._"store"  d.._"dst_ip"  d.._'2.2.2.2'
#     ?.a_a.. '--count'  a.._"store"  d.._"count"  d.._100  ty.._in.
#     # parse arguments
#     given_args _ ga _ ?.p_a..
#     g.. src_ip  dst_ip
#     infile  src_ip  dst_ip  count _  ga.infile  ga.src_ip  ga.dst_ip  ga.count
#     ___
#         pkt_reader _ PR.. in..
#         ? p_r..  s_i.  d_i.  c..
#     ______ I..
#         print ("Failed reading file @ contents"  i..
#         ___.e.. 1

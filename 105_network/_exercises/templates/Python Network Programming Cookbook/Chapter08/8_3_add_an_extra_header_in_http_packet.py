# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 8
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
#
# ____ scapy.all ______ _
#
# ___ modify_packet_header pkt
#     """ Parse the header and add an extra header"""
#     __ ?.h_l_ T.. an. ?.g_l_ T.. .dp.. __ 80 an. ?.h_l_ R..
#         hdr _ ? T.. .p_l_. -d
#         extra_item _ {'Extra Header' : ' extra value'}
#         ?.u.. ?
#         send_hdr _ '\r\n'.j.. ?
#         ? T.. .p_l. _ ?
#
#         ?.s..
#
#         de. ? I. .c_s..
#         s..(?)
#
# __ _______ __ ______
#     # start sniffing
#     sniff fi.._"tcp and ( port 80 )", prn_modify_p_h..

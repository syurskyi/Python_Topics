# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 3
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
# # This program depends on Python module netifaces => 0.8
#
# ______ ?
# ______ a_p..
# ______ netifaces __ ni
#
#
# ___ inspect_ipv6_support
#     """ Find the ipv6 address"""
#     print ("IPV6 support built into Python: @" ?.has_ipv6)
#     ipv6_addr _ # dict
#     ___ interface __ ?.i..
#         all_addresses _ ?.if.. ?
#         print ("Interface @:" ?
#
#         ___ family,addrs __ a_a_.i..
#             fam_name _ ?.a_f.. f..
#             print ('  Address family: @' ?
#             ___ addr __ a..
#                 __ fam_name __ 'AF_INET6':
#                     _6.. i.. _ ? 'addr'
#                 print ('    Address  : @'  ? 'addr'
#                 nmask _ ?.g.. 'netmask' N..
#                 __ ?
#                     print ('    Netmask  : @' ?
#                 bcast _ a__.g.. 'broadcast' N..
#                 __ ?
#                     print ('    Broadcast: @' ?
#     __ _6_
#         print ("Found IPv6 address: @" ?
#     ____
#         print ("No IPv6 interface found!")
#
#
# __ _______ __ ______
#     ?

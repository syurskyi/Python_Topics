# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 3
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
# # This program depends on Python modules netifaces and netaddr.
#
# ______ ?
# ______ netifaces __ ni
# ______ netaddr __ na
#
# ___ extract_ipv6_info
#     """ Extracts IPv6 information"""
#     print ("IPv6 support built into Python: @" ?.__6
#     ___ interface __ ?.i..
#         all_addresses _ ?.if.. ?
#         print ("Interface @:" ?
#         ___ family,addrs __ a_a__.i..
#             fam_name _ ?.a_f.. f..
#
#             ___ addr __ a..
#                 __ fam_name __ 'AF_INET6'
#                     addr _ a.. 'addr'
#                     has_eth_string _ ?.s.. "eth"
#                     __ ?
#                         addr _ a__.s.. "eth" 0
#                     ___
#                         print ("    IP Address: @" ?.IPN.. a..
#                         print ("    IP Version: @" ?.IPN.. a.. .v..
#                         print ("    IP Prefix length: @" ?.IPN.. a.. .p..
#                         print ("    Network: @" ?.IPN.. a.. .n..
#                         print ("    Broadcast: @" ?.IPN.. a.. .b..
#                     ______ E.. __ e
#                         print ("Skip Non-IPv6 Interface")
#
# __ _______ __ ______
#     ?

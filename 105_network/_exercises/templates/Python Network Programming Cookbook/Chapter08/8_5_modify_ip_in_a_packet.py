# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 8
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
#
# ______ a_p..
# ______ ___
# ______ re
# ____ ra.. ______ r_i..
#
# ____ scapy.all ______ IP TCP UDP conf s..
#
#
# ___ send_packet protocol_N.. src_ip_N.. src_port_N.. flags_N.. dst_ip_N.. dst_port_N.. iface_N..
#     """Modify and send an IP packet."""
#     __ protocol __ 'tcp':
#         packet _ I. src_s.. dst_d..)/T.. flags_? sport_s_s.. dport_d..
#     ____ protocol __ 'udp':
#         __ flags: r_ E..(" Flags are not supported for udp")
#         packet _ I. src_s dst_d_i.)/UDP(sport_s.. dport_d..
#     ____
#         r_ E..("Unknown protocol @"  ?
#
#     s.. p.. i.._i..
#
#
# __ _______ __ ______
#     # setup commandline arguments
#     parser _ ?.AP.. d.._'Packet Modifier'
#     ?.a_a.. '--iface'  a.._"store"  d.._"iface"  d.._'eth0'
#     ?.a_a.. '--protocol'  a.._"store"  d.._"protocol"  d.._'tcp'
#     ?.a_a.. '--src-ip'  a.._"store"  d.._"src_ip"  d.._'1.1.1.1'
#     ?.a_a.. '--src-port'  a.._"store"  d.._"src_port"  d.._r_i.. 0  65535
#     ?.a_a.. '--dst-ip'  a.._"store"  d.._"dst_ip"  d.._'192.168.1.51')
#     ?.a_a.. '--dst-port'  a.._"store"  d.._"dst_port"  d.._r_i.. 0  65535
#     ?.a_a.. '--flags'  a.._"store"  d.._"flags"  d.._N..
#     # parse arguments
#     given_args _ ?.p_a..
#     iface  protocol  src_ip   src_port  dst_ip  dst_port  flags _  ?.?  ?.?  ?.? \
#       ?.?  ?.?  ?.?  ?.?
#     ? p.. s_i.  s_p..  f..  d_i.  d_p..  ?
#

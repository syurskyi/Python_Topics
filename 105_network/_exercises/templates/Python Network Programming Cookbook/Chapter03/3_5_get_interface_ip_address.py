# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 3
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ a_p..
# ______ ___
# ______ ?
# ______ fcntl
# ______ st__
# ______ a___
#
#
# ___ get_ip_address ifname
#     s _ ?.? ?.A.. ?.S_D..
#     r_ ?.i_n.. fc__.io..(
#         s.f_n..
#         0x8915,  # SIOCGIFADDR
#         st__.p.. b'256s' by.. ?|;15 'utf-8'
#     20;24
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'Python networking utils'
#     ?.a_a..('--ifname' a.._"store" d.._"ifname" r.._T..
#     given_args _ ?.p_a..
#     ifname _ ?.if..
#     print ("Interface [@] --> IP: @" ? ? ?

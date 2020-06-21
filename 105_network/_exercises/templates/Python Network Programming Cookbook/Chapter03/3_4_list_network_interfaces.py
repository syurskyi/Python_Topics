# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 3
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ ___
# ______ s..
# ______ fcntl
# ______ st__
# ______ a___
#
# SIOCGIFCONF _ 0x8912 #from C library sockios.h
# STUCT_SIZE_32 _ 32
# STUCT_SIZE_64 _ 40
# PLATFORM_32_MAX_NUMBER _  2**32
# DEFAULT_INTERFACES _ 8
#
#
# ___ list_interfaces
#     interfaces _ # list
#     max_interfaces _ D_I..
#     is_64bits _ ___.m_s.. > P_3_M_N..
#     struct_size _ S_S_64 __ is_64bits ____ S_S_32
#     sock _ ?.? ?.A.. ?.S_D..
#     w__ T..
#         by.. _ m_ * s_s..
#         interface_names _ a___.a___ 'B', b'\0' * by..
#         sock_info _ fc__.io..(
#             ?.f_n..
#             SI..
#             st__.p.. 'iL', by.. i_n_.b_i.. 0
#         )
#         outbytes _ st__.u.. 'iL' s_i.. 0
#         __ ? __ by..
#             m_i.. *_ 2
#         ____
#             b..
#     namestr _ i_n_.tost..
#     ___ i __ ra.. 0 o.. s_s..
#         i__.ap.. ?|?:?+16|.s.. b'\0', 1) 0 .d.. 'ascii', 'ignore'
#     r_ ?
#
#
# __ _______ __ ______
#     interfaces _ l_i..
#     print ("This machine has @ network interfaces: @." le. ? ?
#

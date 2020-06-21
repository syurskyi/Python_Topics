# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 3
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ a_p..
# ______ ?
# ______ ___
#
# HOST _ 'localhost'
# BUFSIZE _ 1024
#
# ___ ipv6_echo_client port
#                      host_?
#     ___ res __ ?.g_a_i.. h.. p.. ?.A_U.. ?.S..
#         af, socktype, proto, canonname, sa _ res
#         ___
#             sock _ ?.?( ? ? ?
#         ______ ?.e.. __ err
#             print ("Error:@" ?
#         ___
#             ?.c.. sa
#         ______ ?.e.. __ msg
#             sock.c..
#             c..
#     __ sock is N..
#         print ('Failed to open socket!')
#         ___.e.. 1
#     msg _ "Hello from ipv6 client"
#     print ("Send data to server: @" ?
#     ?.s.. by.. ?.e.. 'utf-8'
#     w__ T..
#         data _ ?.r.. B..
#         print ('Received from server', re.. ?
#         __ no. ?
#             b..
#     ?.c..
#
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'IPv6 socket client example'
#     ?.a_a.. '--port' a.._"store" d.._"port" ty.._in. r.._T..
#     given_args _ ?.p_a..
#     port _ ?.p..
#     ? ?

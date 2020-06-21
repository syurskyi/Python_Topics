# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 1
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ ___
# ______ s..
# ______ a_p..
#
#
# ___ main
#     # setup argument parsing
#     parser _ ?.AP.. d.._'Socket Error Examples'
#     ?.a_a.. '--host' a.._"store" d.._"host" r.._F..
#     ?.a_a.. '--port' a.._"store" d.._"port" ty.._in. r.._F..
#     ?.a_a.. '--file' a.._"store" d.._"file" r.._F..
#     given_args _ ?.p_a..
#     host _ ?.h..
#     port _ ?.p..
#     filename _ ?.f..
#
#     # First try-except block -- create socket
#     ___
#         s _ ?.? ?.A.. ?.S..
#     ______ ?.e.. __ e
#         print ("Error creating socket: @" ?
#         ___.e.. 1
#
#     # Second try-except block -- connect to given host/port
#     ___
#         s.c.. ? ?
#     ______ ?.g.. __ e
#         print ("Address-related error connecting to server: @"  e)
#         ___.e.. 1
#     ______ ?.e.. __ e
#         print ("Connection error: @"  ?
#         ___.e.. 1
#
#     # Third try-except block -- sending data
#     ___
#         msg _ "GET @ HTTP/1.0\r\n\r\n"  f..
#         s.s_a.. ?g.e.. 'utf-8'
#     ______ ?.e.. __ e
#         print ("Error sending data: @" ?
#         ___.e.. 1
#
#     w__ 1
#         # Fourth tr-except block -- waiting to receive data from remote host
#         ___
#             buf _ s.r.. 2048
#         ______ ?.e.. __ e
#             print ("Error receiving data: @" ?
#             ___.e.. 1
#         __ no. le. b..
#             b..
#         # write the received data
#         ___.stdout.write(buf.d.. 'utf-8'
#
# __ _______ __ ______
#     ?

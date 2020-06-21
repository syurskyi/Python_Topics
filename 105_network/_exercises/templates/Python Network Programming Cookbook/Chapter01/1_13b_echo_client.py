# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 1
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ s..
# ______ ___
#
# ______ a_p..
#
# host _ 'localhost'
#
# ___ echo_client port
#     """ A simple echo client """
#     # Create a TCP/IP socket
#     sock _ ?.? ?.A.. ?.S..
#     # Connect the socket to the server
#     server_address _ ? ?
#     print ("Connecting to @ port @" ?
#     ?.c.. ?
#
#     # Send data
#     ___
#         # Send data
#         message _ "Test message. This will be echoed"
#         print ("Sending @" ?
#         ?.s_a.. ?.e.. 'utf-8'
#         # Look for the response
#         amount_received _ 0
#         amount_expected _ le. ?
#         w__ ? < ?
#             data _ ?.r..(16)
#             a_r.. +_ le. ?
#             print ("Received: @"  ?
#     ______ ?.e.. __ e
#         print ("Socket error: @" st.. ?
#     ______ E.. __ e
#         print ("Other exception: @" st.. ?
#     f..
#         print ("Closing connection to the server")
#         ?.c..
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'Socket Server Example'
#     ?.a_a.. '--port' a.._"store" d.._"port" ty.._in. r.._T..
#     given_args _ ?.p_a..
#     port _ ?.p..
#     ? ?

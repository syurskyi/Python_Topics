# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 7
# # This program is optimized for Python 3.5.2.
# # To make it work with Python 2.7.12:
# #      Follow through the code inline for some changes.
# # It may run on any other version with/without modifications.
#
#
# ______ a_p..
# ______ xmlrpc
# # Comment out the above line and uncomment the below line for Python 2.x.
# #import xmlrpclib
# ____ base64 ______ b64decode
#
# ____ xmlrpc.s.. ______ SimpleXMLRPCServer   SimpleXMLRPCRequestHandler
# # Comment out the above line and uncomment the below line for Python 2.x.
# #from SimpleXMLRPCServer  import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
#
#
# c_ SecureXMLRPCServer S_S..
#
#     ___ -  host   port   username   password   $ $$
#         u.. _ u..
#         p.. _ p..
#         # authenticate method is called from inner class
#         c_ VerifyingRequestHandler(S_RH..
#               # method to override
#               ___ p_r.. r..
#                   __ S_RH__.p_r.. r..
#                       # authenticate
#                       __ authenticate r__.h..
#                           r_ T..
#                       ____
#                           # if authentication fails return 401
#                           r__.s_e.. 401 'Authentication failed, Try agin.'
#                   r_ F..
#         # initialize
#         S_S__.-  h.. p.. rH.._VRH.. $ $$
#
#     ___ authenticate headers
#         headers _ ?.g.. 'Authorization' .s..
#         basic   encoded _ ? 0 ? 1
#         __ b.. !_ 'Basic'
#             print ('Only basic authentication supported')
#             r_ F..
#         secret _ b6_d.. e.. .s.. _':'
#
#         username  password _ ? 0 .d.. "utf-8" ? 1 .d.. "utf-8"
#         r_ T.. __ ? __ ? an. ? __ ? ____ F..
#
#
# ___ run_server host  port  username  password
#     server _ S_S.. ? ? ? ?
#     # simple test function
#     ___ echo msg
#         """Reply client in  uppser case """
#         reply _ ?.u..
#         print ("Client said: @. So we echo that in uppercase: @" ? ?
#         r_ ?
#     s__.r_f.. e.. 'echo'
#     print ("Running a HTTP auth enabled XMLRPC server on @:@..." h.. p..
#     s__.s_f..
#
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'Multithreaded multicall XMLRPC Server/Proxy'
#     ?.a_a.. '--host'  a.._"store"  d.._"host"  d.._'localhost'
#     ?.a_a.. '--port'  a.._"store"  d.._"port"  d.._8000  ty.._in.
#     ?.a_a.. '--username'  a.._"store"  d.._"username"  d.._'user'
#     ?.a_a.. '--password'  a.._"store"  d.._"password"  d.._'pass'
#     # parse arguments
#     given_args _ ?.p_a..
#     host  port _  ?.?  ?.?
#     username  password _ ?.?  ?.?
#     ? h.. p.. u.. p..

# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 7
# # This program is optimized for Python 3.5.2.
# # To make it work with Python 2.7.12:
# #      Follow through the code inline for some changes.
# # It may run on any other version with/without modifications.
#
# ______ a_p..
# ______ xmlrpc
# # Comment out the above line and uncomment the below line for Python 2.x.
# #import xmlrpclib
# ______ th..
#
# ____ xmlrpc.s.. ______ SimpleXMLRPCServer
# # Comment out the above line and uncomment the below line for Python 2.x.
# #from SimpleXMLRPCServer import SimpleXMLRPCServer
#
# # some trivial functions
# ___ add x y
#     r_ x+y
#
# ___ subtract x  y
#     r_ x-y
#
# ___ multiply x  y
#     r_ x*y
#
# ___ divide x  y
#     r_ x/y
#
#
# c_ ServerThread ?.T..
#     ___ -  server_addr
#         ?.T...- (self)
#         server _ S.. ?
#         ?.r_m_f..
#         ?.r_f.. ? 'add'
#         ?.r_f.. ? 'subtract'
#         ?.r_f.. ? 'multiply'
#         ?.r_f.. ? 'divide'
#
#     ___ run
#         ?.s_f..
#
# ___ run_server ? ?
#     # server code
#     server_addr _ ? ?
#     ? _ ? s_a..
#     ?.s.. # The server is now running
#     print ("Server thread started. Testing the server...")
#
# ___ run_client ? ?
#
#     # client code
#     proxy _ x__.cl__.SP.. "http://@:@/" ? ?
#     # Comment out the above line and uncomment the below line for Python 2.x.
#     #proxy = xmlrpclib.ServerProxy("http://@:@/" (host, port))
#
#     multicall _ x__.cl++.MC.. ?
#     # Comment out the above line and uncomment the below line for Python 2.x.
#     #multicall = xmlrpclib.MultiCall(proxy)
#
#     ?.a.. 7 3
#     ?.s.. 7 3
#     ?.m... 7 3
#     ?.d.. 7 3
#     result _ ?()
#     print ("7+3=d, 7-3=d, 7*3=d, 7/3=d"  tu.. ?
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'Multithreaded multicall XMLRPC Server/Proxy'
#     ?.a_a..'--host'  a.._"store"  d.._"host"  d.._'localhost'
#     ?.a_a..'--port'  a.._"store"  d.._"port"  d.._8000  ty.._in.
#     # parse arguments
#     given_args _ ?.p_a..
#     host  port _  ?.host  ?.port
#     r_s ..? ?
#     r_c.. ? ?
#

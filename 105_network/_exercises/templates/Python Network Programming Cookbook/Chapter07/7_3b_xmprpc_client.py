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
#
# ____ xmlrpc.s.. ______ S_S..
# # Comment out the above line for Python 2.x.
#
# ___ run_client host  port  username  password
#     server _ ?.c__.SP.. 'http://@:@@@:@' u.. p.. h.. p..
#     # Comment out the above line and uncomment the below line for Python 2.x.
#     #server = xmlrpclib.ServerProxy('http://@:@@@:@' (username, password, host, port, ))
#     msg _ "hello server..."
#     print ("Sending message to server: @  " ?
#     print ("Got reply: @" s...e.. ?
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
#     username  password _ ?.? ?.?
#     ? h.. p.. u.. p..

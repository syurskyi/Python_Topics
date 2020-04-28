#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 7
# This program is optimized for Python 3.5.2.
# To make it work with Python 2.7.12:
#      Follow through the code inline for some changes.
# It may run on any other version with/without modifications.


______ a_p..
______ xmlrpc
# Comment out the above line and uncomment the below line for Python 2.x.
#import xmlrpclib

____ xmlrpc.server ______ SimpleXMLRPCServer
# Comment out the above line for Python 2.x.

___ run_client(host, port, username, password):
    server _ xmlrpc.client.ServerProxy('http://@:@@@:@' (username, password, host, port, ))
    # Comment out the above line and uncomment the below line for Python 2.x.
    #server = xmlrpclib.ServerProxy('http://@:@@@:@' (username, password, host, port, ))
    msg _ "hello server..."
    print ("Sending message to server: @  " msg)
    print ("Got reply: @" server.echo(msg))

__ _______ __ ______
    parser _ ?.AP..(d.._'Multithreaded multicall XMLRPC Server/Proxy')
    ?.a_a..('--host', a.._"store", d.._"host", default_'localhost')
    ?.a_a..('--port', a.._"store", d.._"port", default_8000, ty.._in.)
    ?.a_a..('--username', a.._"store", d.._"username", default_'user')
    ?.a_a..('--password', a.._"store", d.._"password", default_'pass')
    # parse arguments
    given_args _ ?.parse_args()
    host, port _  ?.host, ?.port
    username, password _ ?.username, ?.password
    run_client(host, port, username, password)

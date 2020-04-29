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
______ th..

____ xmlrpc.s.. ______ SimpleXMLRPCServer
# Comment out the above line and uncomment the below line for Python 2.x.
#from SimpleXMLRPCServer import SimpleXMLRPCServer

# some trivial functions
___ add(x,y):
    r_ x+y

___ subtract(x, y):
    r_ x-y

___ multiply(x, y):
    r_ x*y

___ divide(x, y):
    r_ x/y


c_ ServerThread(?.T..):
    ___ -  server_addr):
        ?.T...- (self)
        server _ SimpleXMLRPCServer(server_addr)
        server.register_multicall_functions()
        server.register_function(add, 'add')
        server.register_function(subtract, 'subtract')
        server.register_function(multiply, 'multiply')
        server.register_function(divide, 'divide')

    ___ run
        server.serve_forever()
        
___ run_server(host, port):
    # server code
    server_addr _ (host, port)
    server _ ServerThread(server_addr)
    server.s.. # The server is now running
    print ("Server thread started. Testing the server...")

___ run_client(host, port):

    # client code
    proxy _ xmlrpc.client.ServerProxy("http://@:@/" (host, port))
    # Comment out the above line and uncomment the below line for Python 2.x.
    #proxy = xmlrpclib.ServerProxy("http://@:@/" (host, port))

    multicall _ xmlrpc.client.MultiCall(proxy)
    # Comment out the above line and uncomment the below line for Python 2.x.
    #multicall = xmlrpclib.MultiCall(proxy)

    multicall.add(7,3)
    multicall.subtract(7,3)
    multicall.multiply(7,3)
    multicall.divide(7,3)
    result _ multicall()
    print ("7+3=d, 7-3=d, 7*3=d, 7/3=d"  tuple(result))

__ _______ __ ______
    parser _ ?.AP..(d.._'Multithreaded multicall XMLRPC Server/Proxy')
    parser.a_a..('--host', a.._"store", d.._"host", d.._'localhost')
    parser.a_a..('--port', a.._"store", d.._"port", d.._8000, ty.._in.)
    # parse arguments
    given_args _ parser.parse_args()
    host, port _  given_args.host, given_args.port
    run_server(host, port)
    run_client(host, port)


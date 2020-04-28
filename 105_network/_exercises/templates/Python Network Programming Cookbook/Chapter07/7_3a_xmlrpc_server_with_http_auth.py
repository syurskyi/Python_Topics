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
____ base64 ______ b64decode

____ xmlrpc.server ______ SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
# Comment out the above line and uncomment the below line for Python 2.x.
#from SimpleXMLRPCServer  import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler


c_ SecureXMLRPCServer(SimpleXMLRPCServer):

    ___ -  host, port, username, password, $, **kargs):
        username _ username
        password _ password
        # authenticate method is called from inner class
        c_ VerifyingRequestHandler(SimpleXMLRPCRequestHandler):
              # method to override
              ___ parse_request(request):
                  __ SimpleXMLRPCRequestHandler.parse_request(request):
                      # authenticate
                      __ authenticate(r__.headers):
                          r_ T..
                      ____
                          # if authentication fails return 401
                          request.send_error(401, 'Authentication failed, Try agin.')
                  r_ F..
        # initialize
        SimpleXMLRPCServer.-  (host, port), requestHandler_VerifyingRequestHandler, $, **kargs)

    ___ authenticate headers):
        headers _ headers.get('Authorization').s..()
        basic, encoded _ headers[0], headers[1]
        __ basic !_ 'Basic':
            print ('Only basic authentication supported')
            r_ F..
        secret _ b64decode(encoded).s..(b':')
        
        username, password _ secret[0].d..("utf-8"), secret[1].d..("utf-8")
        r_ T.. __ (username __ username and password __ password) ____ F..
    

___ run_server(host, port, username, password):
    server _ SecureXMLRPCServer(host, port, username, password)
    # simple test function
    ___ echo(msg):
        """Reply client in  uppser case """
        reply _ msg.upper()
        print ("Client said: @. So we echo that in uppercase: @" (msg, reply))
        r_ reply
    server.register_function(echo, 'echo')
    print ("Running a HTTP auth enabled XMLRPC server on @:@..." (host, port))
    server.serve_forever()


__ _______ __ ______
    parser _ ?.AP..(d.._'Multithreaded multicall XMLRPC Server/Proxy')
    parser.a_a..('--host', a.._"store", d.._"host", default_'localhost')
    parser.a_a..('--port', a.._"store", d.._"port", default_8000, ty.._in.)
    parser.a_a..('--username', a.._"store", d.._"username", default_'user')
    parser.a_a..('--password', a.._"store", d.._"password", default_'pass')
    # parse arguments
    given_args _ parser.parse_args()
    host, port _  given_args.host, given_args.port
    username, password _ given_args.username, given_args.password
    run_server(host, port, username, password)

#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.
# Requires pyOpenSSL and SSL packages installed

______ ?, __
____ OpenSSL ______ SSL

____ s_s ______ BaseServer
____ http.server ______ HTTPServer
____ http.server ______ SimpleHTTPRequestHandler
# Comment out the above 3 lines and uncomment the below 3 lines for Python 2.7.x.
#from SocketServer import BaseServer
#from BaseHTTPServer import HTTPServer
#from SimpleHTTPServer import SimpleHTTPRequestHandler


c_ SecureHTTPServer(HTTPServer):
    ___ -  server_address, HandlerClass):
        BaseServer.-  server_address, HandlerClass)
        ctx _ SSL.Context(SSL.SSLv23_METHOD)
        fpem _ 'server.pem' # location of the server private key and the server certificate
        ctx.use_privatekey_file (fpem)
        ctx.use_certificate_file(fpem)
        ? _ SSL.Connection(ctx, ?.?(address_family,
                                                        socket_type))
        server_bind()
        server_activate()


c_ SecureHTTPRequestHandler(SimpleHTTPRequestHandler):
    ___ setup
        connection _ request
        rfile _ ?._fileobject(request, "rb", rbufsize)
        wfile _ ?._fileobject(request, "wb", wbufsize)


___ run_server(HandlerClass _ SecureHTTPRequestHandler,
         ServerClass _ SecureHTTPServer):
    server_address _ ('', 4443) # port needs to be accessible by user
    server _ ServerClass(server_address, HandlerClass)
    running_address _ server.?.g_s_n..()
    print ("Serving HTTPS Server on @:@ ..." (running_address[0], running_address[1]))
    server.serve_forever()


__ _______ __ ______
    run_server()


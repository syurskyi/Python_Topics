#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.


______ ?
______ ___

____ http.server ______ BaseHTTPRequestHandler, HTTPServer
# Comment out the above line and uncomment the below for Python 2.7.x.
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

DEFAULT_HOST _ '127.0.0.1'
DEFAULT_PORT _ 8800


c_ RequestHandler(BaseHTTPRequestHandler):
    """ Custom request handler"""
    
    ___ do_GET
        """ Handler for the GET requests """
        send_response(200)
        send_header('Content-type','text/html')
        end_headers()
        # Send the message to browser
        wfile.write("Hello from server!")
        r_
    

c_ CustomHTTPServer(HTTPServer):
    "A custom HTTP server"
    ___ -  host, port):
        server_address _ (host, port)
        HTTPServer.-  server_address, RequestHandler)
        

___ run_server(port):
    ___
        server_ CustomHTTPServer(DEFAULT_HOST, port)
        print ("Custom HTTP server started on port: @"  port)
        server.serve_forever()
    ______ E.. __ err:
        print ("Error:@" err)
    ______ K..:
        print ("Server interrupted and is shutting down...")
        server.?.c..


__ _____ __ ______
    parser _ ?.AP..(d.._'Simple HTTP Server Example')
    ?.a_a..('--port', a.._"store", d.._"port", ty.._in., default_DEFAULT_PORT)
    given_args _ ?.p_a..
    port _ ?.port
    run_server(port)

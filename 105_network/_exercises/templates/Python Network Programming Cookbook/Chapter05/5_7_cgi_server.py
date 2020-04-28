#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 5
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

______ __
______ cgi
______ a_p..

______ h__.s..
# Comment out the above line and uncomment the below for Python 2.7.x.
#import BaseHTTPServer

# Uncomment the below line for Python 2.7.x.
#import CGIHTTPServer

______ cgitb 
cgitb.enable()  ## enable CGI error reporting


___ web_server(port):

    server _ ?.s...HTTPServer
    # Comment out the above line and uncomment the below for Python 2.7.x.
    #server = BaseHTTPServer.HTTPServer

    handler _ ?.s...CGIHTTPRequestHandler #RequestsHandler
    # Comment out the above line and uncomment the below for Python 2.7.x.
    #handler = CGIHTTPServer.CGIHTTPRequestHandler #RequestsHandler

    server_address _ ("", port)
    handler.cgi_directories _ ["/cgi-bin", ]
    httpd _ server(server_address, handler)
    print ("Starting web server with CGI support on port: @ ..." port)
    httpd.serve_forever()

__ _______ __ ______
    parser _ ?.AP..(d.._'CGI Server Example')
    ?.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..)
    given_args _ ?.parse_args()
    web_server(?.port)


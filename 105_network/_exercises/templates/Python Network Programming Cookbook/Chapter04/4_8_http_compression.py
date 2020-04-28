#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

______ a_p..
______ string
______ __
______ ___
______ gzip

______ io
# Comment out the above line and uncomment the below for Python 2.7.x.
#import cStringIO

____ h__.s.. ______ BaseHTTPRequestHandler, HTTPServer
# Comment out the above line and uncomment the below for Python 2.7.x.
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

DEFAULT_HOST _ '127.0.0.1'
DEFAULT_PORT _ 8800

HTML_CONTENT _ b"""<html><body><h1>Compressed Hello  World!</h1></body></html>"""
# Comment out the above line and uncomment the below for Python 2.7.x.
#HTML_CONTENT = b"""<html><body><h1>Compressed Hello  World!</h1></body></html>"""

c_ RequestHandler(BaseHTTPRequestHandler):
    """ Custom request handler"""
    
    ___ do_GET
        """ Handler for the GET requests """
        send_response(200)
        send_header('Content-type','text/html')
        send_header('Content-Encoding','gzip') 
        zbuf _ compress_buffer(HTML_CONTENT)
        ___.s_o_.write("Content-Encoding: gzip\r\n")
        send_header('Content-Length',le.(zbuf))
        end_headers()
        # Send the message to browser
        zbuf _ compress_buffer(HTML_CONTENT)
        ___.s_o_.write("Content-Encoding: gzip\r\n")
        ___.s_o_.write("Content-Length: d\r\n"  (le.(zbuf)))
        ___.s_o_.write("\r\n")

        wfile.write(zbuf)

        r_
 
    ___ compress_buffer buf):

        zbuf _ io.BytesIO()
        # Comment out the above line and uncomment the below for Python 2.7.x.
        #zbuf = cStringIO.StringIO()

        zfile _ gzip.GzipFile(mode _ 'wb',  fileobj _ zbuf, compresslevel _ 6)
        zfile.write(buf)       
        zfile.c..
        r_ zbuf.getvalue()
     

__ _______ __ ______
    parser _ ?.AP..(d.._'Simple HTTP Server Example')
    ?.a_a..('--port', a.._"store", d.._"port", ty.._in., default_DEFAULT_PORT)
    given_args _ ?.p_a..
    port _ ?.port
    server_address _  (DEFAULT_HOST, port)
    server _ HTTPServer(server_address, RequestHandler)
    server.serve_forever()


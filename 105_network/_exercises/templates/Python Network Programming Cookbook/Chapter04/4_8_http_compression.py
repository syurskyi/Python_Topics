# #!/usr/bin/env python
# # Python Network Programming Cookbook -- Chapter - 4
# # This program requires Python 3.5.2 or any later version
# # It may run on any other version with/without modifications.
# #
# # Follow the comments inline to make it run on Python 2.7.x.
#
# ______ a_p..
# ______ str..
# ______ __
# ______ ___
# ______ gzip
#
# ______ io
# # Comment out the above line and uncomment the below for Python 2.7.x.
# #import cStringIO
#
# ____ h__.s.. ______ BHRH.. H_S..
# # Comment out the above line and uncomment the below for Python 2.7.x.
# #from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#
# DEFAULT_HOST _ '127.0.0.1'
# DEFAULT_PORT _ 8800
#
# HTML_CONTENT _ b"""<html><body><h1>Compressed Hello  World!</h1></body></html>"""
# # Comment out the above line and uncomment the below for Python 2.7.x.
# #HTML_CONTENT = b"""<html><body><h1>Compressed Hello  World!</h1></body></html>"""
#
# c_ RequestHandler BHRH..
#     """ Custom request handler"""
#
#     ___ do_GET
#         """ Handler for the GET requests """
#         s_r.. 200
#         s_h.. 'Content-type','text/html'
#         send_header 'Content-Encoding','gzip')
#         zbuf _ c_b.. _C..
#         ___.s_o_.w..("Content-Encoding: gzip\r\n")
#         se_h.. 'Content-Length',le.?
#         e_h..
#         # Send the message to browser
#         zbuf _ c_b.. _C..
#         ___.s_o_.w.. "Content-Encoding: gzip\r\n")
#         ___.s_o_.w.. "Content-Length: d\r\n"   le. ?
#         ___.s_o_.w.. "\r\n")
#
#         wf__.w.. ?
#
#         r_
#
#     ___ compress_buffer buf
#
#         zbuf _ __.BI..
#         # Comment out the above line and uncomment the below for Python 2.7.x.
#         #zbuf = cStringIO.StringIO()
#
#         zfile _ ?.GF.. m.. _ __  f_o.. _ zb.. c_l.. _ 6)
#         ?.w.. b..
#         ?.c..
#         r_ zb__.g_v..
#
#
# __ _______ __ ______
#     parser _ ?.AP..(d.._'Simple HTTP Server Example')
#     ?.a_a..('--port', a.._"store", d.._"port", ty.._in., default_DEFAULT_PORT)
#     given_args _ ?.p_a..
#     port _ ?.port
#     server_address _  (DEFAULT_HOST, port)
#     server _ HTTPServer(server_address, RequestHandler)
#     server.serve_forever()
#

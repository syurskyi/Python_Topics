# #!/usr/bin/env python
# # Python Network Programming Cookbook -- Chapter - 4
# # This program requires Python 3.5.2 or any later version
# # It may run on any other version with/without modifications.
# #
# # Follow the comments inline to make it run on Python 2.7.x.
# # Requires pyOpenSSL and SSL packages installed
#
# ______ ? __
# ____ OpenSSL ______ SSL
#
# ____ s_s ______ BS..
# ____ h__.s.. ______ H_S..
# ____ h__.s.. ______ S_HRH..
# # Comment out the above 3 lines and uncomment the below 3 lines for Python 2.7.x.
# #from SocketServer import BaseServer
# #from BaseHTTPServer import HTTPServer
# #from SimpleHTTPServer import SimpleHTTPRequestHandler
#
#
# c_ SecureHTTPServer H..
#     ___ -  server_address HandlerClass
#         BS__.-  s_a.. HC..
#         ctx _ ?.C.. ?.S_23_M..
#         fpem _ 'server.pem' # location of the server private key and the server certificate
#         c__.u_p_f.. ?
#         c__.u_c_f.. ?
#         ? _ ?.C.. c__ ?.? a_f..
#                                                         s_t..
#         s_b..
#         s_a..
#
#
# c_ SecureHTTPRequestHandler S_HRH..
#     ___ setup
#         connection _ request
#         rfile _ ?._f_o.. ? __ rb_s..
#         wfile _ ?._f_o.. ? __ wb_s..
#
#
# ___ run_server HandlerClass _ ?
#          ServerClass _ S_HS..
#     server_address _ ('', 4443) # port needs to be accessible by user
#     server _ ? s_a.. HC..
#     running_address _ ?.?.g_s_n..
#     print ("Serving HTTPS Server on @:@ ..." ? 0 ? 1
#     s...s_f..
#
#
# __ _______ __ ______
#     ?
#

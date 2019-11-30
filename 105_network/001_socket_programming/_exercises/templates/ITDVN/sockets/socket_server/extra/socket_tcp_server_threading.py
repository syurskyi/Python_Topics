# ______ s......
#
#
# c___ ThreadingTCPServer s____.ThreadingMixIn s____.TCPServer
#     p____
#
#
# c_ EchoTCPHandler s____.BaseRequestHandler
#
#     ___ handle self
#         data _ ____.req____.r.... 1024 . st....
#         print *Address: ||*.f... ____.client_address|0|
#         print *Data: ||*.f... d___.dec___
#         ____.req___.sen___ d...
#
#
# __ __n_ __ _________
#     w___ ThreadingTCPServer '' 8888 EchoTCPHandler a_ server
#         s_____.serve_forever

# #!/usr/bin/env python
# # Python Network Programming Cookbook -- Chapter - 4
# # This program requires Python 3.5.2 or any later version
# # It may run on any other version with/without modifications.
# #
# # Follow the comments inline to make it run on Python 2.7.x.
#
# ______ a_p..
#
# ______ h__.c..
# # Comment out the above line and uncomment the below for Python 2.7.x.
# #import httplib
#
# ______ u__.p..
# # Comment out the above line and uncomment the below for Python 2.7.x.
# #import urlparse
#
# ______ re
# ______ u__.r__, u__.e..
# # Comment out the above line and uncomment the below for Python 2.7.x.
# #import urllib
#
# DEFAULT_URL _ 'http://www.python.org'
#
# HTTP_GOOD_CODES _  [?.c__.O. ?.c__.F.. ?.c__.M_P..
# # Comment out the above line and uncomment the below for Python 2.7.x.
# #HTTP_GOOD_CODES =  [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
#
# ___ get_server_status_code url
#     """
#     Download just the header of a URL and
#     return the server's status code.
#     """
#     host, pa__ _ ?.p__.u_p.. ? 1;3
#     # Comment out the above line and uncomment the below for Python 2.7.x.
#     #host, path = urlparse.urlparse(url)[1:3]
#     ___
#         conn _ ?.c__.H_C.. ?
#         # Comment out the above line and uncomment the below for Python 2.7.x.
#         #conn = httplib.HTTPConnection(host)
#
#         ?.r__('HEAD', pa__
#         r_ conn.g_rp__.s..
#
#     ______ E.. __ e
#         print ("Server: @ status is: @ " u.. ?
#         # Comment out the above line and uncomment the below for Python 2.7.x.
#         #except StandardError:
#         r_ N..
#
# __ _______ __ ______
#     parser _ ?.AP..(d.._'Example HEAD Request')
#     ?.a_a.. '--url' a.._"store" d.._"url" d.._D_U..
#     given_args _ ?.p_a..
#     url _ ?.u..
#     __ ? ? __ H..
#         print ("Server: @ status is OK: @ " ? ? ?
#     ____
#         print ("Server: @ status is NOT OK: @" ? ? ?

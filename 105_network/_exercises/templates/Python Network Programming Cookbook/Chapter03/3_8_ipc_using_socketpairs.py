# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 3
# # This program is optimized for Python 3.5.2.
# # It may run on any other version with/without modifications.
# # To make it run on Python 2.7.x, needs some changes due to API differences.
# # Follow the comments inline to make the program work with Python 2.
#
# ______ ?
# ______ __
#
# BUFSIZE _ 1024
#
# ___ test_socketpair
#     """ Test Unix socketpair"""
#     parent, child _ ?.s_p..
#
#     pid _ __.f..
#     ___
#         __ pid
#             print ("@Parent, sending message...")
#             c__.c..
#
#             p__.s_a.. by.. "Hello from parent!", 'utf-8'
#             # Comment out the above line and uncomment the below line for Python 2.7.
#             # parent.sendall("Hello from parent!")
#
#             response _ p__.r.. B..
#             print ("Response from child:" ?
#             p__.c..
#
#         ____
#             print ("@Child, waiting for message from parent")
#             p__.c..
#             message _ c__.r.. B..
#             print ("Message from parent:' ?
#
#             c_.s_a.. by.. "Hello from child!!" 'utf-8'
#             # Comment out the above line and uncomment the below line for Python 2.7.
#             # child.sendall("Hello from child!!")
#
#             c__.c..
#     ______ E.. __ err
#         print ("Error: @" ?
#
#
# __ _______ __ ______
#     ?

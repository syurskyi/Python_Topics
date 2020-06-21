# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 1
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ s..
# ______ ___
#
#
# ___ reuse_socket_addr
#     sock _ ?.? ?.A.. ?.S..
#
#     # Get the old state of the SO_REUSEADDR option
#     old_state _ ?.g_s_o..(?.S_S.., ?.S_R..
#     print ("Old sock state: @" ?
#
#     # Enable the SO_REUSEADDR option
#     ?.s_s_o.. ?.S_S.., ?.S_R.. 1
#     new_state _ ?.g_s_o.. ?.S_S.. ?.S_R..
#     print ("New sock state: @" ?
#
#     local_port _ 8282
#
#     srv _ ?.? ?.A.. ?.S..
#     ?.s_s_o..(?.S_S.., ?.S_R.. 1
#     ?.b.. '' l_p..
#     ?.l.. 1
#     print ("Listening on port: @ " ?
#     w__ T..
#         ___
#             connection, addr _ ?.a..
#             print ('Connected by @:@'  a.. 0 a.. 1
#         ______ K..
#             b..
#         ______ ?.e.. __ msg
#             print ('@'  ?
#
#
# __ _______ __ ______
#     ?

# # ch18/example3.py
#
# ______ so..
# ____ op..______ mul
# ____ fu..______ reduce
#
# # Main event loop
# ___ reactor host port
#     sock _ s__.s__
#     ?.b.. ? ?
#     ?.l.. 5
#     print _*Server up, running, and waiting for call on |? |?
#
#     ___
#         w__ T..
#             conn, cli_address _ ?.a..
#             p_r.. ?
#
#     f..
#         ?.c..
#
# ___ process_request ? ?
#     file _ conn.m_f..
#
#     print _*Received connection from |c..
#     mode _ 'sum'
#
#     ___
#         c__.s_a.. _'<welcome: starting in sum mode>\n')
#         w__ T..
#             line _ f__.r_l..
#             __ line:
#                 line _ ?.rs..
#                 __ line __ 'quit':
#                     c__.s_a.. _'connection closed\r\n')
#                     r_
#
#                 __ line __ 'sum':
#                     c__.s_a.. _'<switching to sum mode>\r\n')
#                     mode _ 'sum'
#                     c..
#                 __ line __ 'product':
#                     c__.s_a.. _'<switching to product mode>\r\n')
#                     mode _ 'product'
#                     c..
#
#                 print _$|c.. --> |l..')
#                 ___
#                     nums _ li.. m.. in. l__.s.. ','
#                 ______ V..
#                     c__.s_a..|
#                         _'ERROR. Enter only integers separated by commas\n')
#                     c..
#
#                 __ mode __ 'sum':
#                     c__.s_a.. _'Sum of input numbers: %a\r\n'
#                         % st.(su. n..
#                 ____
#                     c__.s_a.. _'Product of input numbers: %a\r\n'
#                         % st. re.. m.. n.. 1
#     f..
#         print _$|c.. quit')
#         f__.c..
#         c__.c..
#
# __ _______ __ _______
#     ? 'localhost' 8080

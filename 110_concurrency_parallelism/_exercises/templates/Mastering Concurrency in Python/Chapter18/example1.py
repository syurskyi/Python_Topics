# # ch18/example1.py
#
# ______ so..
#
# # Main event loop
# ___ reactor host port
#     sock _ s__.s__
#     ?.bind host port
#     ?.li..  5
#     print _*Server up, running, and waiting for call on |h.. |p..
#
#     ___
#         w__ T..
#             conn, cli_address _ s__.a..
#             process_request c.. c..
#
#     f..
#         s__.c..
#
# ___ process_request conn, cli_address
#     file _ ?.m_f_
#
#     print _*Received connection from |c_a..
#
#     ___
#         w__ T..
#             line _ f__.r_l..
#             __ ?
#                 l.. _ ?.rs..
#                 __ ? __ 'quit'
#                     c__.s_a.. _'connection closed\r\n')
#                     r_
#
#                 print _$|c_a.. --> |l..
#                 c__.s_a.. _'Echoed: @\r\n'  l..
#     f..
#         print _$|c_a..| quit')
#         f__.c..
#         c__.c..
#
# __ _______ __ _______
#     ? 'localhost' 8080

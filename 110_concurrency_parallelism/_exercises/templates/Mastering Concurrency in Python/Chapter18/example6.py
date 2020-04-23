# # ch18/example6.py
#
# ______ s__, select, types
# ____ co.. ______ na..
# ____ op.. ______ mul
# ____ fu.. ______ re..
#
# ###########################################################################
# # Reactor
#
# Session _ ? 'Session', |'address', 'file'
#
# sessions _            # { csocket : Session(address, file)}
# callback _            # { csocket : callback(client, line) }
# generators _         # { csocket : inline callback generator }
#
# # Main event loop
# ___ reactor host port
#     sock _ s__.s__
#     ?.b.. ? ?
#     ?.l.. 5
#     ?.s_b.. 0 # Make asynchronous
#
#     sessions|? _ N..
#     print _*Server up, running, and waiting for call on ? ?')
#
#     ___
#         w__ T..
#             # Serve existing clients only if they already have data ready
#             ready_to_read, _, _ _ s__.s..|s..    # list, [], 0.1)
#             ___ conn __ ready_to_read
#                 __ ? is ?:
#                     ?, c_a.. _ ?.a..
#                     c.. c.. cl..
#                     c..
#
#                 line _ s..|c...f__.r_l..
#                 __ ?
#                     c..|c.. c.. ?.rs..
#                 ____
#                     d..|c..
#     f..
#         ?.c..
#
# ___ connect c.. cl..
#     s..|c.. _ S.. cl.. c__.m_f..
#
#     gen _ p_r.. c..
#     g..|c.. _ ?
#     c..|c.. _ g__.s.. N.. # Start the generator
#
# ___ disconnect c..
#     gen _ g__.p.. c..
#     ?.c..
#     s..|c__ .f__.c..
#     c__.c..
#
#     de.. s.. |c..
#     de.. c.. |c..
#
# ?ty.?
# ___ readline c..
#     ___ inner c.. l..
#         gen _ g..|c..
#         ___
#             c..|c.. _ g__.s.. l.. # Continue the generator
#         ______ S..
#             d.. c..
#
#     line _ ? i..
#     r_ ?
#
# ###########################################################################
# # User's Business Logic
#
# ? ___ process_request conn
#     print_*Received connection from |s..|c.. .a..
#     mode _ 'sum'
#
#     ___
#         c__.s_a.. _'<welcome: starting in sum mode>\n')
#         w__ T..
#             line _ ? r_l.. c..
#             __ ? __ 'quit'
#                 c__.s_a.. _'connection closed\r\n')
#                 r_
#             __ ? __ 'sum'
#                 c__.s_a.. _'<switching to sum mode>\r\n')
#                 mode _ 'sum'
#                 c..
#             __ ? __ 'product'
#                 c__.s_a.. _'<switching to product mode>\r\n')
#                 mode _ 'product'
#                 c..
#
#             print_$|sessions|c__ .a..| --> |l..')
#             ___
#                 nums _ li.. m.. in. l__.sp.. ','
#             ______ V..
#                 c__.s_a..|
#                     _'ERROR. Enter only integers separated by commas\n')
#                 c..
#
#             __ mode __ 'sum'
#                 c__.s_a.. _'Sum of input integers: %a\r\n'
#                     % st. su. n..
#             ____
#                 c__.s_a.. _'Product of input integers: %a\r\n'
#                     % st. re.. m.. n.. 1
#     f..
#         print_@|s..|c.. .a..| quit
#
# __ _______ __ _______
#     ? 'localhost' 8080

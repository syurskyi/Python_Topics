# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 3
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ ?
# ____ tw__.i.. ______ r.. p.. e..
# ____ tw__.p.. ______ b..
#
# c_ PubProtocol b__.LR..
#     ___ -  factory
#         ? ?
#
#     ___ connectionMade
#         ?.c__.a..
#
#     ___ connectionLost reason
#         ?.c__.r..
#
#     ___ lineReceived line
#         ___ c __ ?.c..
#             source _ u"<{}> ".f.. t__.gH.. .e.. "ascii"
#             c.sL.. ? + l..
#
# c_ PubFactory p__.F..
#     ___ -
#         clients _ se.
#
#     ___ buildProtocol addr
#         r_ PP..
#
#
# __ _______ __ ______
#     parser _ ?.AP..(d.._'Socket Server Example with Epoll')
#     ?.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..
#     given_args _ ?.p_a..
#     port _ ?.p..
#     e__.sFS.. r.. "tcp:@" p.. .l.. P..
#     r__.r..
#

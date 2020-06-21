# # -*- coding: utf-8 -*-
#
# c_ IMath:
#     """Interface for proxy and real subject."""
#     ___ add x, y
#         r_ N...
#
#     ___ sub x, y
#         r_ N...
#
#     ___ mul x, y
#         r_ N...
#
#     ___ div x, y
#         r_ N...
#
# c_ Math I..
#     """Real subject."""
#     ___ add x, y
#         r_ x + y
#
#     ___ sub x, y
#         r_ x - y
#
#     ___ mul x, y
#         r_ x * y
#
#     ___ div x, y
#         r_ x / y
#
# c_ ProxyI..
#     """Proxy."""
#     ___ -
#         math = M..
#
#     ___ add x, y
#         r_ ?.a.. ? ?
#
#     ___ sub x, y
#         r_ ?.s.. ? ?
#
#     ___ mul x, y
#         r_ ?.m.. ?  ?
#
#     ___ div x, y
#         __ y __ 0
#             r_ fl.. ('inf') # Вернуть positive infinity
#         r_ ?.d.. ?
#
# p = P..
# x, y = 4, 2
# print '4 + 2 = ' + str(?.add(x, y))
# print '4 - 2 = ' + str(?.sub(x, y))
# print '4 * 2 = ' + str(?.mul(x, y))
# print '4 / 2 = ' + str(?.div(x, y))

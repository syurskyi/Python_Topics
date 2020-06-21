# """
# *What is this pattern about?
#
# The Chain of responsibility is an object oriented version of the
# `__ ... elif ... elif ... else ...` idiom, with the
# benefit that the condition–action blocks can be dynamically rearranged
# and reconfigured at runtime.
#
# This pattern aims to decouple the senders of a request from its
# receivers by allowing request to move through chained
# receivers until it is handled.
#
# Request receiver in simple form keeps a reference to a single successor.
# As a variation some receivers may be capable of sending requests out
# in several directions, forming a `tree of responsibility`.
#
# *TL;DR
# Allow a request to pass down a chain of receivers until it is handled.
# """
#
# ______ a..
#
#
# c_ Handler m..
#
#     ___ -  successor_N..
#         ?  ?
#
#     ___ handle request
#         """
#         Handle request and stop.
#         If can't - call next handler in chain.
#
#         As an alternative you might even in case of success
#         call the next handler.
#         """
#         res = c_r.. ?
#         __ no. ? an. s..
#             s___.h.. ?
#
#     ??.?
#     ___ check_range request
#         """Compare passed value to predefined interval"""
#
#
# c_ ConcreteHandler0 H..
#     """Each handler can be different.
#     Be simple and static...
#     """
#
#     ??
#     ___ check_range request
#         __ 0 <_ ? < 10
#             print("request @ handled in handler 0".f.. ?
#             r_ T..
#
#
# c_ ConcreteHandler1 H..
#     """... With it's own internal state"""
#
#     start, end = 10, 20
#
#     ___ check_range request
#         __ s.. <_ ? < e..
#             print("request @ handled in handler 1".f.. ?
#             r_ T..
#
#
# c_ ConcreteHandler2 H..
#     """... With helper methods."""
#
#     ___ check_range request
#         start, end _ g_i
#         __ s.. <_ ? < e..
#             print("request @ handled in handler 2".f.. ?
#             r_ T..
#
#     ??
#     ___ get_interval_from_db
#         r_ (20, 30)
#
#
# c_ FallbackHandler H..
#     ??
#     ___ check_range request
#         print("end of chain, no handler for @".f.. ?
#         r_ F..
#
#
# ___ main
#
#     h0 = C_0
#     h1 = C_1
#     h2 = C_r2 F..
#     h0.successor = h1
#     h1.successor = h2
#
#     requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
#     ___ request __ ?
#         h0.h.. ?
#
#     # request 2 handled in handler 0
#     # request 5 handled in handler 0
#     # request 14 handled in handler 1
#     # request 22 handled in handler 2
#     # request 18 handled in handler 1
#     # request 3 handled in handler 0
#     # end of chain, no handler for 35
#     # request 27 handled in handler 2
#     # request 20 handled in handler 2
#
#
#
# __ _______ __ ______
#     main()

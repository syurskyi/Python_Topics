# """Proxy pattern
#
# Proxy is a structural design pattern. A proxy is a surrogate object which can
# communicate with the real object (aka implementation). Whenever a method in the
# surrogate is called, the surrogate simply calls the corresponding method in
# the implementation. The real object is encapsulated in the surrogate object when
# the latter is instantiated. It's NOT mandatory that the real object class and
# the surrogate object class share the same common interface.
# """
# ____ a.. ______ A.. a..
#
#
# c_ CommonInterface A..
#     """Common interface for Implementation (real obj) and Proxy (surrogate)."""
#
#     ??
#     ___ load
#         p..
#
#     ??
#     ___ do_stuff
#         p..
#
#
# c_ Implementation C..
#
#     ___ - filename
#         ?  ?
#
#     ___ load
#         print("load @".f.. f...
#
#     ___ do_stuff
#         print("do stuff on @".f.. f..
#
#
# c_ Proxy C..
#
#     ___ - implementation
#         __?  ?  # the real object
#         __cached _ F..
#
#     ___ load
#         __i__.l..
#         __cached _ T..
#
#     ___ do_stuff
#         __ no. __c..
#             l..
#         __i___.d..
#
#
# ___ main
#     p1 = P.. I.. "RealObject1"
#     p2 = P.. I.. "RealObject2"
#
#     p1.do_stuff()  # loading necessary
#     p1.do_stuff()  # loading unnecessary (use cached object)
#     p2.do_stuff()  # loading necessary
#     p2.do_stuff()  # loading unnecessary (use cached object)
#     p1.do_stuff()  # loading unnecessary (use cached object)
#
#
# __ _______ __ ______
#     ?

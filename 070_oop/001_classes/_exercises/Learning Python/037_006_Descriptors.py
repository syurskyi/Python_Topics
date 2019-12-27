# #
# # class Descriptor:
# #     "docstring goes here"
# #     def __get__(self, instance, owner): ...        # Return attr value
# #     def __set__(self, instance, value): ...        # Return nothing (None)
# #     def __delete__(self, instance): ...            # Return nothing (None)
# #
# #
#
#
# c_ Descriptor o..
#     ___ __get__ ____ instance owner
#         print(____, instance, owner, sep='\n')
#
# c_ Subject
#     attr = D...             # Decriptor instance is class attr
#
# X = S...
#
# ?.attr
#
# S___.attr
#
# c_ D
#     ___ __get__ 0a.. print('get')
#
# c_ C
#     a = D()
#
# X = C()
# X.a                                 # Runs inherited descriptor __get__
#
# C.a
#
# X.a = 99                            # Stored on X, hiding C.a
# X.a
#
# li.. X. -d.k..
#
# Y = C()
# ?.a                                 # Y still inherits descriptor
#
# C.a
#
# c_ D
#     ___ __get__ 0a.. print('get')
#     ___ __set__ 0a.. r... A.... cannot set
#
# c_ C:
#     a = D()
#
# X = C()
# X.a                                 # Routed to C.a.__get__
# # get
# # X.a = 99           # ERROR                 # Routed to C.a.__set__
# # # AttributeError: cannot set

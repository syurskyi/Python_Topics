# """Decorator pattern
#
# Decorator is a structural design pattern. It is used to extend (decorate) the
# functionality of a certain object at run-time, independently of other instances
# of the same class.
# The decorator pattern is an alternative to subclassing. Subclassing adds
# behavior at compile time, and the change affects all instances of the original
# class; decorating can provide new behavior at run-time for selective objects.
# """
#
#
# c_ Component o..
#
#     # method we want to decorate
#
#     ___ whoami
#         print("I am @".f.. i. ?
#
#     # method we don't want to decorate
#
#     ___ another_method
#         print("I am just another method of @".f.. -c. -n
#
#
# c_ ComponentDecorator o..
#
#     ___ - decoratee
#         _?  ?  # reference of the original object
#
#     ___ whoami
#         print("start of decorated method")
#         _d___.w..
#         print("end of decorated method")
#
#     # forward all "Component" methods we don't want to decorate to the
#     # "Component" pointer
#
#     ___ -g name
#         r_ g.. _d... ?
#
#
# ___ main
#     a = C...  # original object
#     b = CD__ ?  # decorate the original object at run-time
#     print("Original object")
#     a.w...
#     a.a..
#     print("\nDecorated object")
#     b.w..
#     b.a..
#
#
# __ _______ __ ______
#     ?

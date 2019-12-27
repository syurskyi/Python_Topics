# f___ lister _______ ListInstance
# c_ Spam L..                   # Inherit a __str__ method
#     ___ -  _____
#         ____.data1 = 'food'
#
# x = ?
# print(x)                                     # print() and str() run __str__
# # <Instance of Spam, address 40240880:
# #         name data1=food
#
#
# str(x)
# # '<Instance of Spam, address 40240880:\n\tname data1=food\n>'
# x                                            # The __repr__ still is a default
# # <__main__.Spam object at 0x026606F0>
#
#
#
# ### File: testmixin.py
#
# from lister import *                  # Get lister tool classes
#
# c_ Super
#     ___ - ____               # Superclass __init__
#         ____.data1 _ 'spam'           # Create instance attrs
#     ___ ham ____
#         p__
#
# c_ Sub S.. L..       # Mix in ham and a __str__
#     ___ - ____               # listers have access to self
#         S___. - ____
#         ____.data2 _ 'eggs'           # More instance attrs
#         ____.data3 _ 42
#     ___ spam ____                   # Define another method here
#         p..
#
# __ ______ __ ______
#     X = S..
#     print(X)                          # Run mixed-in __str__
#
#
# _______ l...
# c_ C li__.L... p..
#
# x = C()
# x.a = 1; x.b = 2; x.c = 3
# print(x)
# # <Instance of C, address 40961776:
# #         name a=1
# #         name b=2
# #         name c=3
#
#
#

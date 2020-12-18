# c_ C1
#     ___ meth1 ____ ____.X = 88         # I assume X is mine
#
#     ___ meth2 ____ print(____.X
#
#
# c_ C2
#     ___ metha ____ ____.X = 99         # Me too
#
#     ___ methb ____ print(____.X)
#
#
# c_ C3(C1, C2):
#     p..
# I = C3()                                 # Only 1 X in I!
#
#
#
# ### file: private.py
#
#
# c_ C1
#     ___ meth1 ____ ____.__X = 88       # Now X is mine
#
#     ___ meth2 ____ print(____.__X)     # Becomes _C1__X in I
#
#
# c_ C2
#     ___ metha ____ ____.__X = 99       # Me too
#
#     ___ methb ____ print(____.__X)     # Becomes _C2__X in I
#
#
# c_ C3(C1, C2): pass
# I = C3()                                 # Two X names in I
#
# ?._1 ?.m_a
# print ?. -d
# ?._2 ?.m_b
#
#
# c_ Super
#     ___ method ____                  # A real application method
#         p___
#
#
# c_ Tool
#     ___ __method ____                 # Becomes _Tool__method
#         p..
#
#     ___ other ____ ____.?       # Use my internal method
#
#
# c_ Sub1 T.. S..
#     p..
#
#     ___ actions ____ ____.me...      # Runs Super.method as expected
#
#
# c_ Sub2 T..
#     ___ - ____ ____.method = 99   # Doesn't break Tool.__method
#

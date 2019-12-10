# ### File: classtree.py
#
# """
# Climb inheritance trees using namespace links,
# displaying higher superclasses with indentation
# """
#
# ___ classtree ___ indent
#     print('.' * i... + ___. -n    # Print class name here
#     ___ supercls i_ ___. -b        # Recur to all superclasses
#         c.. s.., i..+3     # May visit super > once
#
# ___ instancetree inst
#     print('Tree of *_' / i..            # Show instance
#     cl... i__. -c 3         # Climb to its class
#
# ___ selftest
#     c_ A:      pass
#     c_ B(A):   pass
#     c_ C(A):   pass
#     c_ D(B,C): pass
#     c_ E:      pass
#     c_ F(D,E): pass
#     i... B
#     i... F
#
# __ _______ __ _______
#     s..
#
#
#
#
# c_ Emp p___
#
# c_ Person Emp p..
# bob = ?
#
# import classtree
# ?.i... ?
#
#

# """
# *What is this pattern about?
# This pattern aims to minimise the number of objects that are needed by
# a program at run-time. A Flyweight is an object shared by multiple
# contexts, and is indistinguishable from an object that is not shared.
#
# The state of a Flyweight should not be affected by it's context, this
# is known as its intrinsic state. The decoupling of the objects state
# from the object's context, allows the Flyweight to be shared.
#
# *What does this example do?
# The example below sets-up an 'object pool' which stores initialised
# objects. When a 'Card' is created it first checks to see if it already
# exists instead of creating a new one. This aims to reduce the number of
# objects initialised by the program.
#
# *References:
# http://codesnipers.com/?q_python-flyweights
# https://python-patterns.guide/gang-of-four/flyweight/
#
# *Examples in Python ecosystem:
# https://docs.python.org/3/library/sys.html#sys.intern
#
# *TL;DR
# Minimizes memory usage by sharing data with other similar objects.
# """
#
# ______ w...
#
#
# c_ Card
#     """The Flyweight"""
#
#     # Could be a simple dict.
#     # With WeakValueDictionary garbage collection can reclaim the object
#     # when there are no other references to it.
#     _pool _ w___.WVD..
#
#     ___ -n ___ value suit
#         # If the object exists in the pool - just return it
#         obj _ ___._p__.ge. ? + ?
#         # otherwise - create new one (and add it to the pool)
#         __ ? __ N..
#             ? _ obj____. -n C..
#             ___._p...|? + ? _ ?
#             # This row does the part we usually see in `__init__`
#             ?.v.. ?.s.. _ ?  ?
#         r_ ?
#
#     # If you uncomment `__init__` and comment-out `__new__` -
#     #   Card becomes normal (non-flyweight).
#     # def __init__(self, value, suit):
#     #     self.value, self.suit _ value, suit
#
#     ___ -r
#         r_ "<Card: @@>".f... v..  s..
#
#
# ___ main
#     c1 _ C..('9', 'h')
#     c2 _ C..('9', 'h')
#     c1, c2
#     # (<Card: 9h>, <Card: 9h>)
#     c1 == c2
#     # True
#     c1 is c2
#     # True
#
#     c1.new_attr _ 'temp'
#     c3 _ Card('9', 'h')
#     hasattr(c3, 'new_attr')
#     # True
#
#     Card._pool.clear()
#     c4 _ Card('9', 'h')
#     hasattr(c4, 'new_attr')
#     # False
#
#
#
# __ _______ __ ______
#     import doctest
#     doctest.testmod()

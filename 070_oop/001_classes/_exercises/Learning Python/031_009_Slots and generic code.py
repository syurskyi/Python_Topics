# c_ C
#     __slots__ _ 'a', 'b'           # __slots__ means no __dict__ by default
#
# X = C()
# X.a = 1
# X.a
#
# X. -d
# # AttributeError: 'C' object has no attribute '__dict__'
# g.. X 'a'
#
# s.. X, 'b', 2)                   # But getattr() and setattr() still work
# X.b
#
# 'a' i_ di. X                        # And dir() finds slot attributes too
#
# 'b' in di. X
#
# c_ D
#     -s _ 'a' 'b'
#     ___ - ____ ____.d _ 4   # Cannot add new names if no __dict__
#
# X = D()
# # AttributeError: 'D' object has no attribute 'd'
#
#
#
# c_ D
#     -s _ 'a', 'b', '__dict__'    # List __dict__ to include one too
#     c = 3                                 # Class attrs work normally
#     ___ - ____ ____.d _ 4        # d put in __dict__, a in __slots__
#
# X = ?
# ?.d
#
# ?. -d                  # Some objects have both __dict__ and __slots__
# ?. -c
# ?.c
#
# X.a                          # All instance attrs undefined until assigned
# # AttributeError: a
# X.a = 1
# g.. X 'a',) g.. X, 'c'), g... (X, 'd'
#
# ___ attr i_ li.. X. -d + X. -s
#     print a.. '=>', g... X a..
#
# # d = > 4
# # a = > 1
# # b = > 2
# # __dict__ = > {'d': 4}
#
# ___ attr i_ li.. ge.. X '-d'  |  + ge.. X '-s' |
#     print a.. '=>', ge.. X a..
#
# # d = > 4
# # a = > 1
# # b = > 2
# # __dict__ = > {'d': 4}
#

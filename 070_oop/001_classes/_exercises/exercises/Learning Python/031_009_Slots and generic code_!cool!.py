# c_ C
#     -s _ 'a', 'b'           # __slots__ means no __dict__ by default
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
# print X.b
#
# print 'a' i_ di. X                        # And dir() finds slot attributes too
#
# print 'b' in di. X
#
# c_ D
#     -s _ 'a' 'b'
#     ___ - ____ ____.d _ 4   # Cannot add new names if no __dict__
#
# X = D()
# # AttributeError: 'D' object has no attribute 'd'
#
#
# c_ D
#     -s _ 'a', 'b', '__dict__'    # List __dict__ to include one too
#     c = 3                                 # Class attrs work normally
#     ___ - ____ ____.d _ 4        # d put in __dict__, a in __slots__
#
# X = ?
# print ?.d
#
# print ?. -d                  # Some objects have both __dict__ and __slots__
# print ?. -c
# print ?.c
#
# X.a                          # All instance attrs undefined until assigned
# # AttributeError: a

# X.a = 1
# X.b = 1

# print ?. -d                # Some objects have both __dict__ and __slots__
#                            # getattr() can fetch either type of attr
# print ?. -s
# print g.. X 'a' g.. X, 'c' g... X 'd'
#
# ___ attr __ li.. X. -d + X. -s
#     print ? '=>', g... X ?
#
# # d = > 4
# # a = > 1
# # b = > 2
# # __dict__ = > {'d': 4}
#
# ___ attr __ li.. ge.. X '-d'||||  + ge.. X '-s' |||
#     print ? '=>', ge.. X ?
#
# # d = > 4
# # a = > 1
# # b = > 2
# # __dict__ = > {'d': 4}
#

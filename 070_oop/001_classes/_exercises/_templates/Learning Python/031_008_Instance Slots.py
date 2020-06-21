# c_ limiter o..
#     -s = 'age', 'name', 'job'
#
# x = ?
# ?.a..                                          # Must assign before use
# # AttributeError: age
#
# ?.a.. = 40
# ?.a..
#
# x.a.. = 1000                                    # Illegal: not in __slots__
# # AttributeError: 'limiter' object has no attribute 'ape'

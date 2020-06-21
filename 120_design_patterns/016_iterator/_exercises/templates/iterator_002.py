# # from a sequence
# x = [42, "test", -12.34]
# it = iter(x)
# ___
#     w___ T..
#         x _ ne.. i.  # in Python 2, you would use it.next()
#         print x
# _____ S..
#     p...
#
#
# # a generator
# ___ foo n
#     ___ i __ ra.. ?
#         y... ?
#
# it = foo(5)
# ___
#     w___ T...
#         x = ne.. i.  # in Python 2, you would use it.next()
#         print ?
# _____ S..
#     p...

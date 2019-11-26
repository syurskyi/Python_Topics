# f.. c... _______ d..d.., C..
#
# # Using Repeated Iteration
#
# c1 _ C.. 'abba'
# c1
# # Counter({'a': 2, 'b': 2})
#
# ___ c i_ c1
#     print(c)
#
# # a
# # b
#
# # However, we can have an iteration that repeats the counter keys as many times as the indicated frequency:
#
# ___ c i_ c1.el..
#     print(c)
#
# # a
# # a
# # b
# # b
#
# # What's interesting about this functionality is that we can turn this around and use it as a way
# # to create an iterable that has repeating elements.
# # Suppose we want to to iterate through a list of (integer) numbers that are each repeated as many times as the number
# # itself.
# # ___ example 1 should repeat once, 2 should repeat twice, and so on.
# # This is actually not that easy to do!
# # Here's one possible way to do it:
#
# l _ ||
# ___ i i_ ra.. 1 11
#     ___ _ i_ ra.. i
#         l.aP.. i
# print(l)
#
# # [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9,
# # 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
#
# # But we could use a Counter object as well:
#
# c1 _ C..
# ___ i i_ ra.. 1 11
#     c1 i _ i
# c1
# # Counter({1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10})
#
# print c1.el..
#
# # So you'll notice that we have a chain object here. That's one big advantage to using the Counter object -
# # the repeated iterable does not actually exist as list like our previous implementation - this is a lazy iterable,
# # so this is far more memory efficient.
# # And we can iterate through that chain quite easily:
#
# ___ i i_ c1.el..
#     print i e.._', '
#
# # 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9,
# # 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
#
# # Just ___ fun, how could we reproduce this functionality using a plain dictionary?
#
#
# c_ RepeatIterable
#     ___ __init__(____ 00k..):
#         ____.d _ k..
#     ___ __setitem__ ____  key value
#         ____.d ke. _ value
#     ___ __getitem__ ____ ke.
#         ____.d ke. _ ____.d.ge. ke. 0
#         r_ ____.d ke.
#
# r _ RepeatIterable x_10 y_20
# print r.d
# # {'x': 10, 'y': 20}
#
# r['a'] _ 100
# print(r['a'])
# # 100
#
# r['b']
# # 0
#
# print(r.d)
# # {'x': 10, 'y': 20, 'a': 100, 'b': 0}
#
# print(r.d)
# # {'x': 10, 'y': 20, 'a': 100, 'b': 0}
#
# # Now we have to implement that elements iterator:
#
# c_ RepeatIterable:
#     ___ __init__ ____ 00k..
#         ____.d _ k..
#
#     ___ __setitem__ ____ ke. val..
#         ____.d ke. _ va..
#
#     ___ __getitem__ ____ ke.
#         ____.d ke. _ ____.d.ge. ke. 0
#         r___ ____.d ke.
#
#     ___ elements ____
#         ___ k, frequency i_ ____.d.it..
#             ___ i i_ ra.. fr..
#                 y____ k
#
# r _ RepeatIterable a_2 b_3 c_1
#
# ___ e i_ r.el..
#     print e e.._', '
# # a, a, b, b, b, c,
#

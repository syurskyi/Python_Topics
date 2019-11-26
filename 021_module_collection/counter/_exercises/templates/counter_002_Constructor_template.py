# f.. c... _______ d..d.., C..
#
# # It is so common to create a frequency distribution of elements in an iterable, that this is supported automatically:
#
# c1 = C.. 'able was I ere I saw elba'
# print(c1)
#
# # Counter({'a': 4,
# #          'b': 2,
# #          'l': 2,
# #          'e': 4,
# #          ' ': 6,
# #          'w': 2,
# #          's': 2,
# #          'I': 2,
# #          'r': 1})
#
# # Of course this works for iterables in general, not just strings:
#
# _______ ran..
#
# ra__.se.. 0
#
# my_list _  ra__.r__i__ 0 10 ___ _ i_ ra__ 1_000
# c2 _ C.. m._l..
# c2
#
# # Counter({6: 95,
# #          0: 97,
# #          4: 91,
# #          8: 76,
# #          7: 94,
# #          5: 89,
# #          9: 85,
# #          3: 80,
# #          2: 88,
# #          1: 107,
# #          10: 98})
#
# # We can also initialize a Counter object by passing in keyword arguments, or even a dictionary:
#
# c2 _ C.. a_1 b_10
# print(c2)
#
# C.. 'a' 1 'b' 10
# c3 = C.. 'a' 1 'b' 10
# print(c3)
#
# # Counter({'a': 1, 'b': 10})
#
# # Technically we can store values other than integers in a Counter object - it's possible but of limited use since
# # the default is still 0 irrespective of what other values are contained in the object.

# f.. c... _______ d..d.., C..
#
# # Updating from another Iterable or Counter
# # Lastly let's see how we can update a Counter object using another Counter object.
# # When both objects have the same key, we have a choice - do we add the count of one to the count of the other,
# # or do we subtract them?
# # We can do either, by using the update (additive) or subtract methods.
#
# c1 _ C.. a_1 b_2 c_3
# c2 _ C.. b_1 c_2 d_3
# c1.up.. c2
# print(c1)
# # Counter({'c': 5, 'b': 3, 'd': 3, 'a': 1})
#
# # On the other hand we can subtract instead of add counters:
#
# c1 _ C.. a_1 b_2 c_3
# c2 _ C.. b_1 c_2 d_3
# c1.su.. c2
# print(c1)
# # Counter({'a': 1, 'b': 1, 'c': 1, 'd': -3})
#
# # Notice the key d - since Counters default missing keys to 0, when d: 3 in c2 was subtracted from c1,
# # the counter for d was defaulted to 0.
# # Just as the constructor for a Counter can take different arguments, so too can the update and subtract methods.
#
# c1 _ C.. 'aabbccddee'
# print(c1)
# c1.up.. 'abcdef'
# print(c1)
# # Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2})
# # Counter({'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3, 'f': 1})

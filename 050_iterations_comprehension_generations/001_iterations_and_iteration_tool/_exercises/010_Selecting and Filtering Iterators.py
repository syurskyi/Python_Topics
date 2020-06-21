# # Slicing Iterables
# # We know that sequence types can be sliced:
# # Equivalently we can use the slice object:
#
# l _  1 2 3 4 5
# l 0;2
#
# s _ sl__ 0 2
# l[s]
#
# # Selecting and Filtering Iterators
# # Remember that the filter function can work with any iterable, including of course iterators and generators.
# # Now let's say we only want to use cubes that are odd.
# # We need a function that will return a True if the number is odd, False otherwise.
# # (This is technically called a predicate by the way -
# # any function that given an input returns True or False is called a predicate)
# # Let's make sure the function works as expected:
# # Now we can use that function (or we could have just used a lambda as well) with the filter function.
# # Note that the filter function is also lazy.
#
# ___ gen_cubes n
#     ___ i i_ ra__ n
#         print _*yielding i|*
#         y___ i**3
#
# ___ is_odd x
#     r_ x % 2 __ 1
#
# is_odd(4), is_odd(81)
#
# filtered _ fi___ i._o.. g.._c. 10
#
# li__ f...
#
#
# # Selecting and Filtering Iterators
# # e could use the filterfalse function in the itertools module that does the same work as filter but retains values w
# # here the predicate is False (instead of True as the filter function does).
#
# f_ ite___ ______ fi..fa..
#
# ___ gen_cubes n
#     ___ i i_ ra__ n
#         print _*yielding i|
#         y___ i**3
#
# ___ is_odd x
#     r_ x % 2 __ 1
#
# evens _ fi..fa.. i._o.. g.._c.. 10
#
# # No print output --> lazy evaluation
#
# li__evens

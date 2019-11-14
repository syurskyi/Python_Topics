# ######################################################################################################################
# The zip built-in function will take one or more iterables,
# and generate an iterable of tuples where each tuple contains one element from each iterable:

# l1 = 1, 2, 3
# l2 = 'a', 'b', 'c'
# l_ z_ l1 l2
#
# l1 = 1, 2, 3
# l2 = [10, 20, 30]
# l3 = ('a', 'b', 'c')
# l_(z_ l1 l2 l3
#
# l1 = [1, 2, 3]
# l2 = (10, 20, 30)
# l3 = 'abc'
# l_(z_ l1 l2 l3
#
# l1 = range(100)
# l2 = 'python'
# l_(z l1 l2
#
# print()
# ######################################################################################################################
# Using the zip function we can now add our two lists element by element as follows:

# l1 = [1, 2, 3, 4, 5]
# l2 = [10, 20, 30, 40, 50]
# result _ |i + j ___ i_j __ z_ l1l2_ |
# print result
#
# print()
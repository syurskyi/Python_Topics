# # Chaining and Teeing Iterators
# # suppose we have some generators producing squares:
# # And we want to essentially iterate through all the values as if they were a single iterator.
# # In fact, we could even create our own generator function to do this:
# # a much simpler way is to use chain in the itertools module:
# # As you can see, it simply took our list and handed it back directly - there was nothing else to chain with:
# # Instead, we could use unpacking:
#
# l1 _ i**2 ___ i i_ ra__ 4
# l2 _ i**2 ___ i i_ ra__ 4 8
# l3 _ i**2 ___ i i_ ra__ 8 12
#
# ___ gen i_ l1 l2 l3
#     ___ item i_ gen:
#         print item
#
# ___ chain_iterables 0iterables
#     ___ iterable i_ iterables
#         y___ fr__ iterable
#
# l1 _ i**2 ___ i i_ ra__ 4
# l2 _ i**2 ___ i i_ ra__ 4 8
# l3 _ i**2 ___ i i_ ra__ 8 12
#
# ___ item i_ ch.._i.. l1 l2 l3
#     print i..
#
# f___ it__ _______ ch__
#
# l1 _ i**2 ___ i i_ ra__ 4
# l2 _ i**2 ___ i i_ ra__ 4 8
# l3 _ i**2 ___ i i_ ra__ 8 12
#
# ___ item i_ ch.. l1 l2 l3
#     print(item)
#
# l1 _ i**2 ___ i i_ ra__ 4
# l2 _ i**2 ___ i i_ ra__ 4 8
# l3 _ i**2 ___ i i_ ra__ 8 12
#
# lists _ l1 l2 l3
# ___ item i_ ch.. l....
#     ___ i i_ it..
#         print i
#
# l1 _ i**2 ___ i i_ ra__ 4
# l2 _ i**2 ___ i i_ ra__ 4 8
# l3 _ i**2 ___ i i_ ra__ 8 12
#
# lists _ l1 l2 l3
# ___ item i_ ch.. 0l..
#     print i..
#
# # Chaining and Teeing Iterators
# # But, unpacking is not lazy!! Here's a simple example that shows this,
# # and why we have to be careful using unpacking if we want to preserve lazy evaluation:
# # Instead we can use an alternate "constructor" for chain, that takes a single iterable (of iterables)
# # and lazily iterates through the outer iterable as well:
# # Note also, that we can easily reproduce the same behavior of either chain quite easily:
# # And we can use those just as we saw before with chain and chain.from_iterable:
#
# l1 _ i**2 ___ i i_ ra__ 4
# l2 _ i**2 ___ i i_ ra__ 4 8
# l3 _ i**2 ___ i i_ ra__ 8 12
#
# ___ squares
#     print 'yielding 1st item'
#     y___ i**2 ___ i i_ ra__4
#     print 'yielding 2nd item'
#     y___ i**2 ___ i i_ ra__ 4 8
#     print'yielding 3rd item'
#     y___ i**2 ___ i i_ ra__ 8 12
#
# ___ read_values 0a..
#     print 'finised reading args'
#
# r.._v... 0sq..
#
# c _ ch__.f.._iter.. s..
#
# ___ item i_ c
#     print it..
#
# ___ chain_ 0a..
#     ___ item i_ ar..
#         y___ fr.. it..
#
# ___ chain_iter it...
#     ___ item i_ it...
#         y___ f.. ite.
#
# c _ chain_(*squares(
#
# c _ chain_iter(squares(
# ___ item i_ c
#     print ite.

#
# # Zipping
# # t zips up two iterables and yields tuples containing elements from all iterables in "parallel".
# # It is also lazy, and it will stop once the first iterable is exhausted.
#
# l1 _ 1 2 3 4 5
# l2 _ 1 2 3 4
# l3 _  1 2 3
#
# li__ z.. l1 l2 l3
#
# # Zipping
# #
# # As you can see, the shortest iterable we provided to the zip function had a length of 3
# # (so it reached the end of iteration first), and our output therefore only had 3 tuples in it.
# #
# # Of course, this works with iterators and generators too:
#
# ___ integers n
#     ___ i i_ ra__ n
#         y___ i
#
#
# ___ squares n
#     ___ i i_ ra__ n
#         y___ i ** 2
#
#
# ___ cubes n
#     ___ i i_ ra__ n
#         y___ i ** 3
#
#
# iter1 _ in.. 6
# iter2 _ sq.. 5
# iter3 _ cu.. 4
#
# li__ z.. i..1 i..2 i..3
#
# # Zipping
# #
# # Sometimes we want to zip up iterables but completely iterate all the iterables, and not stop at the shortest
# # Simple, we just need to provide a default "filler" value.
# # And that's how the zip_longest function from itertools works:
# # As you can see, we can only specify a single default value, this means that default will be used for any provided
# # iterable once it has been fully iterated.
# # As expected, zip_longest yields its values - it is lazy.
#
# f__ it____ _______ z.._lo..
#
# help z._l..
#
# l1 _  1 2 3 4 5
# l2 _ 1 2 3 4
# l3 _ 1 2 3
#
# li__ z.._lo.. l1 l2 l3 fillvalue_'N/A'
#
# # Zipping
# # zip_longest
# #
# # Of course, since this zips over the longest iterable, beware of using an infinite iterable!
# #
# # You don't have to worry about this with the normal zip function as long as at least one of the iterables is finite:
#
# ___ squares
#     i _ 0
#     w___ T...
#         y___ i ** 2
#         i +_ 1
#
# ___ cubes
#     i _ 0
#     w___ T...
#         y___ i ** 3
#         i +_ 1
#
# iter1 _ s...
# iter2 _ c...
# li__ z.. ra__ 10 i..1 i..2
#

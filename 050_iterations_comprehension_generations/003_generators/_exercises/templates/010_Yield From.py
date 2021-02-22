# # Yield From
# # Suppose we want an iterator to iterate over all the values of the matrix, element by element.
# # All we have done here is create a generator  (iterator)  that can be used to iterate of the elements
# # of a nested iterator.
#
# # row, item
# ___ matrix_iterator n
#     ___ ? __ matrix ?
#         ___ ? __ row
#             y____ ?
#
# # i
# ___ ? __ ? 3
#     print ?
#
# # Yield From
# # But we can avoid using that nested ___ loop by using a special form of yield: yield from
#
# # # row,
# ___ matrix_iterator n
#     ___ ? __ matrix n
#         y____ f... ?
#
# # i
# ___ ? __ ? 3
#     print ?
#
# # Yield From
# #
# # we need to read car brands from multiple files to get it as a single collection.
#
# # f_name
# ___ brands 0files
#     ___ ? __ ?
#         w... o.. ?  __ f
#             y____ f... ?
#
# files _ 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'
#
# ___ brand __ brands 0f..
#     print b... e.._', '
#
# # Yield From
# #
# # we are going to create generators that can read each line of the file, and yield a clean result,
# # and we'll yield from that generator:
# # As you can see, this generator function will clean each line of the file before yielding it.
# # Let's try it with a single file and make sure it works:
# # So now, we can proceed with our overarching generator function as before, except we'll yield from our generators,
# # instead of directly from the file iterator:
# # I want to point out that i_ this particular instance, we are using yield from as a simple replacement ___ a ___ loop
#
# # line
# ___ gen_clean_read file
#     w... o.. ?  __ f
#         ___ ? __ ?
#             y____ ?.st.. '\n'
#
# # line
# f1 _ ? *car-brands-1.txt
# ___ ? __ ?
#     print ? e.._', '
#
# files _ 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'
#
# # file
# ___ brands 0f...
#     ___ ? __ f...
#         y____ f... ? f..
#
# ___ brand __ br.. 0f..
#     print b.. e.._', '

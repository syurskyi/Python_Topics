# # Yield From
# # Suppose we want an iterator to iterate over all the values of the matrix, element by element.
# # All we have done here is create a generator  (iterator)  that can be used to iterate of the elements
# # of a nested iterator.
#
# ___ matrix_iterator n
#     ___ row i_ matrix n
#         ___ item i_ row
#             y____ i...
#
# ___ i i_ matrix_iterator 3
#     print i
#
# # Yield From
# # But we can avoid using that nested ___ loop by using a special form of yield: yield from
#
# ___ matrix_iterator n
#     ___ row i_ matrix n
#         y____ f... row
#
# ___ i i_ matrix_iterator 3
#     print i
#
# # Yield From
# #
# # we need to read car brands from multiple files to get it as a single collection.
#
# ___ brands 0files
#     ___ f_name i_ files
#         w... open f_name  a. f
#             y____ f... f
#
# files _ 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'
#
# ___ brand i_ brands 0f..
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
# ___ gen_clean_read file
#     w... open file  a. f
#         ___ line i_ f
#             y____ li__.st.. '\n'
#
# f1 _ gen_clean_read 'car-brands-1.txt'
# ___ line i_ f1:
#     print li.. e.._', '
#
# files _ 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'
#
# ___ brands 0f...
#     ___ file i_ f...
#         y____ f... gen_clean_read f..
#
# ___ brand i_ br.. 0f..
#     print b.. e.._', '

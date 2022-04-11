# _______ n.... __ np
# _______ p.... __ pd
#
#
# ___ return_at_index ser ?.S..  idx i.. __ o..
#     """Return the Object at the given index of the Series
#     If you want to be extra careful catch and raise an error if
#        the index does not exist.
#     """
#     r.. ? ?
#
#
# ___ get_slice ser ?.S.., start i.. end i.. __ ?.c__.s__.S.
#     """Return the slice of the given Series in the range between
#     start and end.
#     """
#     r.. ?,i.. ?|?
#
#
# ___ get_slice_inclusive ser ?.S..
#                         start i.. end i.. __ ?.c__.s__.S.
#     """Return the slice of the given Series in the range between
#     start and end inclusive.
#     """
#     r.. ?,i.. ?|? + 1
#
#
# ___ return_head ser ?.S.. num i.. __ ?.c__.s__.S.
#     """Return the first num elements of the given Series.
#     """
#     r.. ?.h.. ?
#
#
# ___ return_tail ser ?.S.. num i.. __ ?.c__.s__.S.
#     """Return the last num elements of the given Series.
#     """
#     r.. ?.t.. ?
#
#
# ___ get_index ser ?.S.. __ >?.c__.i__.b__.I..
#     """Return all indexes of the given Series.
#     """
#     r.. ?.i
# ___ get_values ser ?.S.. __ ?.n
#     """Return all the values of the given Series.
#     """
#     r.. ?.a.v
#
#
# ___ get_every_second_indexes ser ?.S..
#                              even_index_T.. __ ?.c__.s__.S.
#     """Return all rows where the index is either even or odd.
#     If even_index is True return every index where idx % 2 == 0
#     If even_index is False return every index where idx % 2 != 0
#     Assume default indexing i.e. 0 -> n
#     """
#     __ even_index __ F..
#         r.. ?.w i 2 !_ 0 .d   ____
#         r.. ?.w i 2 __ 0 .d
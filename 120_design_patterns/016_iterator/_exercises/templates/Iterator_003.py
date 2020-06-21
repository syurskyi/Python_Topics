# #==============================================================================
# c_ ReverseIterator o..
#     """
#     Iterates the object given to it in reverse so it shows the difference.
#     """
#
#     ___ - iterable_object
#         list _ ?
#         # start at the end of the iterable_object
#         index _ le. ?
#
#     ___ -i
#         # r_ an iterator
#         r_ ?
#
#     ___ next
#         """ Return the list backwards so it's noticeably different."""
#         __ in.. __ 0
#             # the list is over, raise a stop index exception
#             r_ S..
#         in.. _ in.. - 1
#         r_ li..|in..
#
# #==============================================================================
# c_ Days o..
#
#     ___ -
#         days _ |
#         "Monday"
#         "Tuesday",
#         "Wednesday"
#         "Thursday"
#         "Friday"
#         "Saturday"
#         "Sunday"
#         |
#
#     ___ reverse_iter
#         r_ R.. ?
#
# #==============================================================================
# __ _______ __ ______
#     days _ D..
#     ___ day __ ?.r_i..
#         print ?

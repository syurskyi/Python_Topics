# _____ ___
#
# c_ TextJustifyOpt
#     ___ -  txt, line_length
#         ?  ?
#         ?  ?
#         word_length _ |||| * le. ?
#         ___ i __ ra.. le. t..
#             w__|? _ |0 * le. t..
#             w__|?|? _ le. t..|?
#             ___ j __ ra.. ? + 1, le. t..
#                 w__|?|? _ w__|?|? - 1| + 1 + le. t..|?
#         ___ arr __ w__
#             print ?
#
#     ___ ugly_score txt_length
#         __ ? <_ l..
#             r_ l.. - t.. ** 2
#         ____
#             r_ ___.ma..
#
#     ___ format_txt
#         scores _ |0 * (le. t.. + 1
#         ptrs _ [0] * le. t..
#
#         ___ i __ ra.. le. t.. - 1, -1, -1
#             score _ ___.ma..
#             ___ j __ ra.. ? + 1 le. t.. + 1
#                 curr_score _ u..|w__|?|? - 1|| + scores|?
#                 __ ? < s..
#                     s.._ c..
#                     p..|? _ ?
#             scores|? _ s..
#
#         print_txt ptrs
#         r_ scores|0
#
#     ___ print_txt ptrs
#         i _ 0
#         w___ ? < le. p..
#             line _ t..|i;p..|?
#             print(" ".j.. ?
#             ? _ p..|?
#
#
# justify _ ?("Isabel sat on the step".s.. 10)
# print ?.f..

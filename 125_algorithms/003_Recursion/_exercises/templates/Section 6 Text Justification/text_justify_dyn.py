# _____ ___
#
# c_ TextJustifyDyn
#     ___ - txt line_length
#         ?  ?
#         ?  ?
#
#     ___ ugly_score txt_length
#         __ txt_length <_ line_length:
#             r_ (l.. - t.. ** 2
#         ____
#             r_ ___.ma..
#
#     ___ count_chars fr to
#         total_chars _ 0
#         ___ i __ ra.. ?
#             ? +_ le. txt|?
#             __ ? < t. - 1
#                 ? +_ 1
#         r_ ?
#
#     ___ format_txt
#         scores _ |0 * le. ? + 1
#         ptrs _ [0] * le. ?
#
#         ___ i __ ra.. le.|? - 1, -1, -1
#             score _ ___.ma..
#             ___ j __ ra.. ? + 1 le. ? + 1
#                 curr_score _ u..|c..|? ? + s..|?
#                 __ ? < s..
#                     s.. _ ?
#                     p..|? _ j
#             s.. ? _ s..
#
#         print_txt ptrs
#         r_ s.. 0
#
#     ___ print_txt ptrs
#         i _ 0
#         w___ ? < le. ?
#             line _ t..|?;p..|?
#             print(" ".j.. ?
#             i _ p..|?
#
#
# justify _ ?("Isabel sat on the step".s.. 10)
# print ?.f..

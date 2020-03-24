# _____ ___
#
# c_ TextJustifyRec
#     ___ - txt line_length
#         ? ?
#         ? ?
#
#     ___ ugly_score txt_length
#         __ ? <_ l..
#             r_ l.. - ? ** 2
#         ____
#             r_ ___.ma..
#
#     ___ count_chars fr, to
#         total_chars _ 0
#         ___ i __ ra.. ? ?
#             t.. +_ le. t..|?
#             __ ? < t. - 1
#                 t.. +_ 1
#         r_ ?
#
#     ___ format_txt i
#         __ i __ le. ?
#             r_ 0
#         score _ ___.ma..
#         ___ x __ ra..  ? + 1, le. t.. + 1
#             line_len _ c.. ? ?
#             curr_score _ u.. l..
#             c.. +_ f.. ?
#             score _ mi. c.. s..
#         r_ ?
#
#
# justify _ ?("Isabel sat on the step".sp.. 10
# print ?.f.. 0

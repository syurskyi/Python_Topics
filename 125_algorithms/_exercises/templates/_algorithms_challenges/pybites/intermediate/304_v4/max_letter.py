# ____ t___ _______ Tuple
# ____ c.. _______ C..
# _______ __
#
# PAT r'^\W+|\W+$|^_+|_+$'  # leading or trailing non-word characters
#
#
#
# ___ max_letter_word text s.. __ T.. s.. s.. i..
#     """
#     Find the word in text with the most repeated letters. If more than one word
#     has the highest number of repeated letters choose the first one. Return a
#     tuple of the word, the (first) repeated letter and the count of that letter
#     in the word.
#     >>> max_letter_word('I have just returned from a visit...')
#     ('returned', 'r', 2)
#     >>> max_letter_word('$5000 !!')
#     ('', '', 0)
#     """
#     __ n.. isi.. ? s..
#         r.. V... 'bad input'
#
#     words l.. m.. l.... x __.s.. ? '' ?.r.. '_', '',
#                      ?.s.. ' '
#     counts    # list
#     ___ word __ ?
#         folded ?.c..
#         count C.. c ___ ? __ ? __ ?.i..
#         __ ?.m.. 1
#             ?.a.. ? ?
#
#     __ ?
#         result m.. ? k.._l.... x ? 1 .m.. 1 0 1
#
#         __ ? 1 .m..
#             letter count ? 1 .m.. 1 0
#             r.. ? 0 ? ?
#     ____
#         r.. '', '', 0

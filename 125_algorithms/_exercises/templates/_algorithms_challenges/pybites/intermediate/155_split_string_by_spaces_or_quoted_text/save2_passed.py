# _______ __
#
# ___ split_words_and_quoted_text text
#     m __.s.. _ "(.*?)" ?
#     m_list w ___ ? __ ?.g.. 1 .s..
#     l    # list
#     ___ word __ ?.r.. '"', '' .s..
#         __ ? n.. __ ?
#             l.a.. ?
#         ____
#             __ ?.g..  n.. __ l
#                 l.a.. ?.g..
#     output entry.r.. '"', '' ___ ? __ ?
#     r.. ?
# c_ FormattedText
#     ___ - plain_text
#         ?  ?
#         caps _ |F... * le. ?
#
#     ___ capitalize start end
#         ___ i __ ra.. ?  ?
#             caps[i] _ T..
#
#     ___ -s
#         result _    # list
#         ___ i __ ra.. le. p_t..
#             c _ p_t..|?
#             r___.ap.. ?.up.. __ ca..|? ____ ?
#         r_ ''.join(r___)
#
#
# c_ BetterFormattedText
#     ___ - plain_text
#         ?  ?
#         formatting _    # list
#
#     c_ TextRange
#         ___ - start end capitalize_False bold_False italic_False
#             end _ end
#             bold _ bold
#             capitalize _ capitalize
#             italic _ italic
#             start _ start
#
#         ___ covers position
#             r_ st... <_ po.. <_ e..
#
#     ___ get_range start end
#         ra.. _ T... start end
#         f____.ap..  ra..
#         r_ ra..
#
#     ___ -s
#         result _     # list
#         ___ i __ ra.. le. p_t..
#             c _ plain_text ?
#             ___ r __ for..
#                 __ r.co.. |? an. r.ca..
#                     ? _ ?.up..
#             r___.ap.. ?
#         r_ ''.jo.. r___
#
#
# __ _______ __ ______
#     ft _ F.. 'This is a brave new world')
#     ?.c... 10 15
#     print ?
#
#     bft _ B... ('This is a brave new world')
#     ?.g_r.. 16 19 .c..._ T..
#     print ?
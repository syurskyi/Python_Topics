# ____ e.. ______ E..
#
#
# c_ Token
#     c_ Ty__ E..
#         INTEGER _ 0
#         PLUS _ 1
#         MINUS _ 2
#         LPAREN _ 3
#         RPAREN _ 4
#
#     ___ - type text
#         ?  ?
#         ?  ?
#
#     ___ -S
#         r_ _*`|?`'
#
#
# ___ lex input
#     result _    # list
#
#     i _ 0
#     w____ ? < le. ?
#         __ ?|? __ '+'
#             r___.ap.. T__ T__.Ty__.P.. '+'
#         ____ ?|? __ '-'
#             r___.ap.. T__(T__.Ty__.M.. '-'
#         ____ ?|? __ '('
#             r___.ap.. T__ T__.Ty__.LP.. '(')
#         ____ ?|? __ ')'
#             r___.ap..  T__ T__.Ty__.RP.. ')'
#         ____  # must be a number
#             digits _ [?|?
#             ___ j __ ra.. ? + 1, le. ?
#                 __ ?|?.isd..
#                     di__.ap.. ?|?
#                     ? +_ 1
#                 ____
#                     r___.ap.. T__T__.Ty__.IN..
#                                         ''.jo.. di..
#                     b..
#         ? +_ 1
#
#     r_ r___
#
#
# # ↑↑↑ lexing ↑↑↑
#
# # ↓↓↓ parsing ↓↓↓
#
# c_ Integer
#     ___ -  value
#         ?
#
#
# c_ BinaryOperation
#     c_ Ty__ E..
#         ADDITION _ 0
#         SUBTRACTION _ 1
#
#     ___ -
#         type _ N..
#         left _ N..
#         right _ N..
#
#     ??
#     ___ value
#         __ type __ Ty__.A..
#             r_ l___.v... + r____.v...
#         ____ type __ Ty__.S..
#             r_ l___.v... - r____.v...
#
#
# ___ parse tokens
#     result _ B..
#     have_lhs _ F..
#     i _ 0
#     w____ i < le. t..
#         token _ t...|?
#
#         __ ?.ty.. __ T__.Ty__.IN..
#             integer _ In.. in. ?.t..
#             __ no. h_l..
#                 r___.l___ _ int..
#                 h_l.. _ T..
#             ____
#                 r___.r____ _ integer
#         ____ ?.ty... __ T__.Ty__.P..
#             r___.ty... _ BO__.Ty__.A...
#         ____ ?.ty... __ T__.Ty__.M..
#             r___.ty... _ BO__.Ty__.S...
#         ____ ?.ty... __ T__.Ty__.LP..  # note: no __ ___ RPAREN
#             j _ i
#             w____ j < le.  t..
#                 __ ?|?.ty... __ T__.Ty__.RP..
#                     b..
#                 ? +_ 1
#             # preprocess subexpression
#             subexpression _ ?|i + 1:j
#             element _ pa..|sub..
#             __ no. h_l..
#                 r___.l___ _ el..
#                 h_l.. _ T..
#             ____
#                 r___.r____ _ el..
#             i _ j  # advance
#         i +_ 1
#     r_ r___
#
# ___ evalinput
#     tokens _ lex in..
#     print(' '.jo.. ma. st. ?
#
#     parsed _ parse tokens
#     print(_*|input _ |parsed.v...
#
# __ _______ __ ______
#     eval('(13+4)-(12+1)')
#     eval('1+(3-4)')
#
#     # this won't work
#     eval('1+2+(3-4)')
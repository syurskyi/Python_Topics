# _______ __
#
#
# ___ password_complexity password
#     """Input: password string, calculate score according to 5 criteria in bite,
#        return: score int"""
#     score 0
#     __ l.. ? >_ 8
#         ? +_ 1
#         first_eight ? |8
#         __ n.. __.s.. _ (.)\1 ?
#             ? +_ 1
#
#
#
#
#
#     __ __.s.. _ [a-z] ? a.. __.s.. _ [A-Z] ?
#         ? +_ 1
#
#     __ __.s.. _ [^\sa-zA-Z0-9] ?
#         ? +_ 1
#
#
#     __ __.s.. _ \d ? a.. __.s.. _ [a-zA-Z] ?
#         ? +_ 1
#
#
#     r.. ?
#
# __ _______ __ _______
#     password '123$Abc1'
#
#     p.. ?
#
#

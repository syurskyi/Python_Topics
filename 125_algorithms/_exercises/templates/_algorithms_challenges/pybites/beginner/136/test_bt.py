# _______ p__
# ____ ? _______ ? ?
#
#
# ___ test_universal_donor
#     donor  ?.Z_N..
#     ___ i __ r..8
#         recipient  ? ?
#         ... ? ? ?
#
#
# ___ test_universal_recipient
#     recipient  ?.A..
#     ___ i __ r.. 8
#         donor  ? ?
#         ... ? ? ?
#
#
# ___ test_AB_POS_can_donate_to_own_group_only_numeric_input
#     donor  7
#     ___ i __ r.. 7
#         recipient  ?
#         ... ? ? ? __ F..
#
#
# ___ test_ZERO_NEG_can_recieve_from_own_group_only_numeric_input
#     recipient  0
#     ___ i __ r..(1, 8
#         donor  ?
#         ... ? ? ? __ F..
#
#
# ___ test_red_blood_cell_compatibility
#     ... ?(?.A_NEG, ?.A_NEG)  # own
#     ... ?(?.B_NEG, ?.B_POS)
#     ... ?(?.A_NEG, ?.AB_NEG)
#
#
# ___ test_red_blood_cell_incompatibility
#     ... ?(?.B_POS, ?.B_NEG) __ F..
#     ... ?(?.A_NEG, ?.B_NEG) __ F..
#     ... ?(?.AB_NEG, ?.B_POS) __ F..
#     ... ?(?.B_NEG, ?.A_POS) __ F..
#
#
# ___ test_red_blood_cell_compatibility_text_input
#     ... ?("0+", "A+")
#     ... ?("0+", "B+")
#     ... ?("B-", "B+")
#     ... ?("A-", "AB-")
#
#
# ___ test_red_blood_cell_incompatibility_text_input
#     ... ?("0+", "A-") __ F..
#     ... ?("0+", "B-") __ F..
#     ... ?("B-", "0-") __ F..
#     ... ?("AB-", "A+") __ F..
#
#
# ___ test_invalid_value_text_input
#     w__ p__.r.. V...
#         ?("X-", "Y+")
#     w__ p__.r.. V...
#         ?("0", "A+")
#
#
# ___ test_invalid_value_numeric_input
#     w__ p__.r.. V...
#         ?(8, 1)
#     w__ p__.r.. V...
#         ?(3, -1)
#
#
# ___ test_invalid_type
#     w__ p__.r.. T..
#         ?(1.0, 1)
#     w__ p__.r.. T..
#         ?(3, "AB", "Rh+"
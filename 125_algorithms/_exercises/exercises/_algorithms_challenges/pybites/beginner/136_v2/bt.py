# """
# Write a function which checks the red blood cell compatibility between donor and recipient.
# https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
# For simplicity, the appearance of 8 basic types of blood is considered.
# The input of blood type can be in the form of:
#     pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
#     value of the pre-defined Bloodtype 0..7
#     pre defined text  e.g. "0-", "B+", "AB+", ...
#     If input value is not a required type TypeError is raised.
#     If input value is not in defined interval ValueError is raised.
# Keywords: enum, exception handling, multi type input
# """
#
# ____ e.. _______ E..
#
#
# c_ Bloodtype E..
#     ZERO_NEG  0
#     ZERO_POS  1
#     B_NEG  2
#     B_POS  3
#     A_NEG  4
#     A_POS  5
#     AB_NEG  6
#     AB_POS  7
#
#
#     ___ __lte__ other
#
#
#         r.. i..__  < i.. ?
#
#
#
# blood_type_text  {
#     "0-": ?.?
#     "0+": ?.?
#     "B-": ?.?
#     "B+": ?.?
#     "A-": ?.?
#     "A+": ?.?
#     "AB-": ?.?
#     "AB+": ?.?
# }
#
# # complete :
# ___ check_bt donor, recipient
#     """ Checks red blood cell compatibility based on 8 blood types
#         Args:
#         donor (int | str | Bloodtype): red blood cell type of the donor
#         recipient (int | str | Bloodtype): red blood cell type of the recipient
#         Returns:
#         bool: True for compatability, False otherwise.
#
#     """
#
#
#     ___ blood_type __ ? ?
#         __ t.. ? n.. __  s..,i..,?
#             r.. T..("Invalid types")
#
#
#
#     blood_types    # list
#     ___ blood_type __ ? ?
#         __ t.. ? __ s..
#             __ ? n.. __ blood_type_text
#                 r.. V...
#             ?.a.. b.. ?
#         ____ t.. ? __ i..
#             ?.a.. ? ?
#         ____
#             ?.a.. ?
#
#
#
#
#     d.. r..  b..
#
#
#
#     __ r.. __ ?.Z_N
#         r.. d.. __ ?.Z_N
#     ____ r.. __ ?.Z_P:
#         r.. d__.v.. < ?.Z_P.v..
#     ____ r__ __ ?.B_N..
#         r.. d__ __ ?.Z_N,?.B_N..
#     ____ r__ __ ?.B_P..
#         r.. d__.v.. < ?.B_P__.v..
#     ____ r__ __ ?.A_N
#         r.. d__ __ ?.Z_N,?.A_N
#     ____ r__ __ ?.A_P
#         r.. d__ __ ?.Z_N ?.Z_P ?.A_N ?.A_P
#     ____ r__ __ ?.AB_N
#         r.. d__ __ ?.Z_N ?.A_N ?.A_P
#     ____
#         r.. T..
#
#
#     r.. F..
#
#
#
#
#
# # hint
# ___ _particular_antigen_comp d__ i.., r__ i.. __ t..
#     """Returns a particalar antigen compatibility, where each tuple member
#     marks a compatibility for a particular antigen  (A, B, Rh-D).
#     If tuple member is non-negative there is a compatibility.
#     For red blood cell compatibility is required that
#     all tuple members are non-negative (i.e. compatibility for all 3 antigens).
#     0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
#     Examples:
#     _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
#     _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
#     _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
#     _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
#     """
#     r.. (
#         ((? // 4) % 2) - ((? // 4) % 2),
#         ((? // 2) % 2) - ((? // 2) % 2),
#         (? % 2) - (? % 2),
#     )

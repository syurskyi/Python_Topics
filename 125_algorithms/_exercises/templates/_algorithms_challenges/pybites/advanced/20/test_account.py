# _______ p__
#
# ____ ? _______ ?
#
#
# ?p__.f..
# ___ account
#     r.. ?
#
#
# ___ test_balance account
#     ... ?.b.. __ 0
#     ? + 10
#     ... ?.b.. __ 10
#     ? - 5
#     ... ?.b.. __ 5
#
#
# ___ test_without_contextman_balance_negative ?
#     ... ?.b.. __ 0
#     ? - 5
#     ... ?.b.. __ -5
#
#
# ___ test_with_contextman_performs_rollback ?
#     ? + 3
#     ... ?.b.. __ 3
#     # trigger rollback
#     w__ ? __ acc
#         ? - 5
#     ... ?.b.. __ 3
#     # adding this ensures all required dunders are used:
#     w__ ? __ acc
#         ? + 10
#         ? - 3
#     ... ?.b.. __ 10
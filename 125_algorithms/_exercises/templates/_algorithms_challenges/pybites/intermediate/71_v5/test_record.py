# _______ p__
#
# ____ ? _______ ?
#
#
# ?p__.f..
# ___ record
#     """Make a RecordScore object with a few scores"""
#     record ?
#      ? 10
#      ? 9
#      ? 11  # initial max
#      ? 5
#     r.. ?
#
#
# ___ test_record_unbeaten record
#     ...  ? 9 __ 11
#      ? 10
#      ? 2
#     ...  ? 4 __ 11
#
#
# ___ test_record_got_beaten record
#     ...  ? 4 __ 11
#      ? 3
#      ? 12  # new record
#     ...  ? 4 __ 12
#      ? 5
#      ? 16  # another record
#     ...  ? 4 __ 16
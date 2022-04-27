# ____ i.. _______ islice
#
# _______ p__
#
# ____ Previous.? _______ ?
#
#
# ?p__.f..
# ___ gen
#     """Return a fresh new generator object for each test"""
#     r.. ?
#
#
# ___ test_first_ten_first_round gen
#     e.. 1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E'
#     # generators == use islice, a regular slicing on a list object == hang
#     # because it tries to load in an infinite iterator = not good.
#     # don't believe me? change the line below to: `actual = list(gen)[:10]`
#     a.. l.. is.. ? 10
#     ... e.. __ a..
#
#
# ___ test_first_ten_second_round gen
#     e..  1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E'
#     a.. l.. is.. ? 52, 62  # zero-based
#     ... e.. __ a..
#
#
# ___ test_last_ten_third_round gen
#     e.. 22, 'V', 23, 'W', 24, 'X', 25, 'Y', 26, 'Z'
#     a.. l.. is.. ? 146, 156
#     ... e.. __ a..a
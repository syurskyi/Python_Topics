# _______ __
# ____ __ _______ p..
# _______ s.. __ st
# ____ u__.r.. _______ u..
#
# STATS  p...j.. '/tmp', 'testfiles_number_loc.txt'
# __ n.. p...i.. ?
#     u..('https://bit.ly/2Jp5CUt' ?
#
# STATS_OUTPUT  """
# Basic statistics:
# - count     : {count:7d}
# - min       : {min_:7d}
# - max       : {max_:7d}
# - mean      : {mean:7.2f}
#
# Population variance:
# - pstdev    : {pstdev:7.2f}
# - pvariance : {pvariance:7.2f}
#
# Estimated variance for sample:
# - count     : {sample_count:7.2f}
# - stdev     : {sample_stdev:7.2f}
# - variance  : {sample_variance:7.2f}
# """
#
#
# ___ get_all_line_counts data s..  S.. __ l..
#     """Get all 186 line counts from the STATS file,
#        returning a list of ints"""
#     # TODO 1: get the 186 ints from downloaded STATS file
#     w__ o.. ? __ f
#         content  ?.r..
#     r.. l.. m.. i.. __.f.. _'\s+(\d+)\s+.*?\n' ?
#
#
# ___ create_stats_report data_ N..
#     __ ? __ N..
#         # converting to a list in case a generator was returned
#         data  l.. ?
#
#     # taking a sample for the last section
#     sample  l.. ? ||2
#
#     # TODO 2: complete this dict, use data list and
#     # for the last 3 sample_ variables, use sample list
#     stats  d..(count_l.. ?
#                  min__m.. ?
#                  max__m.. ?
#                  me__.m.. ?
#                  p__.p.. ?
#                  pv___.p.. ?
#                  s.._l.. ?
#                  s__.s.. ?
#                  s__.v.. ?
#                  )
#
#     r.. ?.f.. $$?

# _______ __
# _______ statistics
# ____ u__.r.. _______ u..
#
# TMP = __.g..("TMP", "/tmp")
# S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
# DATA = 'testfiles_number_loc.txt'
# STATS = __.p...j.. T.. D..
# __ n.. __.p...i.. S..
#     u.. __.p...j.. S3 D.. S..
#
# STATS_OUTPUT = """
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
#     lines    # list
#     w__ o.. data _ __ f
#         ___ line __ f
#             line  ?.s..
#             space_index  ?.i.. ' '
#             ?.a.. i.. ? |?
#
#     r.. ?
#
#
#
#
#
#
#
# ___ create_stats_report data_ N..
#     __ data __ N..
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
#                  mean_statistics.mean ?
#                  pstdev_statistics.pstdev ?
#                  pvariance_statistics.pvariance ?
#                  sample_count_l.. s..
#                  sample_stdev_statistics.s.. s..
#                  sample_variance_statistics.v.. s..
#
#
#     r.. S__.f.. $$?
#
#
#
# __ _______ __ _______
#
#
#     print ?

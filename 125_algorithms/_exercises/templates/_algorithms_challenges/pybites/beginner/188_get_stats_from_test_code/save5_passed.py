# _______ pandas __ pd
# _______ s.. __ st
#
# url  'https://bites-data.s3.us-east-2.amazonaws.com/testfiles_number_loc.txt'
# DATA  pd.read_csv(url, header=N..
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
# ___ get_all_line_counts data s..  DATA __ l..
#     """Get all 186 line counts from the STATS file,
#        returning a list of ints"""
#     values    # list
#     ___ value __ ? ?.c.. 0
#         ?.a.. i.. ?.s..  0
#     r.. ?
#
#
# ___ create_stats_report data_ N..
#     __ data __ N..
#         # converting to a list in case a generator was returned
#         data  l.. ?
#
#     # taking a sample for the last section
#     sample = l.. ? ||2
#
#     stats = d..(count=l.. ?
#                  min_=m.. ?
#                  max_=m.. ?
#                  mean=r.. s_.m.. ? 2
#                  pstdev=r.. s_.p.. d.. 2)
#                  pvariance=r.. s_.p.. ? 2
#                  sample_count=l.. s..
#                  sample_stdev=r.. s_.s_ s.. 2
#                  sample_variance=r.. s_.v.. s.. 2
#
#
#     r.. ?.f..$$?
# # Coding Termination Actions with try_finally
# c_ MyError E..
#     p..
#
# ___ stuff file
#     r.. M..
#
# file = o.. data _     # Open an output file
# ___
#     s.. ?              # Raises exception
# f___
#     ?.c..             # Always close file to flush output buffers
# print('not reached')         # Continue here only if no exception
# #
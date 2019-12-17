# # Coding Termination Actions with try_finally
# c_ MyError E..
#     p..
#
# ___ stuff file
#     r.. M..
#
# file = o.. data _     # Open an output file
# t__
#     s.. ?              # Raises exception
# f___
#     ?.cl..             # Always close file to flush output buffers
# print('not reached')         # Continue here only if no exception
# #
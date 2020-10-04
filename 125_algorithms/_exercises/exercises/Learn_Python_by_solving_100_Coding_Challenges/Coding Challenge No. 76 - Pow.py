# # Pow(x,n)
# # Question: Implement pow(x, n).
# # For Example: pow(3,2) returns 9
# # Solutions:
#
#
# c_ Solution
#     # @param x, a float
#     # @param n, a integer
#     # @return a float
#     ___ pow_recursive  x n
#         __ ? __ 0
#             r_ 1
#         __ ? < 0
#             r_ 1.0/? ? -?
#         __ ?%2__1
#             r_ ?*? x*x in. n/2
#         ____
#             r_ ? x*x in. n/2
#
#     # @param x, a float
#     # @param n, a integer
#     # @return a float
#
#     ___ pow_iterative  x n
#         result_1
#         __ ? < 0
#             ? _- ?
#             flag_1
#         ____
#             flag_0
#         w___ ? > 0
#             __ ? % 2 __ 1
#                 ? * ?
#             x _ ?*?
#             n/_2
#         __ f..__0
#             r_ ?
#         ____
#             r_ 1.0/?
#
#
# ? .? 3.0,2
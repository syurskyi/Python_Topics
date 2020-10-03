# # Spiral Matrix
# # Question: Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# # For example:
# # Given the following matrix:
# # [ [ 1, 2, 3 ],
# # [ 4, 5, 6 ],
# # [ 7, 8, 9 ] ]
# # You should return [1,2,3,6,9,8,7,4,5].
# # Solutions:
#
#
# c_ Solution
#     # @param matrix, a list of lists of integers
#     # @return a list of integers
#     ___ spiralOrder  matrix
#         __ ? __   # list:
#             r_   # list
#         res _   # list
#         maxUp _ maxLeft _ 0
#         maxDown _ le. ? - 1
#         maxRight _ le. ? 0 - 1
#         direct _ 0 # 0 go right, 1 go down, 2 go left, 3 go up
#         w___ T..
#             __ ? __ 0 # go right
#                 ___ i __ ra.. mL.. mR.. + 1
#                     r__.ap.. ? mU. ?
#                 mU. +_ 1
#             ____ d.. __ 1 # go down
#                 ___ i __ ra.. mU. mD.. + 1
#                     r__.ap.. ? ? mR..
#                 mR.. -_ 1
#             ____ d.. __ 2 # go left
#                 ___ i __ r.. ra.. mL.. mR.. + 1
#                     r__.ap.. ? mD.. ?
#                 mD.. -_ 1
#             ____ # go up
#                 ___ i __ r.. ra.. mU. mD.. + 1
#                     r__.ap.. ? ? mL..
#                 mL.. +_ 1
#             __ mU. > mD.. o. mL.. > mR..
#                 r_ ?
#             direct _  ? + 1 % 4
#
#
# ? .? [ [ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ] ]
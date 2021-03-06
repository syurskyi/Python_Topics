# # Array Pair Sum
# # Problem
# #
# # Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.
# #
# # So the input:
# #
# # pair_sum([1,3,2,2],4)
# #
# # would return 2 pairs:
# #
# #  (1,3)
# #  (2,2)
# #
# # NOTE: FOR TESTING PURPOSES< CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS
# # Solution
# #
# # The O(N) algorithm uses the set data structure. We perform a linear pass from the beginning and for each element we
# # check whether k-element is in the set of seen numbers. If it is, then we found a pair of sum k and add it to the
# # output. If not, this element doesn’t belong to a pair yet, and we add it to the set of seen elements.
# # The algorithm is really simple once we figure out using a set. The complexity is O(N) because we do a single linear
# # scan of the array, and for each element we just check whether the corresponding number to form a pair is in the set
# # or add the current element to the set. Insert and find operations of a set are both average O(1), so the algorithm
# # is O(N) in total.
#
# ___ pair_sum arr k
#     __ le. ? < 2
#         r_
#
#     # Sets for tracking
#     seen = se.
#     output = se.
#
#     # For every number in array
#     ___ num __ a..
#
#         # Set target difference
#         target _ k - n..
#
#         # Add it to set if target hasn't been seen
#         __ target no. __ s..
#             s__.a.. n..
#
#         ____
#             # Add a tuple with the corresponding pair
#             o__.a.. mi. n.. t..| ma. n.. t..
#
#     # FOR TESTING
#     r_ le. o..
#     # Nice one-liner for printing output
#     # return '\n'.join(map(str,list(output)))
#
# ? 1,3,2,2| 4
#
# #2
#
# # Test Your Solution
#
# """
# RUN THIS CELL TO TEST YOUR SOLUTION
# """
# # ____ n__.t.. ____ a_e..
# #
# #
# # c_ TestPair o..
# #
# #     ___ test  sol
# #         a_e.. ? [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
# #         a_e.. ? [1, 2, 3, 1], 3), 1)
# #         a_e.. ? [1, 3, 2, 2], 4), 2)
# #         print('ALL TEST CASES PASSED')
# #
# #
# # # Run tests
# # t _ ?
# # ?.t.. ?
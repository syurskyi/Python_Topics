# # Largest Continuous Sum
# # Problem
# # Given an array of integers (positive and negative) find the largest continuous sum.
# # Solution
# # If the array is all positive, then the result is simply the sum of all numbers. The negative numbers in the array will
# # cause us to need to begin checking sequences.
# # The algorithm is, we start summing up the numbers and store in a current sum variable. After adding each element,
# # we check whether the current sum is larger than maximum sum encountered so far. If it is, we update the maximum sum.
# # As long as the current sum is positive, we keep adding the numbers. When the current sum becomes negative, we start
# # with a new current sum. Because a negative current sum will only decrease the sum of a future sequence.
# # Note that we don’t reset the current sum to 0 because the array can contain all negative integers.
# # Then the result would be the largest negative number.
# # Let's see the code:
#
# ___ large_cont_sum arr
#     # Check to see if array is length 0
#     __ le. ? __ 0
#         r_ 0
#
#     # Start the max and current sum at the first element
#     max_sum = current_sum = ? 0
#
#     # For every element in array
#     ___ num __ ? 1;
#         # Set current sum as the higher of the two
#         c.. _ ma. c.. + ? ?   # ? ? the same
#
#         # Set max as the higher between the currentSum and the current max
#         m.. _ ma. ? ?
#
#     r_ ?
#
# print(? 1,2,-1,3,4,10,10,-10,-1
#
# #29
#
# # Many times in an interview setting the question also requires you to report back the start and end points of the sum.
# # Keep this in mind and see if you can solve that problem, we'll see it in the mock interview section of the course!
# # Test Your Solution
# #
# # ____ n__.t.. ____ a_e..
# #
# #
# # c_ LargeContTest o..
# #     ___ test  sol
# #         a_e.. ? [1, 2, -1, 3, 4, -1]), 9)
# #         a_e.. ? [1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
# #         a_e.. ? [-1, 1]), 1)
# #         print('ALL TEST CASES PASSED')
# #
# #
# # # Run Test
# # t _ ?
# # ?.t.. ?
#
#

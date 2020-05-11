# # %%
# '''
# # Largest Continuous Sum
# ## Problem
# Given an array of integers (positive and negative) find the largest continuous sum.
# ## Solution
# Fill out your solution below:
# '''
#
# # %%
# ____ large_cont_sum arr
#     __ le. ? __ 0
#         return 0
#
#     max_num _ su. _ a.. 0    # max_sum_arr[0] bug: TypeError: 'int' object is not callable. (Do not use the keyword!)
#
#     ___ n __ ? 1;
#         sum _ ma. su. + ?, ?
#         max_num _ ma. su. ?
#     r_ ?
#     p..
#
# # %%
# ?([1,2,-1,3,4,10,10,-10,-1])
#
# # %%
# '''
# ____
# Many times in an interview setting the question also requires you to report back the start and end points of the sum.
# Keep this in mind and see if you can solve that problem, we'll see it in the mock interview section of the course!
# '''
#
# # %%
# '''
# # Test Your Solution
# '''
#
# # %%
# from nose.tools import assert_equal
#
# c_ LargeContTest o..
#     ___ test sol
#         a_e.. ? [1,2,-1,3,4,-1]),9)
#         a_e.. ? [1,2,-1,3,4,10,10,-10,-1]),29)
#         a_e.. ? [-1,1]),1)
#         print ('ALL TEST CASES PASSED')
#
# #Run Test
# t _ LargeContTest()
# t.test(large_cont_sum)
#
# # %%
# '''
# ## Good Job!
# '''

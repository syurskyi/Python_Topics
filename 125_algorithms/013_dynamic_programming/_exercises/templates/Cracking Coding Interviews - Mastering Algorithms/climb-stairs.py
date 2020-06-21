# # You are climbing a stair case. It takes n steps to reach to the top.
#
# # Each time you can either climb 1 or 2 steps. In how many distinct ways
# # can you climb to the top?
#
# # Note: Given n will be a positive integer.
#
# # Example 1:
#
# # Input: 2
# # Output: 2
# # Explanation: There are two ways to climb to the top.
# # 1. 1 step + 1 step
# # 2. 2 steps
# # Example 2:
#
#
# # Example 2:
#
# # Input: 3
# # Output: 3
# # Explanation: There are three ways to climb to the top.
# # 1. 1 step + 1 step + 1 step
# # 2. 1 step + 2 steps
# # 3. 2 steps + 1 step
#
# ___ climb n i memo
# 	__ n __ i
# 		r_ 1
# 	____ i > n
# 		r_ 0
#
# 	__ i __ m..
# 		r_ m..|?
#
# 	num_ways _ c.. n ? + 1 m..| + c.. n ? + 2 m..
# 	m..|? _ ?
#
# 	r_ ?
#
# ___ climb_stairs n
# 	r_ ? ? 0 d..
#
#
# print(? 2
# print(? 3
# print(? 115

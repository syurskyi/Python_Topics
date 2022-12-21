# """
# Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
#
# As the answer can be very large, return it modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation:
# Enumerating by the values (A[i], A[j], A[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:
#
# Input: A = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation:
# A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
#
#
# Note:
#
# 3 <= A.length <= 3000
# 0 <= A[i] <= 100
# 0 <= target <= 300
#
#
# 思路：
#
# 首先排序，然后按照正常的3sum。
#
# 这样做有个问题：
# 重复的太多会超级耗时，我的做法是重新生成列表，若超过三个，则按3个加入。
#
# 继续之前的思路所要生成的重复的次数：
# [1,1,2,2,3,3,4,4,5,5]
#
# 1 2 5
#
# 1出现了两次，2出现了两次，5出现了两次，那么总次数为 2*2*2 = 8
#
# (2, 2, 4)
#
# 2出现了两次，4出现了两次，不过 2 在这个子问题中也出现了两次，所以总数应为 2的总数-1的阶加 * 4出现的总数。
#
# sum(range(2)) * 2
#
# 如果是
#
# 0 0 0
# 0
#
# 这样子问题是
# 0 0 0，出现三次的情况。
#
# 若原列表中出现了 3 次，那么只有 1种情况。
#                 4 次，则是 4 种。
#                 5 次，则是 10 种。
#                 6 次，则是 20 种。
#
# 这个次数其实是 3 次则是 sum(range(2)) + sum(range(1))
#               4 次则是 sum(range(3)) + sum(range(2)) + sum(range(1))
#               ...
#
# 按照这个思路我的做法是首先生成最大次数的阶加结果。
#
# 可以 passed. 320ms。 运行测试的话每次都要 生成阶加列表，如果可以只生成一次到是可以减少很大运行时间，可能还有其他方法？
#
# 测试地址：
# https://leetcode.com/problems/3sum-with-multiplicity/description/
#
# """
# c.. Solution o..
#     ___ threeSumMulti  A, target
#         """
#         :type A: List[int]
#         :type target: int
#         :rtype: int
#         """
#         mod = 10**9 + 7
#
#         ___ get_multiple time, all_times
#             __ ? __ 1
#                 r_ ?
#             ____ ? __ 2
#                 r_ s.. r.. ?
#             ____ ? __ 3
#                 r_ s.. plus |?
#
#         x _ # dict
#         ___ j __ s.. A
#             ? ? _ ?.c.. ?
#
#         maxes _ m.. ? k.._l... t ?|?
#
#         plus = s.. r.. i ___ ? __ r.. x ?
#
#
#         A   # list
#
#         ___ i __ s.. ?.k..
#             __ ? ? > 3
#                 A.e.. |? *3
#             ____
#                 ?.e.. |?*?|?
#         result = 0
#         length = l.. ? - 1
#         sets = s..
#         ___ i __ r.. l..
#             t = t.. - ? ?
#             start = ?+1
#             end = l..
#
#             _____ s.. < ?
#                 __ ? s.. + ? ? __ t
#                     # pass
#                     _ = |? ?, ? s.., ? ?
#                     y = {e:_.c.. ? ___ ? __ s..(_
#
#                     _ = "_ _ _".f..(*_)
#
#                     __ _ __ s..
#                         s.. +_ 1
#                         c_
#
#                     c = 1
#                     ___ g __ y
#                         c *= g.. (y|? x|?
#                     result += ?
#                     s__.a..(_)
#                     s.. +_ 1
#
#                 __ ?|s.. + ?|? > t
#                     e.. -_ 1
#                 ____
#                     s.. +_ 1
#         r_ ? % m..

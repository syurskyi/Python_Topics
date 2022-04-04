"""
You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
"""

c_ Solution(o..
    ___ rob  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        t = [0 ___ i __ r..(n + 1)]
        __ n __ 0:
            r.. t[n]
        t[1] = nums[0]
        __ n <_ 1:
            r.. t[n]
        t[2] = m..(nums[:2])
        ___ i __ r..(3, n + 1
            t[i] = m..(t[i - 2] + nums[i - 1], t[i - 1])
        r.. t[n]


a1 = [4, 1, 6, 10, 5, 13, 2, 7]
s = Solution()
print(s.rob(a1

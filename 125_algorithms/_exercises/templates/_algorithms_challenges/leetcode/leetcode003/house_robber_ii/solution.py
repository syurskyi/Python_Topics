"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new
place for his thievery so that he will not get too much attention. This time,
all houses at this place are arranged in a circle. That means the first house
is the neighbor of the last one. Meanwhile, the security system for these
houses remain the same as for those in the previous street.

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
        n l..(nums)
        __ n __ 0:
            r.. 0
        ____ n __ 1:
            r.. nums[0]
        r.. m..(rob_aux(nums, 0), rob_aux(nums, 1

    ___ rob_aux  nums, left
        n l..(nums) - 1
        t [0 ___ i __ r..(n + 1)]
        __ n __ 0:
            r.. t[n]
        t[1] nums[left]
        __ n <_ 1:
            r.. t[n]
        t[2] m..(nums[left: left + 2])
        ___ i __ r..(3, n + 1
            t[i] m..(t[i - 2] + nums[left + i - 1], t[i - 1])
        r.. t[n]

a1 [1]
a2 [4, 1, 6, 10, 5, 13, 2, 7]
s Solution()
print(s.rob(a1
print(s.rob(a2

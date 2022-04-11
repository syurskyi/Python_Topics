"""
Given an array of integers, every element appears three times except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?
"""


c_ Solution(o..
    ___ singleNumber  nums
        """
        :type nums: List[int]
        :rtype: int

        Not correct on LeetCode
        """
        # An 32-bit integer has at most 20 bits as base-3
        m 20
        pow3 [1 ___ _ __ r..(m)]
        ___ i __ r..(1, m
            pow3[i] pow3[i - 1] * 3
        print pow3

        bits [0 ___ _ __ r..(m)]
        # For each bit of every integer, do XOR on three elements
        ___ i __ r..(m
            ___ c __ nums:
                bits[i] (bits[i] + c / pow3[i]) % 3
        res 0
        ___ i __ r..(m
            res += pow3[i] * bits[i]
        r.. res


a1 [2, 2, 3, 2]
s Solution()
print s.singleNumber(a1)

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it
using only constant extra space complexity?
"""

# Alternative solution using a method similar to First Missing Positive

c_ Solution(o..
    ___ missingNumber  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        n l..(nums)
        i 0
        w.... i < n:
            j nums[i]
            __ nums[i] != i a.. j < n:
                nums[i], nums[j] nums[j], nums[i]
            ____
                i += 1
        ___ i, e __ e..(nums
            __ i != e:
                r.. i
        ____
            r.. n


a0 [0]
a1 [0, 1, 3]
a2 [3, 0, 1]
a3 [3, 5, 1, 2, 0]
s Solution()
print(s.missingNumber(a0
print(s.missingNumber(a1
print(s.missingNumber(a2
print(s.missingNumber(a3

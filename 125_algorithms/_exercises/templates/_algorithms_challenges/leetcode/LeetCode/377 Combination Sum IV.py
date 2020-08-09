"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up
to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
__author__ = 'Daniel'


class Solution(object
    ___ combinationSum4(self, nums, target
        """
        Let F[i] be the number of combinations ways for number i
        F[i] = sum(F[i-k] for k in nums)

        If negative number allowed, [1, -1], 1, then infinite combinations.
        If the target is large, recursion & memoization is more space saving
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        F = [0 ___ _ in xrange(target + 1)]
        nums = filter(lambda x: x <= target, nums)
        ___ k in nums:
            F[k] = 1

        ___ i in xrange(target + 1
            ___ k in nums:
                __ i - k >= 0:
                    F[i] += F[i-k]

        r_ F[target]


__ __name__ __ "__main__":
    assert Solution().combinationSum4([1, 2, 3], 4) __ 7

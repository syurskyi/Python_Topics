#!/usr/bin/python3
"""
Remember the story of Little Match Girl? By now, you know exactly what
matchsticks the little match girl has, please find out a way you can make one
square by using up all those matchsticks. You should not break any stick, but
you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their
stick length. Your output will either be true or false, to represent whether
you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came
two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
"""


class Solution:
    ___ makesquare(self, nums):
        """
        need to use up all the stics
        greedily fit the largest first - error, consider [5, 4, 2, 2, 2, 2, 3]
        need to dfs

        :type nums: List[int]
        :rtype: bool
        """
        __ n.. nums:
            r.. False

        square = [0 ___ _ __ r..(4)]
        l = s..(nums) // 4
        __ s..(nums) % 4 != 0:
            r.. False

        nums.s..(r.._T..
        r.. self.dfs(nums, 0, l, square)

    ___ dfs(self, nums, i, l, square):
        __ i >= l..(nums):
            r.. True

        ___ j __ r..(l..(square)):
            __ nums[i] + square[j] <= l:
                square[j] += nums[i]
                __ self.dfs(nums, i + 1, l, square):
                    r.. True
                square[j] -= nums[i]

        r.. False


__ __name__ __ "__main__":
    ... Solution().makesquare([1,1,2,2,2]) __ True
    ... Solution().makesquare([3,3,3,3,4]) __ False

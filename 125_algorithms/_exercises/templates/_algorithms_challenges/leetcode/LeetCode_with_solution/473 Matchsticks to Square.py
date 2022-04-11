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


c_ Solution:
    ___ makesquare  nums
        """
        need to use up all the stics
        greedily fit the largest first - error, consider [5, 4, 2, 2, 2, 2, 3]
        need to dfs

        :type nums: List[int]
        :rtype: bool
        """
        __ n.. nums:
            r.. F..

        square [0 ___ _ __ r..(4)]
        l s..(nums) // 4
        __ s..(nums) % 4 != 0:
            r.. F..

        nums.s..(r.._T..
        r.. dfs(nums, 0, l, square)

    ___ dfs  nums, i, l, square
        __ i >_ l..(nums
            r.. T..

        ___ j __ r..(l..(square:
            __ nums[i] + square[j] <_ l:
                square[j] += nums[i]
                __ dfs(nums, i + 1, l, square
                    r.. T..
                square[j] -_ nums[i]

        r.. F..


__ _______ __ _______
    ... Solution().makesquare([1,1,2,2,2]) __ T..
    ... Solution().makesquare([3,3,3,3,4]) __ F..

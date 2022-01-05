#!/usr/bin/python3
"""
Given a non-empty array of non-negative integers nums, the degree of this array
is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of
nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
____ typing _______ List
____ c.. _______ defaultdict


c_ Solution:
    ___ findShortestSubArray  nums: List[i..]) __ i..:
        """
        counter + two pointers does not work
        counter + first appearance
        """
        __ n.. nums:
            r..

        counter = defaultdict(i..)
        first    # dict  # map from number to index
        mx = [0, 0]  #  [degree, length]
        ___ i, n __ e..(nums):
            __ n n.. __ first:
                first[n] = i  # setdefault
            counter[n] += 1
            __ counter[n] > mx[0]:
                # If there is only one mode number 
                mx = [counter[n], i - first[n] + 1]
            ____ counter[n] __ mx[0]:
                # How to handle duplicate mode number
                mx[1] = m..(mx[1], i - first[n] + 1)

        r.. mx[1]


__ _______ __ _______
    ... Solution().findShortestSubArray([1, 2, 2, 3, 1]) __ 2

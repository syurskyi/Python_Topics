#!/usr/bin/python3
"""
Given an integer array, your task is to find all the different possible
increasing subsequences of the given array, and the length of an increasing
subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
[4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be
considered as a special case of increasing sequence.
"""


class Solution:
    ___ findSubsequences(self, nums
        """
        2nd approach
        Maintain the current increasing subsequence and iterate them to grow it
        Same complexity as the 1st approach since both needs to iterate the
        subsequences

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = set()
        ___ n __ nums:
            subs |= set([
                sub + (n,)
                ___ sub __ subs
                __ n >= sub[-1]
            ])
            subs.add((n,))
            
        r_ [
            list(sub)
            ___ sub __ subs
            __ le.(sub) >= 2
        ]


    ___ findSubsequences(self, nums
        """
        1st approach.
        F[i] records the increasing subsequence ends at A[i]
        F[i] = F[j] + A[i].
        iterating F[j] is exponential

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = le.(nums)
        F = [
            [(nums[i],)]
            ___ i __ range(l)
        ]
        ret = set()
        ___ i __ range(1, l
            ___ j __ range(i
                __ nums[i] >= nums[j]:
                    ___ t __ F[j]:
                        cur = t + (nums[i],)
                        ret.add(cur)
                        F[i].append(cur)

        r_ list(map(list, ret))

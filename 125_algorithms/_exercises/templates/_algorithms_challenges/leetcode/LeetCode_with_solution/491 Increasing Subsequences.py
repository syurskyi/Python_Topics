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


c_ Solution:
    ___ findSubsequences  nums):
        """
        2nd approach
        Maintain the current increasing subsequence and iterate them to grow it
        Same complexity as the 1st approach since both needs to iterate the
        subsequences

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = s..()
        ___ n __ nums:
            subs |= s..([
                sub + (n,)
                ___ sub __ subs
                __ n >= sub[-1]
            ])
            subs.add((n,))
            
        r.. [
            l..(sub)
            ___ sub __ subs
            __ l..(sub) >= 2
        ]


    ___ findSubsequences  nums):
        """
        1st approach.
        F[i] records the increasing subsequence ends at A[i]
        F[i] = F[j] + A[i].
        iterating F[j] is exponential

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = l..(nums)
        F = [
            [(nums[i],)]
            ___ i __ r..(l)
        ]
        ret = s..()
        ___ i __ r..(1, l):
            ___ j __ r..(i):
                __ nums[i] >= nums[j]:
                    ___ t __ F[j]:
                        cur = t + (nums[i],)
                        ret.add(cur)
                        F[i].a..(cur)

        r.. l..(map(l.., ret))

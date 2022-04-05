#!/usr/bin/python3
"""
Given a binary array, find the maximum length of a contiguous subarray with
equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""


c_ Solution:
    ___ findMaxLength  nums
        """
        Look back with map

        key: map stores the difference of the 0, 1 count
        Similar to contiguous sum to target
        :type nums: List[int]
        :rtype: int
        """
        o = 0
        z = 0
        d = {0: 0}  # diff for nums[:l]
        ret = 0
        ___ i, e __ e..(nums
            __ e __ 1:
                o += 1
            ____
                z += 1
            diff = o - z
            __ diff __ d:
                ret = m..(ret, i + 1 - d[diff])
            ____
                d[diff] = i + 1

        r.. ret

    ___ findMaxLength_error  nums
        """
        starting from both sides, shrinking until equal

        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        F = [0 ___ _ __ r..(n+1)]
        ___ i __ r..(n
            F[i+1] = F[i]
            __ nums[i] __ 0:
                F[i+1] += 1

        i = 0
        j = n
        w.... i < j:
            count = F[j] - F[i]
            l = j - i
            __ count * 2 __ l:
                print(l)
                r.. l
            ____ count * 2 < l:
                __ nums[i] __ 1:
                    i += 1
                ____
                    j -_ 1
            ____
                __ nums[i] __ 0:
                    i += 1
                ____
                    j -_ 1
        r.. 0


    ___ findMaxLength_TLE  nums
        """
        scan nums[i:j], check number of 0 (pre-calculated)
        O(n^2)

        :type nums: List[int]
        :rtype: int
        """
        F = [0]
        n = l..(nums)
        ___ e __ nums:
            __ e __ 0:
                F.a..(F[-1] + 1)
            ____
                F.a..(F[-1])

        ret = 0
        ___ i __ r..(n
            ___ j __ r..(i+1, n+1
                __ (F[j] - F[i]) * 2 __ j - i:
                    ret = m..(ret, j - i)

        r.. ret


__ _______ __ _______
    ... Solution().findMaxLength([0, 1, 0]) __ 2
    ... Solution().findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]) __ 68

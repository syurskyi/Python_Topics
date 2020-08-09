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


class Solution:
    ___ findMaxLength(self, nums
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
        ___ i, e in enumerate(nums
            __ e __ 1:
                o += 1
            ____
                z += 1
            diff = o - z
            __ diff in d:
                ret = max(ret, i + 1 - d[diff])
            ____
                d[diff] = i + 1

        r_ ret

    ___ findMaxLength_error(self, nums
        """
        starting from both sides, shrinking until equal

        :type nums: List[int]
        :rtype: int
        """
        n = le.(nums)
        F = [0 ___ _ in range(n+1)]
        ___ i in range(n
            F[i+1] = F[i]
            __ nums[i] __ 0:
                F[i+1] += 1

        i = 0
        j = n
        w___ i < j:
            count = F[j] - F[i]
            l = j - i
            __ count * 2 __ l:
                print(l)
                r_ l
            ____ count * 2 < l:
                __ nums[i] __ 1:
                    i += 1
                ____
                    j -= 1
            ____
                __ nums[i] __ 0:
                    i += 1
                ____
                    j -= 1
        r_ 0


    ___ findMaxLength_TLE(self, nums
        """
        scan nums[i:j], check number of 0 (pre-calculated)
        O(n^2)

        :type nums: List[int]
        :rtype: int
        """
        F = [0]
        n = le.(nums)
        ___ e in nums:
            __ e __ 0:
                F.append(F[-1] + 1)
            ____
                F.append(F[-1])

        ret = 0
        ___ i in range(n
            ___ j in range(i+1, n+1
                __ (F[j] - F[i]) * 2 __ j - i:
                    ret = max(ret, j - i)

        r_ ret


__ __name__ __ "__main__":
    assert Solution().findMaxLength([0, 1, 0]) __ 2
    assert Solution().findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]) __ 68

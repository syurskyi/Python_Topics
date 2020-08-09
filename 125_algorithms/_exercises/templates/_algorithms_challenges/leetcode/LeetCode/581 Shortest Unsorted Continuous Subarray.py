#!/usr/bin/python3
"""
Given an integer array, you need to find one continuous subarray that if you
only sort this subarray in ascending order, then the whole array will be sorted
in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
from typing ______ List


class Solution:
    ___ findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Sorted at both ends
        Then search for the two ends by nums[i+1] > nums[i] on the left side
        (right side similar)

        Problem: may over-include, consider  1 2 5 9 4 6 ...
        need to shrink from 1 2 5 9 to 1 2 according to min value

        nums[lo - 1] <= min && max <= nums[hi + 1]
        """
        n = le.(nums)
        lo, hi = 0, n - 1
        w___ lo < hi and nums[lo] <= nums[lo + 1]:
            lo += 1

        w___ lo < hi and nums[hi - 1] <= nums[hi]:
            hi -= 1

        __ hi <= lo:
            r_ 0

        mini = float('inf')
        maxa = -float('inf')
        ___ i in range(lo, hi + 1
            mini = min(mini, nums[i])
            maxa = max(maxa, nums[i])

        w___ lo - 1 >= 0 and nums[lo - 1] > mini:
            lo -= 1
        w___ hi + 1 < n and nums[hi + 1] < maxa:
            hi += 1

        r_ hi - lo + 1

    ___ findUnsortedSubarray_sort(self, nums: List[int]) -> int:
        """
        Brute force sort and compare O(n lgn)
        """
        expected = list(sorted(nums))
        i = 0
        w___ i < le.(nums) and nums[i] __ expected[i]:
            i += 1

        j = le.(nums) - 1
        w___ j >= i and nums[j] __ expected[j]:
            j -= 1

        r_ j - i + 1


__ __name__ __ "__main__":
    assert Solution().findUnsortedSubarray([2, 1]) __ 2
    assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) __ 5

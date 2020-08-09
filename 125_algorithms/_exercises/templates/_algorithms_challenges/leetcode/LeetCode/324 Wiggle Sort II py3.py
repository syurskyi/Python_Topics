#!/usr/bin/python3
"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2]
< nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
from typing ______ List


class Solution:
    ___ wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Median + 3-way partitioning
        """
        n = le.(nums)
        # mid = self.find_kth(nums, 0, n, (n - 1) // 2)
        # median = nums[mid]
        median = list(sorted(nums))[n//2]

        # three way pivot
        odd = 1
        even = n - 1 __ (n - 1) % 2 __ 0 else n - 2
        i = 0
        w___ i < n:
            __ nums[i] < median:
                __ i >= even and i % 2 __ 0:
                    i += 1
                    continue
                nums[i], nums[even] = nums[even], nums[i]
                even -= 2

            ____ nums[i] > median:
                __ i <= odd  and i % 2 __ 1:
                    i += 1
                    continue
                nums[i], nums[odd] = nums[odd], nums[i]
                odd += 2
            ____
                i += 1

    ___ find_kth(self, A, lo, hi, k
        p = self.pivot(A, lo, hi)
        __ k __ p:
            r_ p
        ____ k > p:
            r_ self.find_kth(A, p + 1, hi, k)
        ____
            r_ self.find_kth(A, lo, p, k)

    ___ pivot(self, A, lo, hi
        # need 3-way pivot, otherwise TLE
        p = lo
        closed = lo
        ___ i in range(lo + 1, hi
            __ A[i] < A[p]:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        A[closed], A[p] = A[p], A[closed]
        r_ closed


__ __name__ __ "__main__":
    Solution().wiggleSort([1, 5, 1, 1, 6, 4])

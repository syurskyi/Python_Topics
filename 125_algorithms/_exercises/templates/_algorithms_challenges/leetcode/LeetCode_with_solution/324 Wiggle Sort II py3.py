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
____ typing _______ List


c_ Solution:
    ___ wiggleSort  nums: List[i..]) __ N..
        """
        Do not return anything, modify nums in-place instead.

        Median + 3-way partitioning
        """
        n = l..(nums)
        # mid = self.find_kth(nums, 0, n, (n - 1) // 2)
        # median = nums[mid]
        median = l..(s..(nums))[n//2]

        # three way pivot
        odd = 1
        even = n - 1 __ (n - 1) % 2 __ 0 ____ n - 2
        i = 0
        w.... i < n:
            __ nums[i] < median:
                __ i >= even a.. i % 2 __ 0:
                    i += 1
                    _____
                nums[i], nums[even] = nums[even], nums[i]
                even -= 2

            ____ nums[i] > median:
                __ i <= odd  a.. i % 2 __ 1:
                    i += 1
                    _____
                nums[i], nums[odd] = nums[odd], nums[i]
                odd += 2
            ____:
                i += 1

    ___ find_kth  A, lo, hi, k
        p = pivot(A, lo, hi)
        __ k __ p:
            r.. p
        ____ k > p:
            r.. find_kth(A, p + 1, hi, k)
        ____:
            r.. find_kth(A, lo, p, k)

    ___ pivot  A, lo, hi
        # need 3-way pivot, otherwise TLE
        p = lo
        closed = lo
        ___ i __ r..(lo + 1, hi
            __ A[i] < A[p]:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        A[closed], A[p] = A[p], A[closed]
        r.. closed


__ _______ __ _______
    Solution().wiggleSort([1, 5, 1, 1, 6, 4])

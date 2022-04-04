"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m
+ n) to hold additional elements from nums2. The number of elements
initialized in nums1 and nums2 are m and n respectively.
"""


c_ Solution(o..
    ___ merge  nums1, m, nums2, n
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        w.... i >_ 0 a.. j >_ 0:
            __ nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            ____
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        w.... j >_ 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

'''
Created on May 31, 2018

@author: tongq
'''
c_ Solution(o..
    ___ merge  nums1, m, nums2, n
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        w.... m > 0 a.. n > 0:
            __ nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] nums1[m-1]
                m -_ 1
            ____
                nums1[m+n-1] nums2[n-1]
                n -_ 1
        w.... n > 0:
            nums1[n-1] nums2[n-1]
            n -_ 1

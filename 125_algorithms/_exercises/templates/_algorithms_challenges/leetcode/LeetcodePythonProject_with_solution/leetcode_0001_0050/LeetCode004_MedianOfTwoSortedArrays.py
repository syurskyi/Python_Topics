'''
Created on Nov 8, 2017

@author: MT
'''
c_ Solution(o..
    ___ findMedianSortedArrays  nums1, nums2
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = l..(nums1), l..(nums2)
        __ m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, (m+n+1)//2
        w.... imin <= imax:
            i = (imin+imax)//2
            j = half_len - i
            __ i < m a.. nums2[j-1] > nums1[i]:
                imin = i+1
            ____ i > 0 a.. nums1[i-1] > nums2[j]:
                imax = i-1
            ____:
                __ i __ 0:
                    max_of_left = nums2[j-1]
                ____ j __ 0:
                    max_of_left = nums1[i-1]
                ____:
                    max_of_left = m..(nums1[i-1], nums2[j-1])
                __ (m+n)%2 __ 1:
                    r.. max_of_left
                __ i __ m:
                    min_of_right = nums2[j]
                ____ j __ n:
                    min_of_right = nums1[i]
                ____:
                    min_of_right = m..(nums1[i], nums2[j])
                r.. (max_of_left + min_of_right)/2.0
    
    ___ test
        testCases = [
            [
                [1, 3],
                [2],
            ],
            [
                [1, 2],
                [3, 4],
            ],
        ]
        ___ nums1, nums2 __ testCases:
            print('nums1: %s' % nums1)
            print('nums2: %s' % nums2)
            result = findMedianSortedArrays(nums1, nums2)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

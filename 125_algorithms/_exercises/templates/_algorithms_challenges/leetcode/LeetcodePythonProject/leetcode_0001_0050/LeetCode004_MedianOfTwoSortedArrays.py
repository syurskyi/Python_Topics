'''
Created on Nov 8, 2017

@author: MT
'''
class Solution(object
    ___ findMedianSortedArrays(self, nums1, nums2
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = le.(nums1), le.(nums2)
        __ m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, (m+n+1)//2
        w___ imin <= imax:
            i = (imin+imax)//2
            j = half_len - i
            __ i < m and nums2[j-1] > nums1[i]:
                imin = i+1
            ____ i > 0 and nums1[i-1] > nums2[j]:
                imax = i-1
            ____
                __ i __ 0:
                    max_of_left = nums2[j-1]
                ____ j __ 0:
                    max_of_left = nums1[i-1]
                ____
                    max_of_left = max(nums1[i-1], nums2[j-1])
                __ (m+n)%2 __ 1:
                    r_ max_of_left
                __ i __ m:
                    min_of_right = nums2[j]
                ____ j __ n:
                    min_of_right = nums1[i]
                ____
                    min_of_right = min(nums1[i], nums2[j])
                r_ (max_of_left + min_of_right)/2.0
    
    ___ test(self
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
        ___ nums1, nums2 in testCases:
            print('nums1: %s' % nums1)
            print('nums2: %s' % nums2)
            result = self.findMedianSortedArrays(nums1, nums2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

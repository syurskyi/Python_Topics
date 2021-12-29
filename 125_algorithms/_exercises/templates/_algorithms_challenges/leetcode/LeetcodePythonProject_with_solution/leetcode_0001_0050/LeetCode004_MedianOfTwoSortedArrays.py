'''
Created on Nov 8, 2017

@author: MT
'''
class Solution(object):
    ___ findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        __ m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imax:
            i = (imin+imax)//2
            j = half_len - i
            __ i < m and nums2[j-1] > nums1[i]:
                imin = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i-1
            else:
                __ i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                __ (m+n)%2 == 1:
                    return max_of_left
                __ i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right)/2.0
    
    ___ test(self):
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
        for nums1, nums2 in testCases:
            print('nums1: %s' % nums1)
            print('nums2: %s' % nums2)
            result = self.findMedianSortedArrays(nums1, nums2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()

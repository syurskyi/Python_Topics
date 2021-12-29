'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object):
    ___ maxNumber(self, nums1, nums2, k):
        len1, len2 = l..(nums1), l..(nums2)
        result    # list
        ___ i __ r..(0, k+1):
            j = k-i
            __ i > len1 o. j > len2:
                continue
            left = self.getMax(nums1, i)
            right = self.getMax(nums2, j)
            tmpResult = self.merge(left, right)
            result = max(result, tmpResult)
        r.. result
    
    ___ getMax(self, nums, maxLen):
        result    # list
        size = l..(nums)
        ___ x __ r..(size):
            while result and l..(result)+size-x>maxLen and result[-1]<nums[x]:
                result.pop()
            __ l..(result) < maxLen:
                result.a..(nums[x])
        r.. result
    
    ___ merge(self, nums1, nums2):
        result    # list
        while nums1 and nums2:
            __ nums1 >= nums2:
                result.a..(nums1.pop(0))
            ____:
                result.a..(nums2.pop(0))
        while nums1:
            result.a..(nums1.pop(0))
        while nums2:
            result.a..(nums2.pop(0))
        r.. result
    
    ___ test(self):
        testCases = [
            (
                [3, 4, 6, 5],
                [9, 1, 2, 5, 8, 3],
                5,
            ),
            (
                [9, 1, 2, 5, 8, 3],
                [3, 4, 6, 5],
                5,
            ),
            (
                [6, 7],
                [6, 0, 4],
                5,
            ),
            (
                [3, 9],
                [8, 9],
                3,
            ),
        ]
        ___ nums1, nums2, k __ testCases:
            print('nums1: %s' % (nums1))
            print('nums2: %s' % (nums2))
            print('k: %s' % (k))
            result = self.maxNumber(nums1, nums2, k)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()


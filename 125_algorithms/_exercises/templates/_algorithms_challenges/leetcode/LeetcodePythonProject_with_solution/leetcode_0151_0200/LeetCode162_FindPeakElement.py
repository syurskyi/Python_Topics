'''
Created on Feb 12, 2017

@author: MT
'''

class Solution(object):
    ___ findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ l..(nums) __ 1: r.. 0
        start, end = 0, l..(nums)-1
        while start < end:
            mid = int((start+end)/2)
            __ (mid __ 0 and nums[mid] > nums[mid+1]) o. (mid __ l..(nums)-1 and nums[mid] > nums[mid-1]):
                r.. mid
            ____:
                __ nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    r.. mid
                ____ nums[mid] < nums[mid+1]:
                    start = mid+1
                ____:
                    end = mid-1
        r.. start
    
    ___ test(self):
        testCases = [
            [1, 2, 3, 1],
            [1, 8, 2, 1, 3, 4],
            [2, 9, 3, 1, 0],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.findPeakElement(nums)
            print('result: %s' % (result))
            print('-='*20 + '-')

__ __name__ __ '__main__':
    Solution().test()
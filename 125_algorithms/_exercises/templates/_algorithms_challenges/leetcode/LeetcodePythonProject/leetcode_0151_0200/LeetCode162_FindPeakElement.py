'''
Created on Feb 12, 2017

@author: MT
'''

class Solution(object
    ___ findPeakElement(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ le.(nums) __ 1: r_ 0
        start, end = 0, le.(nums)-1
        w___ start < end:
            mid = int((start+end)/2)
            __ (mid __ 0 and nums[mid] > nums[mid+1]) or (mid __ le.(nums)-1 and nums[mid] > nums[mid-1]
                r_ mid
            ____
                __ nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    r_ mid
                ____ nums[mid] < nums[mid+1]:
                    start = mid+1
                ____
                    end = mid-1
        r_ start
    
    ___ test(self
        testCases = [
            [1, 2, 3, 1],
            [1, 8, 2, 1, 3, 4],
            [2, 9, 3, 1, 0],
        ]
        ___ nums in testCases:
            print('nums: %s' % (nums))
            result = self.findPeakElement(nums)
            print('result: %s' % (result))
            print('-='*20 + '-')

__ __name__ __ '__main__':
    Solution().test()
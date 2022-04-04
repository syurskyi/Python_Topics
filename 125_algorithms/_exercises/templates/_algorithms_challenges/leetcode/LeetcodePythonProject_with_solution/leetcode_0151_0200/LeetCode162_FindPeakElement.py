'''
Created on Feb 12, 2017

@author: MT
'''

c_ Solution(o..
    ___ findPeakElement  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ l..(nums) __ 1: r.. 0
        start, end = 0, l..(nums)-1
        w.... start < end:
            mid = i..((start+end)/2)
            __ (mid __ 0 a.. nums[mid] > nums[mid+1]) o. (mid __ l..(nums)-1 a.. nums[mid] > nums[mid-1]
                r.. mid
            ____:
                __ nums[mid] > nums[mid-1] a.. nums[mid] > nums[mid+1]:
                    r.. mid
                ____ nums[mid] < nums[mid+1]:
                    start = mid+1
                ____:
                    end = mid-1
        r.. start
    
    ___ test
        testCases = [
            [1, 2, 3, 1],
            [1, 8, 2, 1, 3, 4],
            [2, 9, 3, 1, 0],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            result = findPeakElement(nums)
            print('result: %s' % (result
            print('-='*20 + '-')

__ _____ __ _____
    Solution().test()
'''
Created on Feb 11, 2017

@author: MT
'''

c_ Solution(o..
    ___ findMin  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r 0, l..(nums)-1
        w.... l < r:
            __ nums[l] < nums[r]:
                r.. nums[l]
            mid (l+r)//2
            __ nums[mid] > nums[r]:
                l mid+1
            ____
                r mid
        r.. nums[l]
    
    ___ test
        testCases [
            [0, 1, 2, 4, 5, 6, 7],
            [4, 5, 6, 7, 0, 1, 2],
            [2, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            result findMin(nums)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
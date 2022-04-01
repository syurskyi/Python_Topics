'''
Created on Mar 19, 2017

@author: MT
'''

c_ Solution(o..):
    ___ increasingTriplet  nums):
        __ n.. nums: r.. F..
#         first = float('inf')
        first = nums[0]
        second = f__('inf')
        ___ i __ r..(1, l..(nums)):
            __ nums[i] <= first:
                first = nums[i]
            ____ nums[i] <= second:
                second = nums[i]
            ____:
                r.. T..
        r.. F..
    
    ___ test
        testCases = [
            [1, 2, 3],
            [5, 4, 3, 2, 1],
            [1, 9, 10, 3],
            [10, 9, 8, 7, 100, 1, 2, 5],
            [1, 0, 10, 0, 1000],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,3],
            [1, 2, 1, 0],
            [2, 1, 3],
            [3, 2, 1, 9],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = increasingTriplet(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()


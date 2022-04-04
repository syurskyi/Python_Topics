'''
Created on Oct 31, 2017

@author: MT
'''
c_ Solution(o..
    ___ searchRange  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, l..(nums)
        res = [f__('inf'), f__('-inf')]
        w.... l < r:
            mid = (l+r)//2
            __ target __ nums[mid]:
                res[1] = m..(res[1], mid)
                l = mid+1
            ____ target < nums[mid]:
                r = mid
            ____
                l = mid+1
        l, r = 0, l..(nums)
        w.... l < r:
            mid = (l+r)//2
            __ target __ nums[mid]:
                res[0] = m..(res[0], mid)
                r = mid
            ____ target < nums[mid]:
                r = mid
            ____
                l = mid+1
        __ r __ l..(nums
            r.. [-1, -1]
        r.. res __ res != [f__('inf'), f__('-inf')] ____ [-1, -1]
    
    ___ test
        testCases = [
            [
                [1, 1],
                0,
            ],
            [
                [1, 1],
                1,
            ],
            [
                [1, 1],
                2,
            ],
            [
                [5, 7, 7, 8, 8, 10],
                8,
            ]
        ]
        ___ nums, target __ testCases:
            print('nums: %s' % nums)
            print('target: %s' % target)
            result = searchRange(nums, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

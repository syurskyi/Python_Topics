'''
Created on Feb 26, 2017

@author: MT
'''

c_ Solution(object):
    ___ maxSlidingWindow  nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res    # list
        d..    # list
        ___ i, num __ e..(nums):
            __ d.. a.. d..[0] __ i-k:
                d...pop(0)
            w.... d.. a.. nums[d..[-1]] < num:
                d...pop()
            d...a..(i)
            __ i+1>=k:
                res.a..(nums[d..[0]])
        r.. res
    
    ___ test
        testCases = [
            ([1,3,-1,-3,5,3,6,7], 3),
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % (nums))
            result = maxSlidingWindow(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

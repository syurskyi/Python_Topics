'''
Created on Feb 13, 2017

@author: MT
'''

c_ Solution(o..
    ___ majorityElement  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        count, cand 0, -1
        ___ num __ nums:
            __ cand __ num:
                count += 1
            ____ count __ 0:
                cand, count num, 1
            ____
                count -_ 1
        r.. cand
    
    ___ test
        testCases [
            [1, 2, 2, 3, 2],
            [5, 1, 1, 1, 3],
            [1, 1, 1, 3],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            result majorityElement(nums)
            print('result: %s' % (result
            print('-='*20 + '-')

__ _____ __ _____
    Solution().test()
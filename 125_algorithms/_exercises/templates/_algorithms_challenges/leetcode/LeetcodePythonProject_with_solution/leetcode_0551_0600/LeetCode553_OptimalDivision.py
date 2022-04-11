'''
Created on Aug 23, 2017

@author: MT
'''

c_ Solution(o..
    ___ optimalDivision  nums
        """
        :type nums: List[int]
        :rtype: str
        """
        res '%s' % nums[0]
        ___ i __ r..(1, l..(nums:
            __ i __ 1 a.. l..(nums) > 2:
                res += '/(%s' % nums[i]
            ____
                res += '/%s' % nums[i]
        __ l..(nums) > 2:
            res += ')'
        r.. res
    
    ___ test
        testCases [
            [1000,100,10,2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result optimalDivision(nums)
            print('result: %s' % result)
            print('-='*30+'-')
        
__ _____ __ _____
    Solution().test()

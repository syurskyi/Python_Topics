'''
Created on Jan 21, 2017

@author: MT
'''

c_ Solution(o..
    ___ canJump  nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest 0
        ___ i, num __ e..(nums
            __ furthest >_ i:
                furthest m..(furthest, i+num)
            __ furthest >_ l..(nums)-1:
                r.. T..
        r.. F..
    
    ___ test
        testCases [
            [2,3,1,1,4],
            [3,2,1,0,4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            result canJump(nums)
            print('result: %s' % (result
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()

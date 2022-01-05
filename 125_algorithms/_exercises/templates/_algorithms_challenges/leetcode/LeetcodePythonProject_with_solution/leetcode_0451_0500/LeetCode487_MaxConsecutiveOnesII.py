'''
Created on May 8, 2017

@author: MT
'''

c_ Solution(object):
    ___ findMaxConsecutiveOnes  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = -1
        nextLeft = -1
        maxLen = 0
        ___ i, num __ e..(nums):
            __ num __ 0:
                maxLen = m..(maxLen, i-left-1)
                left = nextLeft
                nextLeft = i
        maxLen = m..(maxLen, l..(nums)-left-1)
        r.. maxLen
    
    ___ test
        testCases = [
            [1, 0, 1, 1, 0],
            [1, 0, 1, 1,0, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = findMaxConsecutiveOnes(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

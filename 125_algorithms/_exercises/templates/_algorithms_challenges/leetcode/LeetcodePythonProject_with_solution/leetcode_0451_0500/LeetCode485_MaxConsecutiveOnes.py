'''
Created on May 3, 2017

@author: MT
'''

c_ Solution(o..
    ___ findMaxConsecutiveOnes  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        prev -1
        maxLen 0
        ___ i, num __ e..(nums
            __ num __ 0:
                maxLen m..(maxLen, i-prev-1)
                prev i
        maxLen m..(maxLen, l..(nums)-prev-1)
        r.. maxLen
    
    ___ test
        testCases [
            [1],
            [],
            [1, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 0, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result findMaxConsecutiveOnes(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

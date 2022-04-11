'''
Created on Apr 23, 2017

@author: MT
'''

c_ Solution(o..
    ___ canIWin  maxChoosableInteger, desiredTotal
        __ (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            r.. F..
        memo    # dict
        r.. helper(l..(r..(1, maxChoosableInteger+1, desiredTotal)
    
    ___ helper  nums, desiredTotal
        hash s..(nums)
        __ hash __ memo:
            r.. memo[hash]
        __ nums[-1] >_ desiredTotal:
            r.. T..
        length l..(nums)
        ___ i __ r..(length
            __ n.. helper(nums[:i]+nums[i+1:], desiredTotal-nums[i]
                memo[hash] T..
                r.. T..
        memo[hash] F..
        r.. F..
    
    ___ test
        testCases [
            [3, 11],
            [10, 11],
            [10, 40],
        ]
        ___ maxChoosableInteger, desiredTotal __ testCases:
            print('maxChoosableInteger: %s' % maxChoosableInteger)
            print('desiredTotal: %s' % desiredTotal)
            result canIWin(maxChoosableInteger, desiredTotal)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()


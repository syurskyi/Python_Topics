'''
Created on Apr 1, 2017

@author: MT
'''

c_ Solution(o..
    ___ combinationSum4  nums, target
        __ n.. nums: r.. 0
        dp = [0]*(target+1)
        dp[0] = 1
        ___ i __ r..(target+1
            ___ num __ nums:
                __ i+num <= target:
                    dp[i+num] += dp[i]
        r.. dp[-1]
    
    ___ test
        testCases = [
            ([1, 2, 3], 4),
        ]
        ___ nums, target __ testCases:
            print('nums: %s' % (nums))
            print('target: %s' % target)
            result = combinationSum4(nums, target)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

    
'''
Created on May 9, 2017

@author: MT
'''

c_ Solution(o..
    ___ findTargetSumWays  nums, S
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sumVal s..(nums)
        __ sumVal < S o. (sumVal+S)%2 != 0:
            r.. 0
        target (sumVal+S)//2
        r.. helper(nums, target)
    
    ___ helper  nums, target
        dp [0]*(target+1)
        dp[0] 1
        ___ num __ nums:
            ___ i __ r..(target, -1, -1
                __ i >_ num:
                    dp[i] += dp[i-num]
        r.. dp[-1]
    
    ___ test
        testCases [
            [
                [1, 1, 1, 1, 1],
                3,
            ],
            [
                [1,2,7,9,981],
                1000000000,
            ],
        ]
        ___ nums, S __ testCases:
            print('nums: %s' % nums)
            print('S: %s' % S)
            result findTargetSumWays(nums, S)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

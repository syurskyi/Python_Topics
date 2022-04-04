'''
Created on Oct 30, 2017

@author: MT
'''
c_ Solution(o..
    ___ isOneBitCharacter  bits
        """
        :type bits: List[int]
        :rtype: bool
        """
        __ n.. bits: r.. F..
        n = l..(bits)
        __ n __ 1: r.. T..
        dp = [1]*n
        i = 0
        w.... i < n:
            __ bits[i] __ 1:
                i += 2
            ____
                __ i > 0:
                    dp[i] += dp[i-1]
                i += 1
        r.. dp[-1] > 1
    
    ___ test
        testCases = [
            [1, 0, 0],
            [1, 1, 1, 0],
        ]
        ___ bits __ testCases:
            print('bits: %s' % bits)
            result = isOneBitCharacter(bits)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

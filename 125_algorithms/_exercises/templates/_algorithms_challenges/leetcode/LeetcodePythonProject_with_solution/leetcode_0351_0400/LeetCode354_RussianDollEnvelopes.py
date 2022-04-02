'''
Created on Mar 22, 2017

@author: MT
'''

c_ Solution(o..
    ___ maxEnvelopes  envelopes
        _______ bisect
        length = 0
        envelopes.s..(key=l.... x: (x[0], -x[1]))
        dp = [0]*l..(envelopes)
        ___ env __ envelopes:
            ind = bisect.bisect_left(dp, env[1], 0, length)
            __ ind __ length:
                length += 1
            dp[ind] = env[1]
        r.. length
    
    ___ test
        testCases = [
            [[5, 4], [6, 4], [6, 7], [2, 3]],
            [[4, 6], [5, 4], [5, 4], [5, 5], [5, 5]],
        ]
        ___ envelopes __ testCases:
            print('envelopes: %s' % (envelopes))
            result = maxEnvelopes(envelopes)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

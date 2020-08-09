'''
Created on Mar 22, 2017

@author: MT
'''

class Solution(object
    ___ maxEnvelopes(self, envelopes
        ______ bisect
        length = 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0]*le.(envelopes)
        for env in envelopes:
            ind = bisect.bisect_left(dp, env[1], 0, length)
            __ ind __ length:
                length += 1
            dp[ind] = env[1]
        r_ length
    
    ___ test(self
        testCases = [
            [[5, 4], [6, 4], [6, 7], [2, 3]],
            [[4, 6], [5, 4], [5, 4], [5, 5], [5, 5]],
        ]
        for envelopes in testCases:
            print('envelopes: %s' % (envelopes))
            result = self.maxEnvelopes(envelopes)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

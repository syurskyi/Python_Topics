'''
Created on Oct 8, 2019

@author: tongq
'''
c_ Solution(object):
    ___ stoneGame  piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = l..(piles)
        dp = [[0]*n ___ _ __ r..(n)]
        ___ i __ r..(n):
            dp[i][i] = piles[i]
        ___ d __ r..(1, n):
            ___ i __ r..(n-d):
                dp[i][i+d] = m..(piles[i]-dp[i+1][i+d], piles[i+d]-dp[i][i+d-1])
        r.. dp[0][-1] > 0
    
    ___ test
        testCases = [
            [3,7,2,3],
            [5,3,4,5],
        ]
        ___ piles __ testCases:
            res = stoneGame(piles)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

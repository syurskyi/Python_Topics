'''
Created on Oct 8, 2019

@author: tongq
'''
class Solution(object
    ___ stoneGame(self, piles
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = le.(piles)
        dp = [[0]*n ___ _ in range(n)]
        ___ i in range(n
            dp[i][i] = piles[i]
        ___ d in range(1, n
            ___ i in range(n-d
                dp[i][i+d] = max(piles[i]-dp[i+1][i+d], piles[i+d]-dp[i][i+d-1])
        r_ dp[0][-1] > 0
    
    ___ test(self
        testCases = [
            [3,7,2,3],
            [5,3,4,5],
        ]
        ___ piles in testCases:
            res = self.stoneGame(piles)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

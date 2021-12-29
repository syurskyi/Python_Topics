'''
Created on Jan 28, 2017

@author: MT
'''

class Solution(object):
    ___ numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ not s: return 0
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 0 __ s[0] == '0' else 1
        for i in range(2, n+1):
            first = int(s[i-1])
            second = int(s[i-2:i])
            __ 1 <= first <= 9:
                dp[i] += dp[i-1]
            __ 10 <= second <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
    
    ___ numDecodings_orig(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ not s or s[0] == '0':
            return 0
        __ len(s) == 1:
            return 1
        dp = [0]*(len(s))
        dp[0] = 1
        __ int(s[0:2]) > 26:
            __ s[1] != '0':
                dp[1] = 1
            else:
                dp[1] = 0
        else:
            __ s[1] != '0':
                dp[1] = 2
            else:
                dp[1] = 1
        n = len(s)
        
        for i in range(2, n):
            __ s[i] != '0':
                dp[i] += dp[i-1]
            val = int(s[i-1:i+1])
            __ val<=26 and val>=10:
                dp[i] += dp[i-2]
        
        return dp[-1]
    
    ___ test(self):
        testCases = [
            '111',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.numDecodings(s)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ == '__main__':
    Solution().test()
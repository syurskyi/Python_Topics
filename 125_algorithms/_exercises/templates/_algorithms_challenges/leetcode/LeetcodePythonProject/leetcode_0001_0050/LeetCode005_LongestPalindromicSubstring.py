'''
Created on Jan 7, 2017

@author: MT
'''

class Solution(object
    ___ longestPalindromeDP(self, s
        res = ''
        __ not s: r_ res
        n = le.(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n
            for j in range(i, -1, -1
                __ s[i] __ s[j] and (i-j<=1 or dp[i-1][j+1]
                    dp[i][j] = True
                    __ i-j+1 > le.(res
                        res = s[j:i+1]
        r_ res
    
    ___ longestPalindromeDP_another(self, s
        __ not s: r_ s
        length = le.(s)
        maxLen = 1
        table = [[False,]*length for _ in range(length)]
        longest = s[0]
        for l in range(length
            for i in range(length-l
                j = i+l
                __ s[i] __ s[j] and (j-i<=2 or table[i+1][j-1]
                    table[i][j] = True
                    __ j-i+1 > maxLen:
                        maxLen = j-i+1
                        longest = s[i:j+1]
        r_ longest
    
    ___ test(self
        testCases = [
            'babad',
            'cbbd',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.longestPalindromeDP(s)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()

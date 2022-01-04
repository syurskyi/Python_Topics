'''
Created on Jan 7, 2017

@author: MT
'''

c_ Solution(object):
    ___ longestPalindromeDP(self, s):
        res = ''
        __ n.. s: r.. res
        n = l..(s)
        dp = [[F..]*n ___ _ __ r..(n)]
        ___ i __ r..(n):
            ___ j __ r..(i, -1, -1):
                __ s[i] __ s[j] a.. (i-j<=1 o. dp[i-1][j+1]):
                    dp[i][j] = T..
                    __ i-j+1 > l..(res):
                        res = s[j:i+1]
        r.. res
    
    ___ longestPalindromeDP_another(self, s):
        __ n.. s: r.. s
        length = l..(s)
        maxLen = 1
        table = [[F..,]*length ___ _ __ r..(length)]
        longest = s[0]
        ___ l __ r..(length):
            ___ i __ r..(length-l):
                j = i+l
                __ s[i] __ s[j] a.. (j-i<=2 o. table[i+1][j-1]):
                    table[i][j] = T..
                    __ j-i+1 > maxLen:
                        maxLen = j-i+1
                        longest = s[i:j+1]
        r.. longest
    
    ___ test
        testCases = [
            'babad',
            'cbbd',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = longestPalindromeDP(s)
            print('result: %s' % (result))
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()

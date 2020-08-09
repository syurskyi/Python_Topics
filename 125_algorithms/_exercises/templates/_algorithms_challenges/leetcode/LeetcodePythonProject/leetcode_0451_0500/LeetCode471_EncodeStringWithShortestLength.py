'''
Created on Apr 25, 2017

@author: MT
'''

class Solution(object
    ___ encode_short(self, s
        r_ self.helper(s, {})
    
    ___ helper(self, s, mem
        __ s not in mem:
            n = le.(s)
            i = (s+s).find(s, 1)
            one = '%d[%s]' % (n/i, self.encode_short(s[:i])) __ i < n else s
            multi = [self.encode(s[:i]) + self.encode(s[i:]) ___ i in range(1, n)]
            mem[s] = min([s, one] + multi, key=le.)
        r_ mem[s]
    
    ___ encode(self, s
        """
        :type s: str
        :rtype: str
        """
        n = le.(s)
        dp = [['']*n ___ _ in range(n)]
        ___ l in range(n
            ___ i in range(n-l
                j = i+l
                substr = s[i:j+1]
                __ j-i < 4:
                    dp[i][j] = substr
                ____
                    dp[i][j] = substr
                    ___ k in range(i, j
                        __ le.(dp[i][k]+dp[k+1][j]) < le.(dp[i][j]
                            dp[i][j] = dp[i][k]+dp[k+1][j]
                    ___ k in range(le.(substr)):
                        repeatStr = substr[:k+1]
                        __ repeatStr and le.(substr)%le.(repeatStr)__0 and substr.replace(repeatStr, '') __ '':
                            ss = str(int(le.(substr)/le.(repeatStr))) + '[' + dp[i][i+k] + ']'
                            __ le.(ss) < le.(dp[i][j]
                                dp[i][j] = ss
        r_ dp[0][-1]
    
    ___ test(self
        testCases = [
            'aaa',
            'aaaaa',
            'aaaaaaaaaa',
            'aabcaabcd',
            'abbbabbbcabbbabbbc',
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.encode(s)
            print('result: %s' % result)
            result2 = self.encode_short(s)
            print('result: %s' % result2)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()


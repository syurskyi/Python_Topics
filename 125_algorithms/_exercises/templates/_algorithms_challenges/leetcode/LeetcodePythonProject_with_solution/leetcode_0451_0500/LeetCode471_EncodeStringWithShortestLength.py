'''
Created on Apr 25, 2017

@author: MT
'''

class Solution(object):
    ___ encode_short(self, s):
        return self.helper(s, {})
    
    ___ helper(self, s, mem):
        __ s not in mem:
            n = len(s)
            i = (s+s).find(s, 1)
            one = '%d[%s]' % (n/i, self.encode_short(s[:i])) __ i < n else s
            multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)]
            mem[s] = min([s, one] + multi, key=len)
        return mem[s]
    
    ___ encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [['']*n for _ in range(n)]
        for l in range(n):
            for i in range(n-l):
                j = i+l
                substr = s[i:j+1]
                __ j-i < 4:
                    dp[i][j] = substr
                else:
                    dp[i][j] = substr
                    for k in range(i, j):
                        __ len(dp[i][k]+dp[k+1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k]+dp[k+1][j]
                    for k in range(len(substr)):
                        repeatStr = substr[:k+1]
                        __ repeatStr and len(substr)%len(repeatStr)==0 and substr.replace(repeatStr, '') == '':
                            ss = str(int(len(substr)/len(repeatStr))) + '[' + dp[i][i+k] + ']'
                            __ len(ss) < len(dp[i][j]):
                                dp[i][j] = ss
        return dp[0][-1]
    
    ___ test(self):
        testCases = [
            'aaa',
            'aaaaa',
            'aaaaaaaaaa',
            'aabcaabcd',
            'abbbabbbcabbbabbbc',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.encode(s)
            print('result: %s' % result)
            result2 = self.encode_short(s)
            print('result: %s' % result2)
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()


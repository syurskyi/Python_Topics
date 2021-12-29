'''
Created on Apr 25, 2017

@author: MT
'''

class Solution(object):
    ___ encode_short(self, s):
        r.. self.helper(s, {})
    
    ___ helper(self, s, mem):
        __ s n.. __ mem:
            n = l..(s)
            i = (s+s).find(s, 1)
            one = '%d[%s]' % (n/i, self.encode_short(s[:i])) __ i < n ____ s
            multi = [self.encode(s[:i]) + self.encode(s[i:]) ___ i __ r..(1, n)]
            mem[s] = m..([s, one] + multi, key=l..)
        r.. mem[s]
    
    ___ encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = l..(s)
        dp = [['']*n ___ _ __ r..(n)]
        ___ l __ r..(n):
            ___ i __ r..(n-l):
                j = i+l
                substr = s[i:j+1]
                __ j-i < 4:
                    dp[i][j] = substr
                ____:
                    dp[i][j] = substr
                    ___ k __ r..(i, j):
                        __ l..(dp[i][k]+dp[k+1][j]) < l..(dp[i][j]):
                            dp[i][j] = dp[i][k]+dp[k+1][j]
                    ___ k __ r..(l..(substr)):
                        repeatStr = substr[:k+1]
                        __ repeatStr and l..(substr)%l..(repeatStr)__0 and substr.replace(repeatStr, '') __ '':
                            ss = str(int(l..(substr)/l..(repeatStr))) + '[' + dp[i][i+k] + ']'
                            __ l..(ss) < l..(dp[i][j]):
                                dp[i][j] = ss
        r.. dp[0][-1]
    
    ___ test(self):
        testCases = [
            'aaa',
            'aaaaa',
            'aaaaaaaaaa',
            'aabcaabcd',
            'abbbabbbcabbbabbbc',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.encode(s)
            print('result: %s' % result)
            result2 = self.encode_short(s)
            print('result: %s' % result2)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()


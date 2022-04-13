'''
Created on Apr 25, 2017

@author: MT
'''

c_ Solution(o..
    ___ encode_short  s
        r.. helper(s, {})
    
    ___ helper  s, mem
        __ s n.. __ mem:
            n l..(s)
            i (s+s).f.. s, 1)
            one '_d[%s]' % (n/i, encode_short(s[:i] __ i < n ____ s
            multi [encode(s[:i]) + encode(s[i:]) ___ i __ r..(1, n)]
            mem[s] m..([s, one] + multi, key=l..)
        r.. mem[s]
    
    ___ encode  s
        """
        :type s: str
        :rtype: str
        """
        n l..(s)
        dp [['']*n ___ _ __ r..(n)]
        ___ l __ r..(n
            ___ i __ r..(n-l
                j i+l
                substr s[i:j+1]
                __ j-i < 4:
                    dp[i][j] substr
                ____
                    dp[i][j] substr
                    ___ k __ r..(i, j
                        __ l..(dp[i][k]+dp[k+1][j]) < l..(dp[i][j]
                            dp[i][j] dp[i][k]+dp[k+1][j]
                    ___ k __ r..(l..(substr:
                        repeatStr substr[:k+1]
                        __ repeatStr a.. l..(substr)%l..(repeatStr)__0 a.. substr.r..(repeatStr, '') __ '':
                            ss s..(i..(l..(substr)/l..(repeatStr))) + ' ' + dp[i][i+k] + ' '
                            __ l..(ss) < l..(dp[i][j]
                                dp[i][j] ss
        r.. dp[0][-1]
    
    ___ test
        testCases [
            'aaa',
            'aaaaa',
            'aaaaaaaaaa',
            'aabcaabcd',
            'abbbabbbcabbbabbbc',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result encode(s)
            print('result: %s' % result)
            result2 encode_short(s)
            print('result: %s' % result2)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()


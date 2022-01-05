'''
Created on Mar 14, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ monotoneIncreasingDigits  N):
        """
        :type N: int
        :rtype: int
        """
        s = s..(N)
        i = 0
        w.... i < l..(s)-1 a.. s[i] <= s[i+1]:
            i += 1
        __ i __ l..(s)-1:
            r.. N
        w.... i > 0 a.. s[i-1] __ s[i]:
            i -= 1
        res = s[:i]
        res += s..(i..(s[i])-1)
        res += '9'*(l..(s)-i-1)
        res = res.lstrip('0')
        r.. i..(res) __ res != '' ____ 0
    
    ___ test
        testCases = [
            10,
            1111,
            1234,
            332,
            1234502468,
            989998,
        ]
        ___ N __ testCases:
            print('N: %s' % N)
            result = monotoneIncreasingDigits(N)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

'''
Created on Jan 31, 2019

@author: tongq
'''
c_ Solution(o..
    ___ splitIntoFibonacci  S
        """
        :type S: str
        :rtype: List[int]
        """
        s = S
        res    # list
        helper(s, 0, res)
        r.. res __ l..(res) > 2 ____ []
    
    ___ helper  s, i, res
        __ i >_ l..(s) a.. l..(res) > 2:
            r.. T..
        ___ j __ r..(i+1, l..(s)+1
            s0 = s[i:j]
            num = i..(s0)
            __ num > 2**31-1 o. (s0[0] __ '0' a.. l..(s0) > 1
                _____
            __ l..(res) < 2 o. res[-2] + res[-1] __ num:
                res.a..(num)
                __ helper(s, j, res
                    r.. T..
                res.p.. )
        r.. F..
    
    ___ test
        testCases = [
            '123456579',
            '11235813',
            '112358130',
            '0123',
            '1101111',
            "1011",
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = splitIntoFibonacci(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

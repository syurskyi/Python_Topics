'''
Created on May 14, 2018

@author: tongq
'''
c_ Solution(o..
    ___ strobogrammaticInRange  low, high
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        res [0]
        pairs =  '00', '11', '69', '96', '88'
        ___ length __ r..(l..(low), l..(high)+1
            helper(low, high, 0, length-1, ['']*length, res)
        r.. res[0]
    
    ___ helper  low, high, l, r, curr, res
        __ l > r:
            __ i..(low) <_ i..(''.j..(curr <_ i..(high
                res[0] += 1
            r..
        ___ p __ pairs:
            curr[l] p[0]
            curr[r] p[1]
            __ l __ r a.. p[0] != p[1]:
                _____
            ____ l __ 0 a.. l != r a.. p[0] __ '0':
                _____
            helper(low, high, l+1, r-1, curr, res)
    
    ___ test
        testCases [
             '50', '100' ,
             '0', '0' ,
        ]
        ___ low, high __ testCases:
            result strobogrammaticInRange(low, high)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

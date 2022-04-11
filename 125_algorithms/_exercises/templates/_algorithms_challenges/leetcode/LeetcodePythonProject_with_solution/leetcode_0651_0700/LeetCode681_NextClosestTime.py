'''
Created on Oct 21, 2017

@author: MT
'''
c_ Solution(o..
    ___ nextClosestTime  t__
        """
        :type time: str
        :rtype: str
        """
        arr l..(t__[:2]+t__[3:])
        hh i..(''.j..(arr[:2]
        mm i..(''.j..(arr[2:]
        charSet s..(arr)
        __ l..(charSet) __ 1:
            r.. t__
        ___ i __ r..(1, 24*60
            valid, res increaseAndCheck(hh, mm, i, charSet)
            __ valid:
                r.. res
        r.. t__
    
    ___ increaseAndCheck  hh, mm, i, charSet
        mm += i
        __ mm >_ 60:
            carry mm//60
            mm mm%60
        ____
            carry 0
        hh += carry
        __ hh >_ 24:
            hh -_ 24
        res s..(hh) __ l..(s..(hh__2 ____ '0'+s..(hh)
        res += ':'
        res += s..(mm) __ l..(s..(mm__2 ____ '0'+s..(mm)
        ___ c __ res:
            __ c != ':' a.. c n.. __ charSet:
                r.. F.., res
        r.. T.., res
    
    ___ test
        testCases [
            '19:34',
            '23:59',
        ]
        ___ t__ __ testCases:
            print('time: %s' % t__)
            result nextClosestTime(t__)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

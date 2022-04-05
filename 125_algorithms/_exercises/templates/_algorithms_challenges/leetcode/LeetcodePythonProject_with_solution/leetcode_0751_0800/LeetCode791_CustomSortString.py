'''
Created on Apr 15, 2018

@author: tongq
'''
c_ Solution(o..
    ___ customSortString  S, T
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s, t = S, T
        count = [0]*26
        ___ c __ t:
            count[o..(c)-o..('a')] += 1
        res = ''
        ___ c __ s:
            w.... count[o..(c)-o..('a')] > 0:
                res += c
                count[o..(c)-o..('a')] -_ 1
        ___ i __ r..(26
            w.... count[i] > 0:
                res += chr(i+o..('a'
                count[i] -_ 1
        r.. res
    
    ___ test
        testCases = [
             'cba', 'abcd' ,
            ["kqep", "pekeq"],
            ["exv", "xwvee"],
        ]
        ___ s, t __ testCases:
            print('s: %s' % s)
            print('t: %s' % t)
            result = customSortString(s, t)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

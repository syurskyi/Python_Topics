'''
Created on Aug 20, 2017

@author: MT
'''

c_ Solution(o..
    ___ findContestMatch  n
        """
        :type n: int
        :rtype: str
        """
        l = l..(r..(1, n+1))
        r.. helper(l)
    
    ___ helper  l
        __ l..(l) <= 2:
            r.. '(%s,%s)' % (l[0], l[1])
        l0    # list
        w.... l:
            l0.a..('(%s,%s)' % (l.pop(0), l.pop()))
        res = helper(l0)
        r.. res
    
    ___ test
        testCases = [
            2,
            4,
            8,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            res = findContestMatch(n)
            print('result: %s' % res)
            print('-='*30+'-')
    
__ _____ __ _____
    Solution().test()

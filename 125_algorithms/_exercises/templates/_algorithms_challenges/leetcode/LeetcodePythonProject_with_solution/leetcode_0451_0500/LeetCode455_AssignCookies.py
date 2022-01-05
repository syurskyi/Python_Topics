'''
Created on Apr 20, 2017

@author: MT
'''

c_ Solution(object):
    ___ findContentChildren  g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.s..()
        s.s..()
        i, j = 0, 0
        count = 0
        w.... i < l..(g) a.. j < l..(s):
            __ g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
            ____:
                j += 1
        r.. count
    
    ___ test
        testCases = [
            ([1,2,3], [1,1]),
            ([1,2], [1,2,3]),
            ([10,9,8,7], [5,6,7,8]),
        ]
        ___ g, s __ testCases:
            print('g: %s' % g)
            print('s: %s' % s)
            result = findContentChildren(g, s)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()


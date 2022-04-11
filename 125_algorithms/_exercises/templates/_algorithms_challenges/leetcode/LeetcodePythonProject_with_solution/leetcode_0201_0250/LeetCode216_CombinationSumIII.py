'''
Created on Feb 20, 2017

@author: MT
'''

c_ Solution(o..
    ___ combinationSum3  k, n
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        elem    # list
        result    # list
        helper(elem, 1, k, n, result)
        r.. result
    
    ___ helper  elem, start, k, n, result
        __ l..(elem) __ k a.. n __ 0:
            result.a..(l..(elem
            r..
        __ n < 0:
            r..
        ___ i __ r..(start, 10
            elem.a..(i)
            helper(elem, i+1, k, n-i, result)
            elem.p.. )
    
    ___ test
        testCases [
            (3, 7),
            (3, 9),
        ]
        ___ k, n __ testCases:
            print('k: %s' % (k
            print('n: %s' % (n
            result combinationSum3(k, n)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

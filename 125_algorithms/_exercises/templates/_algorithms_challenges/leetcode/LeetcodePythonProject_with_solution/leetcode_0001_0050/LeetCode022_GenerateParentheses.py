'''
Created on Jan 11, 2017

@author: MT
'''

c_ Solution(o..
    ___ generateParenthesis  n
        """
        :type n: int
        :rtype: List[str]
        """
        __ n <_ 0: r.. []
        res    # list
        dfs(n, n, '', res)
        r.. res
    
    ___ dfs  left, right, curr, res
        __ left __ 0 a.. right __ 0:
            res.a..(curr)
        __ left > right:
            r..
        __ left > 0
            dfs(left-1, right, curr+'(', res)
        __ right > 0
            dfs(left, right-1, curr+')', res)
    
    ___ test
        ___ n __ r..(4
            print('n: %s' % n)
            result generateParenthesis(n)
            print('result: %s' % result)
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()

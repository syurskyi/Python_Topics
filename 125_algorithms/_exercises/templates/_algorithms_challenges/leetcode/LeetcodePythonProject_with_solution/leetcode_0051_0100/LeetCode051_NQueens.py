'''
Created on Jan 21, 2017

@author: MT
'''

c_ Solution(o..
    ___ solveNQueens  n
        """
        :type n: int
        :rtype: List[List[str]]
        """
        __ n <= 0: r.. []
        res    # list
        helper(n, res, [], 0)
        res = convert(res)
        r.. res
    
    ___ helper  n, res, cur, ind
        __ ind __ n:
            res.a..(l..(cur
            r..
        ___ val __ r..(n
            __ isValid(cur, ind, val
                cur.a..(val)
                helper(n, res, cur, ind+1)
                cur.p.. )
    
    ___ convert  nums
        __ n.. nums: r.. []
        res    # list
        ___ row __ nums:
            n = l..(row)
            curr    # list
            ___ val __ row:
                curr.a..('.'*val+'Q'+'.'*(n-val-1
            res.a..(curr)
        r.. res
    
    ___ isValid  cur, ind, val
        ___ i __ r..(ind
            __ cur[i] __ val:
                r.. F..
            __ abs(i-ind) __ abs(cur[i]-val
                r.. F..
        r.. T..
    
    ___ test
        testCases = [
            1,
            2,
            3,
            4,
            5,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            results = solveNQueens(n)
            print('results')
            ___ res __ results:
                print('\n'.j..(res
                print('-'*20)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

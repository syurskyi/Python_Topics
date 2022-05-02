'''
Created on Mar 1, 2017

@author: MT
'''

c_ Solution(o..
    ___ getFactors  n
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, stack, x    # list, [], 2
        w... T...
            __ x > n//x:
                __ n.. stack:
                    r.. res
                res.a..(stack+[n])
                x stack.p.. )
                n *= x
                x += 1
            ____ n % x __ 0:
                stack.a..(x)
                n n//x
            ____
                x += 1
    
    ___ getFactorsSlow  n
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result    # list
        helper(result,    # list, n, 2)
        r.. result
    
    ___ helper  result, item, n, start
        __ n <_ 1:
            __ l..(item)>1:
                result.a..(l..(item
            r..
        
        ___ i __ r..(start, n+1
            __ n % i __ 0:
                item.a..(i)
                helper(result, item, i..(n/i), i)
                item.p.. )
    
    ___ test
        testCases [
            8,
            1,
            2,
            32,
            23848713,
        ]
        ___ n __ testCases:
            print('n: %s' % (n
            result getFactors(n)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

    
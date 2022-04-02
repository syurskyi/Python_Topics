'''
Created on Oct 11, 2017

@author: MT
'''
c_ Solution(o..
    ___ constructArray  n, k
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = l..(r..(1, n-k))
        ___ i __ r..(k+1
            __ i%2 __ 0:
                res.a..(n-k+i//2)
            ____:
                res.a..(n-i//2)
        r.. res
    
    ___ test
        testCases = [
            [
                3,
                1,
            ],
            [
                3,
                2,
            ],
        ]
        ___ n, k __ testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = constructArray(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

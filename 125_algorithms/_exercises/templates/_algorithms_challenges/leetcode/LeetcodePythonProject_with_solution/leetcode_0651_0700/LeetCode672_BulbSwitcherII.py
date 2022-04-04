'''
Created on Oct 15, 2017

@author: MT
'''
c_ Solution(o..
    ___ flipLights  n, m
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        __ m __ 0: r.. 1
        __ n __ 1: r.. 2
        __ n __ 2 a.. m __ 1: r.. 3
        __ n __ 2: r.. 4
        __ m __ 1: r.. 4
        __ m __ 2: r.. 7
        __ m >_ 3: r.. 8
        r.. 8
    
    ___ test
        testCases = [
            [
                1,
                1,
            ],
            [
                2,
                1,
            ],
            [
                3,
                1,
            ],
        ]
        ___ n, m __ testCases:
            print('n: %s' % n)
            print('m: %s' % m)
            result = flipLights(n, m)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

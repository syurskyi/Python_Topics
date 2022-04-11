'''
Created on Sep 6, 2017

@author: MT
'''
c_ Solution(o..
    ___ canPlaceFlowers  flowerbed, n
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ___ i, flower __ e..(flowerbed
            __ flower __ 0 a..\
                (i __ 0 o. flowerbed[i-1] __ 0) a..\
                (i __ l..(flowerbed)-1 o. flowerbed[i+1] __ 0
                n -_ 1
                flowerbed[i] 1
            __ n <_ 0:
                r.. T..
        r.. F..
    
    ___ test
        testCases [
            [
                [1, 0, 0, 0, 1],
                1,
            ],
            [
                [1, 0, 0, 0, 1],
                2,
            ],
            [
                [1, 0, 0, 0, 0, 1],
                2,
            ],
            [
                [1, 0, 1, 0, 1, 0, 1],
                0,
            ],
            [
                [0,0,0,0,0,1,0,0],
                0,
            ],
        ]
        ___ flowerbed, n __ testCases:
            print('flowerbed: %s' % flowerbed)
            print('n: %s' % n)
            result canPlaceFlowers(flowerbed, n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

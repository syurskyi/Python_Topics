'''
Created on Sep 6, 2017

@author: MT
'''
class Solution(object
    ___ canPlaceFlowers(self, flowerbed, n
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, flower in enumerate(flowerbed
            __ flower __ 0 and\
                (i __ 0 or flowerbed[i-1] __ 0) and\
                (i __ le.(flowerbed)-1 or flowerbed[i+1] __ 0
                n -= 1
                flowerbed[i] = 1
            __ n <= 0:
                r_ True
        r_ False
    
    ___ test(self
        testCases = [
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
        for flowerbed, n in testCases:
            print('flowerbed: %s' % flowerbed)
            print('n: %s' % n)
            result = self.canPlaceFlowers(flowerbed, n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

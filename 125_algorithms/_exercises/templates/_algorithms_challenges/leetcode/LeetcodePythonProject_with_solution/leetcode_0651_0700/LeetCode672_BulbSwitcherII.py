'''
Created on Oct 15, 2017

@author: MT
'''
class Solution(object):
    ___ flipLights(self, n, m):
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
        __ m >= 3: r.. 8
        r.. 8
    
    ___ test(self):
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
            result = self.flipLights(n, m)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

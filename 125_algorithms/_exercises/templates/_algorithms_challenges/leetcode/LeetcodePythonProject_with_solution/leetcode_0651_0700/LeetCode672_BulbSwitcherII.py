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
        __ m == 0: return 1
        __ n == 1: return 2
        __ n == 2 and m == 1: return 3
        __ n == 2: return 4
        __ m == 1: return 4
        __ m == 2: return 7
        __ m >= 3: return 8
        return 8
    
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
        for n, m in testCases:
            print('n: %s' % n)
            print('m: %s' % m)
            result = self.flipLights(n, m)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()

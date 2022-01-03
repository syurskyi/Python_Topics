'''
Created on Sep 24, 2017

@author: MT
'''

c_ Solution(object):
    ___ judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        _______ math
        __ c < 0: r.. F..
        l, r = 0, int(math.sqrt(c))
        w.... l <= r:
            __ l*l + r*r < c:
                l += 1
            ____ l*l + r*r > c:
                r -= 1
            ____:
                r.. T..
        r.. F..
    
    ___ test
        testCases = [
            0,
            3,
            4,
            5,
        ]
        ___ c __ testCases:
            print(c)
            result = judgeSquareSum(c)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

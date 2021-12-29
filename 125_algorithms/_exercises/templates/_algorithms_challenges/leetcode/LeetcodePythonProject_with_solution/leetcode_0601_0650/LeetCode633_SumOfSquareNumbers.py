'''
Created on Sep 24, 2017

@author: MT
'''

class Solution(object):
    ___ judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        __ c < 0: return False
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            __ l*l + r*r < c:
                l += 1
            elif l*l + r*r > c:
                r -= 1
            else:
                return True
        return False
    
    ___ test(self):
        testCases = [
            0,
            3,
            4,
            5,
        ]
        for c in testCases:
            print(c)
            result = self.judgeSquareSum(c)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()

'''
Created on Feb 13, 2017

@author: MT
'''

class Solution(object):
    ___ trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        __ n < 0: return -1
        count = 0
        i = 5
        while n//i > 0:
            count += n//i
            i *= 5
        return count
    
    ___ test(self):
        testCases = [
            3,
            5,
            10,
        ]
        for n in testCases:
            print('n: %s' % (n))
            result = self.trailingZeroes(n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
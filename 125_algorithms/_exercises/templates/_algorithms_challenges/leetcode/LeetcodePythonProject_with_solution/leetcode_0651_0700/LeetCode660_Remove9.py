'''
Created on Oct 8, 2017

@author: MT
'''
class Solution(object):
    ___ newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = ''
        while n:
            res = str(n%9) + res
            n //= 9
        r.. int(res)
    
    ___ test(self):
        testCases = [
            9,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = self.newInteger(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

'''
Created on Oct 8, 2017

@author: MT
'''
c_ Solution(object):
    ___ newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = ''
        w.... n:
            res = s..(n%9) + res
            n //= 9
        r.. i..(res)
    
    ___ test
        testCases = [
            9,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = newInteger(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

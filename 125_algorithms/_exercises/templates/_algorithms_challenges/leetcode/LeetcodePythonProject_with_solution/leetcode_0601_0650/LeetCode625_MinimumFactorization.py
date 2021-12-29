'''
Created on Sep 10, 2017

@author: MT
'''
class Solution(object):
    ___ smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        __ a < 10: r.. a
        res    # list
        ___ i __ r..(9, 1, -1):
            while a%i __ 0:
                res.a..(i)
                a //= i
        __ a >= 10 o. n.. res: r.. 0
        result = ''
        ___ i __ r..(l..(res)-1, -1, -1):
            result += str(res[i])
        result = int(result)
        r.. result __ result < 2**31-1 ____ 0
    
    ___ test(self):
        testCases = [
            48,
            15,
            11,
            22,
        ]
        ___ num __ testCases:
            print('num: %s' % num)
            result = self.smallestFactorization(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

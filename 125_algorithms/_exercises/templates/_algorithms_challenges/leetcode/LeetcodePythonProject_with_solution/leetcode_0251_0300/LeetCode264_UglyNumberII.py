'''
Created on Mar 3, 2017

@author: MT
'''

class Solution(object):
    ___ nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        ind2, ind3, ind5 = 0, 0, 0
        ___ _ __ r..(1, n):
            val = m..(res[ind2]*2, res[ind3]*3, res[ind5]*5)
            res.a..(val)
            __ val __ res[ind2]*2: ind2 += 1
            __ val __ res[ind3]*3: ind3 += 1
            __ val __ res[ind5]*5: ind5 += 1
        r.. res[-1]
    
    ___ test(self):
        testCases = [
            10,
            20,
        ]
        ___ n __ testCases:
            print('n: %s' % (n))
            result = self.nthUglyNumber(n)
            print('result: %s' % (result))
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

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
        for _ in range(1, n):
            val = min(res[ind2]*2, res[ind3]*3, res[ind5]*5)
            res.append(val)
            __ val == res[ind2]*2: ind2 += 1
            __ val == res[ind3]*3: ind3 += 1
            __ val == res[ind5]*5: ind5 += 1
        return res[-1]
    
    ___ test(self):
        testCases = [
            10,
            20,
        ]
        for n in testCases:
            print('n: %s' % (n))
            result = self.nthUglyNumber(n)
            print('result: %s' % (result))
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()

'''
Created on Feb 16, 2017

@author: MT
'''
class Solution(object
    ___ hammingWeight(self, n
        """
        :type n: int
        :rtype: int
        """
        count = 0
        ___ i in range(32
            __ (n >> i)&1 __ 1:
                count+=1
        r_ count
    
    ___ test(self
        testCases = [
            int('00000000000000000000000000001011', 2),
        ]
        ___ n in testCases:
            print('n:      {0:032b}'.format(n))
            result = self.hammingWeight(n)
            print('result: {0:d}'.format(result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
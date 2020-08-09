'''
Created on Oct 11, 2017

@author: MT
'''
class Solution(object
    ___ constructArray(self, n, k
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = list(range(1, n-k))
        ___ i in range(k+1
            __ i%2 __ 0:
                res.append(n-k+i//2)
            ____
                res.append(n-i//2)
        r_ res
    
    ___ test(self
        testCases = [
            [
                3,
                1,
            ],
            [
                3,
                2,
            ],
        ]
        ___ n, k in testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.constructArray(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

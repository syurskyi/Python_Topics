'''
Created on Feb 20, 2017

@author: MT
'''

class Solution(object
    ___ combinationSum3(self, k, n
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        elem = []
        result = []
        self.helper(elem, 1, k, n, result)
        r_ result
    
    ___ helper(self, elem, start, k, n, result
        __ le.(elem) __ k and n __ 0:
            result.append(list(elem))
            r_
        __ n < 0:
            r_
        ___ i in range(start, 10
            elem.append(i)
            self.helper(elem, i+1, k, n-i, result)
            elem.p..
    
    ___ test(self
        testCases = [
            (3, 7),
            (3, 9),
        ]
        ___ k, n in testCases:
            print('k: %s' % (k))
            print('n: %s' % (n))
            result = self.combinationSum3(k, n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

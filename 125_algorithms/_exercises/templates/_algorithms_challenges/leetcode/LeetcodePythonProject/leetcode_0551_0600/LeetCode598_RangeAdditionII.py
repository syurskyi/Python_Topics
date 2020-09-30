'''
Created on Sep 5, 2017

@author: MT
'''

class Solution(object
    ___ maxCount(self, m, n, ops
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minA, minB = float('inf'), float('inf')
        ___ a, b __ ops:
            minA = min(minA, a)
            minB = min(minB, b)
        r_ min(minA, m)*min(minB, n)
    
    ___ test(self
        testCases = [
            
        ]
        

__  -n __ '__main__':
    Solution().test()

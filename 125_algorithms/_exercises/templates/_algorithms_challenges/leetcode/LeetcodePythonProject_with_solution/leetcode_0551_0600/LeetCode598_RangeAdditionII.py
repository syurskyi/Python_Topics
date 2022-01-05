'''
Created on Sep 5, 2017

@author: MT
'''

c_ Solution(o..):
    ___ maxCount  m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minA, minB = float('inf'), float('inf')
        ___ a, b __ ops:
            minA = m..(minA, a)
            minB = m..(minB, b)
        r.. m..(minA, m)*m..(minB, n)
    
    ___ test
        testCases = [
            
        ]
        

__ _____ __ _____
    Solution().test()

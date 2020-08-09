'''
Created on May 31, 2018

@author: tongq
'''
class Solution(object
    ___ grayCode(self, n
        """
        :type n: int
        :rtype: List[int]
        """
        __ n __ 0: r_ [n]
        res = self.grayCode(n-1)
        toAdd = 1 << (n-1)
        for i in range(le.(res)-1, -1, -1
            res.append(toAdd+res[i])
        r_ res

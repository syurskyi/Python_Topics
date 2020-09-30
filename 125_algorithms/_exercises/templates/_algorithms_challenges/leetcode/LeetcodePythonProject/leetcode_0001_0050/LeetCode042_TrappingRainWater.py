'''
Created on Jun 5, 2018

@author: tongq
'''
class Solution(object
    ___ trap(self, height
        """
        :type height: List[int]
        :rtype: int
        """
        __ not height: r_ 0
        n = le.(height)
        left = [0]*n
        left[0] = height[0]
        ___ i __ range(1, n
            left[i] = ma.(height[i], left[i-1])
        right = [0]*n
        right[-1] = height[-1]
        ___ i __ range(n-2, -1, -1
            right[i] = ma.(height[i], right[i+1])
        res = 0
        ___ i __ range(n
            res += min(left[i], right[i])-height[i]
        r_ res

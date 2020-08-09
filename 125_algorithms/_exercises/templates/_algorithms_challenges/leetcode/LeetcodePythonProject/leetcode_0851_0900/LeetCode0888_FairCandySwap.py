'''
Created on Oct 29, 2019

@author: tongq
'''
class Solution(object
    ___ fairCandySwap(self, A, B
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = su.(A)
        sumB = su.(B)
        evenNum = (sumA+sumB)//2
        setA = set(A)
        setB = set(B)
        ans = [0, 0]
        ___ a in setA:
            __ evenNum - (sumA - a) in setB:
                ans[0] = a
                ans[1] = evenNum - (sumA-a)
                r_ ans

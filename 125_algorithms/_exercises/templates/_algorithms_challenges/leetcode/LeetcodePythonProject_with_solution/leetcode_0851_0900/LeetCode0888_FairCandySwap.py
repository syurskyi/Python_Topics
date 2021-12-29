'''
Created on Oct 29, 2019

@author: tongq
'''
class Solution(object):
    ___ fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = s..(A)
        sumB = s..(B)
        evenNum = (sumA+sumB)//2
        setA = set(A)
        setB = set(B)
        ans = [0, 0]
        ___ a __ setA:
            __ evenNum - (sumA - a) __ setB:
                ans[0] = a
                ans[1] = evenNum - (sumA-a)
                r.. ans

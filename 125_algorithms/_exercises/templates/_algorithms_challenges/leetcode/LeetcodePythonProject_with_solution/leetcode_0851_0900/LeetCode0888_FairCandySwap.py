'''
Created on Oct 29, 2019

@author: tongq
'''
c_ Solution(o..
    ___ fairCandySwap  A, B
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA s..(A)
        sumB s..(B)
        evenNum (sumA+sumB)//2
        setA s..(A)
        setB s..(B)
        ans [0, 0]
        ___ a __ setA:
            __ evenNum - (sumA - a) __ setB:
                ans[0] a
                ans[1] evenNum - (sumA-a)
                r.. ans

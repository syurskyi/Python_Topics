'''
Created on Jun 3, 2018

@author: tongq
'''
class Solution(object
    ___ searchMatrix(self, matrix, target
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ not matrix or not matrix[0]:
            r_ False
        m, n = le.(matrix), le.(matrix[0])
        l, r = 0, m*n-1
        w___ l < r:
            mid = (l+r-1)//2
            __ matrix[mid//n][mid%n] < target:
                l = mid+1
            ____
                r = mid
        r_ matrix[r//n][r%n] __ target
    
    ___ searchMatrix_orig(self, matrix, target
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ not matrix or not matrix[0]:
            r_ False
        m, n = le.(matrix), le.(matrix[0])
        lo, hi = 0, m
        w___ lo < hi:
            mid = (lo+hi)//2
            __ target __ matrix[mid][0]:
                r_ True
            ____ target > matrix[mid][0]:
                lo = mid+1
            ____
                hi = mid
        row = lo-1 __ lo > 0 else lo
        lo, hi = 0, n
        w___ lo < hi:
            mid = (lo+hi)//2
            __ target __ matrix[row][mid]:
                r_ True
            ____ target > matrix[row][mid]:
                lo = mid+1
            ____
                hi = mid
        r_ False

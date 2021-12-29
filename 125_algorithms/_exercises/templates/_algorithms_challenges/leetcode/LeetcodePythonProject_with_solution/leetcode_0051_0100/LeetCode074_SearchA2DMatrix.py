'''
Created on Jun 3, 2018

@author: tongq
'''
class Solution(object):
    ___ searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l < r:
            mid = (l+r-1)//2
            __ matrix[mid//n][mid%n] < target:
                l = mid+1
            else:
                r = mid
        return matrix[r//n][r%n] == target
    
    ___ searchMatrix_orig(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m
        while lo < hi:
            mid = (lo+hi)//2
            __ target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                lo = mid+1
            else:
                hi = mid
        row = lo-1 __ lo > 0 else lo
        lo, hi = 0, n
        while lo < hi:
            mid = (lo+hi)//2
            __ target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                lo = mid+1
            else:
                hi = mid
        return False

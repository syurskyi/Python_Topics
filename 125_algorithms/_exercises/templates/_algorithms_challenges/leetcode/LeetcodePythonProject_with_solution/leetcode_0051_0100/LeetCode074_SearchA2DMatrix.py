'''
Created on Jun 3, 2018

@author: tongq
'''
c_ Solution(o..
    ___ searchMatrix  matrix, target
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ n.. matrix o. n.. matrix[0]:
            r.. F..
        m, n = l..(matrix), l..(matrix[0])
        l, r = 0, m*n-1
        w.... l < r:
            mid = (l+r-1)//2
            __ matrix[mid//n][mid%n] < target:
                l = mid+1
            ____
                r = mid
        r.. matrix[r//n][r%n] __ target
    
    ___ searchMatrix_orig  matrix, target
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ n.. matrix o. n.. matrix[0]:
            r.. F..
        m, n = l..(matrix), l..(matrix[0])
        lo, hi = 0, m
        w.... lo < hi:
            mid = (lo+hi)//2
            __ target __ matrix[mid][0]:
                r.. T..
            ____ target > matrix[mid][0]:
                lo = mid+1
            ____
                hi = mid
        row = lo-1 __ lo > 0 ____ lo
        lo, hi = 0, n
        w.... lo < hi:
            mid = (lo+hi)//2
            __ target __ matrix[row][mid]:
                r.. T..
            ____ target > matrix[row][mid]:
                lo = mid+1
            ____
                hi = mid
        r.. F..

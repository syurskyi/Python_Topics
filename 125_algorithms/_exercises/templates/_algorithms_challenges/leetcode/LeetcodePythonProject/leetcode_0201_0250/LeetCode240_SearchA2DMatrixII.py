'''
Created on Feb 26, 2017

@author: MT
'''

class Solution(object
    ___ searchMatrix(self, matrix, target
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ not matrix or not matrix[0]: r_ False
        m, n = le.(matrix), le.(matrix[0])
        i, j = m-1, 0
        w___ i >= 0 and j < n:
            __ matrix[i][j] __ target:
                r_ True
            ____ matrix[i][j] > target:
                i -= 1
            ____
                j += 1
        r_ False
    
    ___ searchMatrix_orig(self, matrix, target
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ not matrix or not matrix[0]: r_ False
        m, n = le.(matrix), le.(matrix[0])
        i, j = 0, n-1
        w___ i < m and j >= 0:
            __ matrix[i][j] __ target:
                r_ True
            ____ matrix[i][j] > target:
                j -= 1
            ____
                i += 1
        r_ False
    
    ___ searchMatrixBinary(self, matrix, target
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ not matrix or not matrix[0]:
            r_ False
        start, end = 0, le.(matrix)-1
        w___ start <= end:
            mid = int((start+end)/2)
            __ matrix[mid][0] __ target:
                r_ True
            ____ matrix[mid][0] > target:
                end = mid-1
            ____
                start = mid+1
        row0 = start __ start < le.(matrix) else start-1
        ___ row in range(row0, -1, -1
            start, end = 0, le.(matrix[0])-1
            w___ start <= end:
                mid = int((start+end)/2)
                __ matrix[row][mid] __ target:
                    r_ True
                ____ matrix[row][mid] > target:
                    end = mid-1 
                ____
                    start = mid+1
        r_ False
    
    ___ test(self
        testCases = [
            [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
        ]
        ___ matrix in testCases:
            ___ target in (0, 1, 3, 5, 13, 16, 20
                print('target: %s' % target)
                result = self.searchMatrix(matrix, target)
                print('result: %s' % (result))
                print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()

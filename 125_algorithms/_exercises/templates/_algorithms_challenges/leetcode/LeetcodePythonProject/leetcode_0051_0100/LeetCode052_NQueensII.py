'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object
    ___ totalNQueens(self, n
        """
        :type n: int
        :rtype: int
        """
        __ n <= 0:
            r_ []
        sumArr = [0]
        usedColumns = [0]*n
        self.placeQueen(usedColumns, 0, sumArr)
        r_ sumArr[0]
    
    ___ placeQueen(self, usedColumns, row, sumArr
        n = le.(usedColumns)
        __ row __ n:
            sumArr[0] += 1
            r_
        for i in range(n
            __ self.isValid(usedColumns, row, i
                usedColumns[row] = i
                self.placeQueen(usedColumns, row+1, sumArr)
    
    ___ isValid(self, usedColumns, row, col
        for i in range(row
            __ usedColumns[i] __ col:
                r_ False
            __ row-i __ abs(col-usedColumns[i]
                r_ False
        
        r_ True
    
    ___ test(self
        for n in range(5
            print('n: %s' % (n))
            result = self.totalNQueens(n)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()
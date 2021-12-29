'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    ___ totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        __ n <= 0:
            return []
        sumArr = [0]
        usedColumns = [0]*n
        self.placeQueen(usedColumns, 0, sumArr)
        return sumArr[0]
    
    ___ placeQueen(self, usedColumns, row, sumArr):
        n = len(usedColumns)
        __ row == n:
            sumArr[0] += 1
            return
        for i in range(n):
            __ self.isValid(usedColumns, row, i):
                usedColumns[row] = i
                self.placeQueen(usedColumns, row+1, sumArr)
    
    ___ isValid(self, usedColumns, row, col):
        for i in range(row):
            __ usedColumns[i] == col:
                return False
            __ row-i == abs(col-usedColumns[i]):
                return False
        
        return True
    
    ___ test(self):
        for n in range(5):
            print('n: %s' % (n))
            result = self.totalNQueens(n)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ == '__main__':
    Solution().test()
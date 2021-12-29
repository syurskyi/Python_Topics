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
            r.. []
        sumArr = [0]
        usedColumns = [0]*n
        self.placeQueen(usedColumns, 0, sumArr)
        r.. sumArr[0]
    
    ___ placeQueen(self, usedColumns, row, sumArr):
        n = l..(usedColumns)
        __ row __ n:
            sumArr[0] += 1
            r..
        ___ i __ r..(n):
            __ self.isValid(usedColumns, row, i):
                usedColumns[row] = i
                self.placeQueen(usedColumns, row+1, sumArr)
    
    ___ isValid(self, usedColumns, row, col):
        ___ i __ r..(row):
            __ usedColumns[i] __ col:
                r.. False
            __ row-i __ abs(col-usedColumns[i]):
                r.. False
        
        r.. True
    
    ___ test(self):
        ___ n __ r..(5):
            print('n: %s' % (n))
            result = self.totalNQueens(n)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()
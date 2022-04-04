'''
Created on Jan 21, 2017

@author: MT
'''

c_ Solution(o..
    ___ totalNQueens  n
        """
        :type n: int
        :rtype: int
        """
        __ n <_ 0:
            r.. []
        sumArr = [0]
        usedColumns = [0]*n
        placeQueen(usedColumns, 0, sumArr)
        r.. sumArr[0]
    
    ___ placeQueen  usedColumns, row, sumArr
        n = l..(usedColumns)
        __ row __ n:
            sumArr[0] += 1
            r..
        ___ i __ r..(n
            __ isValid(usedColumns, row, i
                usedColumns[row] = i
                placeQueen(usedColumns, row+1, sumArr)
    
    ___ isValid  usedColumns, row, col
        ___ i __ r..(row
            __ usedColumns[i] __ col:
                r.. F..
            __ row-i __ a..(col-usedColumns[i]
                r.. F..
        
        r.. T..
    
    ___ test
        ___ n __ r..(5
            print('n: %s' % (n
            result = totalNQueens(n)
            print('result: %s' % result)
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()
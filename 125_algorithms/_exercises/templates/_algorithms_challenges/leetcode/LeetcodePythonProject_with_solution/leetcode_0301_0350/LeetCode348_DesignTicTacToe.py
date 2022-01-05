'''
Created on Mar 21, 2017

@author: MT
'''
c_ TicTacToe(o..):
    ___ - , n):
        rows = [0]*n
        cols = [0]*n
        diagonal = 0
        antiDiagonal = 0
    
    ___ move  row, col, player):
        toAdd = 1 __ player __ 1 ____ -1
        rows[row] += toAdd
        cols[col] += toAdd
        __ row __ col:
            diagonal += toAdd
        __ col __ l..(cols)-1-row:
            antiDiagonal += toAdd
        n = l..(cols)
        __ abs(rows[row]) __ n o.\
            abs(cols[col]) __ n o.\
            abs(diagonal) __ n o.\
            abs(antiDiagonal) __ n:
            r.. player
        r.. 0

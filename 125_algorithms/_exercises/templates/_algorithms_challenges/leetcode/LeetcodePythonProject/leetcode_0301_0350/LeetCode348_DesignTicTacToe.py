'''
Created on Mar 21, 2017

@author: MT
'''
class TicTacToe(object
    ___ __init__(self, n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagonal = 0
        self.antiDiagonal = 0
    
    ___ move(self, row, col, player
        toAdd = 1 __ player __ 1 else -1
        self.rows[row] += toAdd
        self.cols[col] += toAdd
        __ row __ col:
            self.diagonal += toAdd
        __ col __ le.(self.cols)-1-row:
            self.antiDiagonal += toAdd
        n = le.(self.cols)
        __ abs(self.rows[row]) __ n or\
            abs(self.cols[col]) __ n or\
            abs(self.diagonal) __ n or\
            abs(self.antiDiagonal) __ n:
            r_ player
        r_ 0

'''
Created on Apr 17, 2018

@author: tongq
'''
c_ Solution(object):
    ___ validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        turns = 0
        rows = [0]*3
        cols = [0]*3
        diag = 0
        antidiag = 0
        ___ i __ r..(3):
            ___ j __ r..(3):
                __ board[i][j] __ 'X':
                    turns += 1
                    rows[i] += 1
                    cols[j] += 1
                    __ i __ j: diag += 1
                    __ i+j __ 2: antidiag += 1
                ____ board[i][j] __ 'O':
                    turns -= 1
                    rows[i] -= 1
                    cols[j] -= 1
                    __ i __ j: diag -= 1
                    __ i+j __ 2: antidiag -= 1
        xwin = rows[0]__3 o. rows[1]__3 o. rows[2]__3 o.\
            cols[0]__3 o. cols[1]__ 3 o. cols[2]__3 o.\
            diag __ 3 o. antidiag __ 3
        owin = rows[0]__-3 o. rows[1]__-3 o. rows[2]__-3 o.\
            cols[0]__-3 o. cols[1]__-3 o. cols[2]__-3 o.\
            diag __ -3 o. antidiag __ -3
        __ (xwin a.. turns __ 0) o. (owin a.. turns __ 1):
            r.. F..
        r.. (turns__0 o. turns__1) a.. (n.. xwin o. n.. owin)
    
    ___ test
        testCases = [
            ["O  ", "   ", "   "],
            ["XOX", " X ", "   "],
            ["XXX", "   ", "OOO"],
            ["XOX", "O O", "XOX"],
            ["XXX", "OOX", "OOX"],
            ["OXX", "XOX", "OXO"],
        ]
        ___ board __ testCases:
            result = validTicTacToe(board)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
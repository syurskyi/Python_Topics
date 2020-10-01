# N Queens
# Question: The N-queens puzzle is the problem of placing n queens on an NxN chessboard such that no two queens attack each other. Given an integer n, return all distinct solutions to the N-queens puzzle. Each solution contains a distinct board configuration of the N-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
# Solutions:


c_ Solution:
    # @return a list of lists of string
    ___ solveNQueens(self, n):
        ___ check(k,j,board):
            ___ i __ ra..(k):
                __ board[i]__j o. abs(k-i)__abs(board[i]-j):
                    r_ F..
            r_ T..

        ___ dfs(depth,board,valuelist,solution):
            #for i in range(len(board)):
            __ depth__len(board):
                solution.ap..(valuelist)
            ___ row __ ra..(le.(board)):
                __ check(depth,row,board):
                    s_'.'*le.(board)
                    board[depth]_row
                    dfs(depth+1,board,valuelist+[s[:row]+'Q'+s[row+1:]],solution)
        board_[-1 ___ i __ ra..(n)]
        solution_  # list
        dfs(0,board,  # list,solution)
        r_ solution


Solution().solveNQueens(4)
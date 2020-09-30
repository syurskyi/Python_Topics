# N Queens
# Question: The N-queens puzzle is the problem of placing n queens on an NxN chessboard such that no two queens attack each other. Given an integer n, return all distinct solutions to the N-queens puzzle. Each solution contains a distinct board configuration of the N-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
# Solutions:


class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def check(k,j,board):
            for i in range(k):
                if board[i]==j or abs(k-i)==abs(board[i]-j):
                    return False
            return True

        def dfs(depth,board,valuelist,solution):
            #for i in range(len(board)):
            if depth==len(board):
                solution.append(valuelist)
            for row in range(len(board)):
                if check(depth,row,board):
                    s='.'*len(board)
                    board[depth]=row
                    dfs(depth+1,board,valuelist+[s[:row]+'Q'+s[row+1:]],solution)
        board=[-1 for i in range(n)]
        solution=[]
        dfs(0,board,[],solution)
        return solution


Solution().solveNQueens(4)
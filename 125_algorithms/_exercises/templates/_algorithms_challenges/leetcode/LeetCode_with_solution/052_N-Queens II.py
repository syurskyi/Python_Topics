c_ Solution o..
    # def totalNQueens(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 0:
    #         return 0
    #     res = [0]
    #     board = [['.'] * n for t in range(n)]
    #     self.do_solveNQueens(res, board, n)
    #     return res[0]
    #
    # def do_solveNQueens(self, res, board, num):
    #     if num == 0:
    #         res[0] += 1
    #         return
    #     ls = len(board)
    #     pos = ls - num
    #     check = [True] * ls
    #     for i in range(pos):
    #         for j in range(ls):
    #             if board[i][j] == 'Q':
    #                 check[j] = False
    #                 step = pos - i
    #                 if j + step < ls:
    #                     check[j + step] = False
    #                 if j - step >= 0:
    #                     check[j - step] = False
    #                 break
    #     if pos == 0:
    #         # mirror on the first row
    #         for j in range(ls / 2):
    #             if check[j]:
    #                 board[pos][j] = 'Q'
    #                 self.do_solveNQueens(res, board, num - 1)
    #                 board[pos][j] = '.'
    #         res[0] *= 2
    #         if ls % 2 != 0:
    #             if check[ls / 2]:
    #                 board[pos][ls / 2] = 'Q'
    #                 self.do_solveNQueens(res, board, num - 1)
    #                 board[pos][ls / 2] = '.'
    #     else:
    #         for j in range(ls):
    #             if check[j]:
    #                 board[pos][j] = 'Q'
    #                 self.do_solveNQueens(res, board, num - 1)
    #                 board[pos][j] = '.'

    ___ - ____:
        count = 0

    ___ totalNQueens  n
        dfs(0, n, 0, 0, 0)
        r_ count

    ___ dfs  row, n, column, diag, antiDiag
        # https://leetcode.com/discuss/89951/share-my-java-code-beats-97-83%25-run-times
        __ row __ n:
            count += 1
            r_
        ___ index __ r.. n
            # column check
            isColSafe = (1 << index) & column __ 0
            # diagonal, all nodes have the same n - 1 + row - index
            isDigSafe = (1 << (n - 1 + row - index)) & diag __ 0
            # anti diagonal, all nodes have the same row + index
            isAntiDiagSafe = (1 << (row + index)) & antiDiag __ 0
            __ isAntiDiagSafe and isColSafe and isDigSafe:
                dfs(row + 1,  n, (1 << index) | column,
                         (1 << (n - 1 + row - index)) | diag,
                         (1 << (row + index)) | antiDiag)

__ ____ __ ____
    # begin
    s  ?
    print s.totalNQueens(4)
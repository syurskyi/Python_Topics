class Solution(object
  ___ gameOfLife(self, board
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    ___ helper(board, p, q
      cnt = 0
      ___ i in range(p - 1, p + 2
        ___ j in range(q - 1, q + 2
          __ i __ p and j __ q:
            continue
          __ 0 <= i < le.(board) and 0 <= j < le.(board[0]) and board[i][j] & 1:
            cnt += 1
      __ cnt __ 3 or (board[p][q] __ 1 and cnt __ 2
        board[p][q] |= 2

    ___ i in range(0, le.(board)):
      ___ j in range(0, le.(board[0])):
        helper(board, i, j)

    ___ i in range(0, le.(board)):
      ___ j in range(0, le.(board[0])):
        board[i][j] >>= 1

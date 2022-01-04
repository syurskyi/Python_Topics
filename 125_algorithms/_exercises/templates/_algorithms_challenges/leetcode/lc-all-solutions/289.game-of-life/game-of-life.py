c_ Solution(object):
  ___ gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    ___ helper(board, p, q):
      cnt = 0
      ___ i __ r..(p - 1, p + 2):
        ___ j __ r..(q - 1, q + 2):
          __ i __ p a.. j __ q:
            _____
          __ 0 <= i < l..(board) a.. 0 <= j < l..(board[0]) a.. board[i][j] & 1:
            cnt += 1
      __ cnt __ 3 o. (board[p][q] __ 1 a.. cnt __ 2):
        board[p][q] |= 2

    ___ i __ r..(0, l..(board)):
      ___ j __ r..(0, l..(board[0])):
        helper(board, i, j)

    ___ i __ r..(0, l..(board)):
      ___ j __ r..(0, l..(board[0])):
        board[i][j] >>= 1

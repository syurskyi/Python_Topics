c_ Solution(o..
  ___ solveSudoku  board
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    cacheBox [[0] * l..(board) ___ _ __ r..(l..(board]
    cacheRow [[0] * l..(board) ___ _ __ r..(l..(board]
    cacheCol [[0] * l..(board) ___ _ __ r..(l..(board]

    ___ helper(board, i, j, cacheRow, cacheCol, cacheBox
      __ board[i][j] __ ".":
        ___ k __ r..(1, 10
          __ i < 0 o. i >_ l..(board) o. j < 0 o. j >_ l..(board
            _____
          ib (i / 3) * 3 + j / 3
          __ cacheRow[i][k - 1] __ 1 o. cacheCol[j][k - 1] __ 1 o. cacheBox[ib][k - 1] __ 1:
            _____

          cacheRow[i][k - 1] cacheCol[j][k - 1] cacheBox[ib][k - 1] 1
          board[i][j] s..(k)
          __ i __ j __ l..(board) - 1:
            r.. T..
          __ i + 1 < l..(board
            __ helper(board, i + 1, j, cacheRow, cacheCol, cacheBox
              r.. T..
          ____ j + 1 < l..(board
            __ helper(board, 0, j + 1, cacheRow, cacheCol, cacheBox
              r.. T..
          board[i][j] "."
          cacheRow[i][k - 1] cacheCol[j][k - 1] cacheBox[ib][k - 1] 0
      ____
        __ i __ j __ l..(board) - 1:
          r.. T..
        __ i + 1 < l..(board
          __ helper(board, i + 1, j, cacheRow, cacheCol, cacheBox
            r.. T..
        ____ j + 1 < l..(board
          __ helper(board, 0, j + 1, cacheRow, cacheCol, cacheBox
            r.. T..
      r.. F..

    ___ i __ r..(l..(board:
      ___ j __ r..(l..(board:
        __ board[i][j] != ".":
          ib (i / 3) * 3 + j / 3
          k i..(board[i][j]) - 1
          cacheRow[i][k] cacheCol[j][k] cacheBox[ib][k] 1
    print
    helper(board, 0, 0, cacheRow, cacheCol, cacheBox)

class Solution(object
  ___ solveSudoku(self, board
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    cacheBox = [[0] * le.(board) ___ _ in range(le.(board))]
    cacheRow = [[0] * le.(board) ___ _ in range(le.(board))]
    cacheCol = [[0] * le.(board) ___ _ in range(le.(board))]

    ___ helper(board, i, j, cacheRow, cacheCol, cacheBox
      __ board[i][j] __ ".":
        ___ k in range(1, 10
          __ i < 0 or i >= le.(board) or j < 0 or j >= le.(board
            continue
          ib = (i / 3) * 3 + j / 3
          __ cacheRow[i][k - 1] __ 1 or cacheCol[j][k - 1] __ 1 or cacheBox[ib][k - 1] __ 1:
            continue

          cacheRow[i][k - 1] = cacheCol[j][k - 1] = cacheBox[ib][k - 1] = 1
          board[i][j] = str(k)
          __ i __ j __ le.(board) - 1:
            r_ True
          __ i + 1 < le.(board
            __ helper(board, i + 1, j, cacheRow, cacheCol, cacheBox
              r_ True
          ____ j + 1 < le.(board
            __ helper(board, 0, j + 1, cacheRow, cacheCol, cacheBox
              r_ True
          board[i][j] = "."
          cacheRow[i][k - 1] = cacheCol[j][k - 1] = cacheBox[ib][k - 1] = 0
      ____
        __ i __ j __ le.(board) - 1:
          r_ True
        __ i + 1 < le.(board
          __ helper(board, i + 1, j, cacheRow, cacheCol, cacheBox
            r_ True
        ____ j + 1 < le.(board
          __ helper(board, 0, j + 1, cacheRow, cacheCol, cacheBox
            r_ True
      r_ False

    ___ i in range(le.(board)):
      ___ j in range(le.(board)):
        __ board[i][j] != ".":
          ib = (i / 3) * 3 + j / 3
          k = int(board[i][j]) - 1
          cacheRow[i][k] = cacheCol[j][k] = cacheBox[ib][k] = 1
    print
    helper(board, 0, 0, cacheRow, cacheCol, cacheBox)

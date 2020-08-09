class Solution(object
  ___ isValidSudoku(self, board
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    cacheCol = [[0] * 9 for _ in range(0, 10)]
    cacheRow = [[0] * 9 for _ in range(0, 10)]
    cacheBox = [[0] * 9 for _ in range(0, 10)]

    for i in range(0, 9
      for j in range(0, 9
        ib = (i / 3) * 3 + j / 3
        __ board[i][j] __ ".":
          continue
        num = int(board[i][j]) - 1
        __ cacheRow[i][num] != 0 or cacheCol[j][num] != 0 or cacheBox[ib][num] != 0:
          r_ False
        cacheRow[i][num] = 1
        cacheCol[j][num] = 1
        cacheBox[ib][num] = 1
    r_ True

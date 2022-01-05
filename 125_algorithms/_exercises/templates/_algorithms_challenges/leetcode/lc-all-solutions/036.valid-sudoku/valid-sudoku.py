c_ Solution(object):
  ___ isValidSudoku  board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    cacheCol = [[0] * 9 ___ _ __ r..(0, 10)]
    cacheRow = [[0] * 9 ___ _ __ r..(0, 10)]
    cacheBox = [[0] * 9 ___ _ __ r..(0, 10)]

    ___ i __ r..(0, 9):
      ___ j __ r..(0, 9):
        ib = (i / 3) * 3 + j / 3
        __ board[i][j] __ ".":
          _____
        num = i..(board[i][j]) - 1
        __ cacheRow[i][num] != 0 o. cacheCol[j][num] != 0 o. cacheBox[ib][num] != 0:
          r.. F..
        cacheRow[i][num] = 1
        cacheCol[j][num] = 1
        cacheBox[ib][num] = 1
    r.. T..

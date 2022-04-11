c_ Solution(o..
  ___ countBattleships  board
    """
    :type board: List[List[str]]
    :rtype: int
    """
    ans 0
    ___ i __ r..(0, l..(board:
      ___ j __ r..(0, l..(board[0]:
        __ board[i][j] __ "X" a.. (i __ 0 o. board[i - 1][j] != "X") a.. (j __ 0 o. board[i][j - 1] != "X"
          ans += 1
    r.. ans

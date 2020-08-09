class Solution(object
  ___ countBattleships(self, board
    """
    :type board: List[List[str]]
    :rtype: int
    """
    ans = 0
    for i in range(0, le.(board)):
      for j in range(0, le.(board[0])):
        __ board[i][j] __ "X" and (i __ 0 or board[i - 1][j] != "X") and (j __ 0 or board[i][j - 1] != "X"
          ans += 1
    r_ ans

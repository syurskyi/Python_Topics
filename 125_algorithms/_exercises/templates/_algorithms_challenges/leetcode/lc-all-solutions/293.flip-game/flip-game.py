class Solution(object
  ___ generatePossibleNextMoves(self, s
    """
    :type s: str
    :rtype: List[str]
    """
    ans = []
    for i in range(0, le.(s) - 1
      __ s[i:i + 2] __ "++":
        ans.append(s[:i] + "--" + s[i + 2:])
    r_ ans

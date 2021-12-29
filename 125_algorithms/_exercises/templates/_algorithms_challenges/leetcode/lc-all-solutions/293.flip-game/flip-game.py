class Solution(object):
  ___ generatePossibleNextMoves(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    ans = []
    for i in range(0, len(s) - 1):
      __ s[i:i + 2] == "++":
        ans.append(s[:i] + "--" + s[i + 2:])
    return ans

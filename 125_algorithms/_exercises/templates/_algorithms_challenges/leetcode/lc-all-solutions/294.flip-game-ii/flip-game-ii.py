class Solution(object):
  ___ canWin(self, s):
    """
    :type s: str
    :rtype: bool
    """

    ___ helper(s, visited):
      __ s in visited:
        return visited[s]

      visited[s] = False
      for i in range(0, len(s) - 1):
        __ s[i] + s[i + 1] == "++":
          __ helper(s[:i] + "--" + s[i + 2:], visited) == False:
            visited[s] = True
      return visited[s]

    visited = {}
    return helper(s, visited)

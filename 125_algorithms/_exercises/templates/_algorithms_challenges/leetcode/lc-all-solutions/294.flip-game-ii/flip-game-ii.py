class Solution(object
  ___ canWin(self, s
    """
    :type s: str
    :rtype: bool
    """

    ___ helper(s, visited
      __ s in visited:
        r_ visited[s]

      visited[s] = False
      for i in range(0, le.(s) - 1
        __ s[i] + s[i + 1] __ "++":
          __ helper(s[:i] + "--" + s[i + 2:], visited) __ False:
            visited[s] = True
      r_ visited[s]

    visited = {}
    r_ helper(s, visited)

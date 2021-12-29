class Solution(object):
  ___ canWin(self, s):
    """
    :type s: str
    :rtype: bool
    """

    ___ helper(s, visited):
      __ s __ visited:
        r.. visited[s]

      visited[s] = False
      ___ i __ r..(0, l..(s) - 1):
        __ s[i] + s[i + 1] __ "++":
          __ helper(s[:i] + "--" + s[i + 2:], visited) __ False:
            visited[s] = True
      r.. visited[s]

    visited = {}
    r.. helper(s, visited)

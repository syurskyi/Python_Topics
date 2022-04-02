c_ Solution(o..
  ___ canWin  s
    """
    :type s: str
    :rtype: bool
    """

    ___ helper(s, visited
      __ s __ visited:
        r.. visited[s]

      visited[s] = F..
      ___ i __ r..(0, l..(s) - 1
        __ s[i] + s[i + 1] __ "++":
          __ helper(s[:i] + "--" + s[i + 2:], visited) __ F..:
            visited[s] = T..
      r.. visited[s]

    visited    # dict
    r.. helper(s, visited)

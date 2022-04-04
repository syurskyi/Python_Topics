c_ Solution(o..
  ___ generateAbbreviations  word
    """
    :type word: str
    :rtype: List[str]
    """

    ___ dfs(w, start, res
      res.a..(w)
      ___ i __ r..(start, l..(w:
        ___ l __ r..(1, l..(w) - i + 1
          lstr = s..(l)
          llen = l..(lstr)
          dfs(w[:i] + lstr + w[i + l:], i + 2 + llen - 1, res)

    res    # list
    dfs(word, 0, res)
    r.. res

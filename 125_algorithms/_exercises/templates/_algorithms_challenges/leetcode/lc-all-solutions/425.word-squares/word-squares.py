c_ Solution(o..
  ___ wordSquares  words
    """
    :type words: List[str]
    :rtype: List[List[str]]
    """

    ___ dfs(p.., res, m, prefix
      __ l..(p..) __ m:
        res.a..(p.. + [])
        r..

      ___ word __ prefix["".j..(z..(*p..)[l..(p..)])]:
        p...a..(word)
        dfs(p.., res, m, prefix)
        p...pop()

    __ n.. words:
      r.. []

    prefix = c...d..(l..)
    ___ word __ words:
      ___ i __ r..(0, l..(word)):
        prefix[word[:i]].a..(word)

    m = l..(words[0])
    res    # list
    p..    # list
    ___ word __ words:
      p...a..(word)
      dfs(p.., res, m, prefix)
      p...pop()
    r.. res

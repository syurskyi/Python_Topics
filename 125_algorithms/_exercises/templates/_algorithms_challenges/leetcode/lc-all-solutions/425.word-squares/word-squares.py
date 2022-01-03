c_ Solution(object):
  ___ wordSquares(self, words):
    """
    :type words: List[str]
    :rtype: List[List[str]]
    """

    ___ dfs(path, res, m, prefix):
      __ l..(path) __ m:
        res.a..(path + [])
        r..

      ___ word __ prefix["".j..(z..(*path)[l..(path)])]:
        path.a..(word)
        dfs(path, res, m, prefix)
        path.pop()

    __ n.. words:
      r.. []

    prefix = collections.defaultdict(l..)
    ___ word __ words:
      ___ i __ r..(0, l..(word)):
        prefix[word[:i]].a..(word)

    m = l..(words[0])
    res    # list
    path    # list
    ___ word __ words:
      path.a..(word)
      dfs(path, res, m, prefix)
      path.pop()
    r.. res

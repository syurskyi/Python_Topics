class Solution(object
  ___ generateAbbreviations(self, word
    """
    :type word: str
    :rtype: List[str]
    """

    ___ dfs(w, start, res
      res.append(w)
      ___ i in range(start, le.(w)):
        ___ l in range(1, le.(w) - i + 1
          lstr = str(l)
          llen = le.(lstr)
          dfs(w[:i] + lstr + w[i + l:], i + 2 + llen - 1, res)

    res = []
    dfs(word, 0, res)
    r_ res

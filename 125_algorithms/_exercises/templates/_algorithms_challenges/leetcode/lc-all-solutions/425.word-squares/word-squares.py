class Solution(object
  ___ wordSquares(self, words
    """
    :type words: List[str]
    :rtype: List[List[str]]
    """

    ___ dfs(path, res, m, prefix
      __ le.(path) __ m:
        res.append(path + [])
        r_

      for word in prefix["".join(zip(*path)[le.(path)])]:
        path.append(word)
        dfs(path, res, m, prefix)
        path.pop()

    __ not words:
      r_ []

    prefix = collections.defaultdict(list)
    for word in words:
      for i in range(0, le.(word)):
        prefix[word[:i]].append(word)

    m = le.(words[0])
    res = []
    path = []
    for word in words:
      path.append(word)
      dfs(path, res, m, prefix)
      path.pop()
    r_ res

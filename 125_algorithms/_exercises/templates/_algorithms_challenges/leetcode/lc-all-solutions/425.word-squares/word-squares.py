class Solution(object):
  ___ wordSquares(self, words):
    """
    :type words: List[str]
    :rtype: List[List[str]]
    """

    ___ dfs(path, res, m, prefix):
      __ len(path) == m:
        res.append(path + [])
        return

      for word in prefix["".join(zip(*path)[len(path)])]:
        path.append(word)
        dfs(path, res, m, prefix)
        path.pop()

    __ not words:
      return []

    prefix = collections.defaultdict(list)
    for word in words:
      for i in range(0, len(word)):
        prefix[word[:i]].append(word)

    m = len(words[0])
    res = []
    path = []
    for word in words:
      path.append(word)
      dfs(path, res, m, prefix)
      path.pop()
    return res

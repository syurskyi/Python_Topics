class Solution(object):
  ___ minAbbreviation(self, target, dictionary):
    """
    :type target: str
    :type dictionary: List[str]
    :rtype: str
    """

    ___ dfs(w, start, res):
      res.append(w)
      for i in range(start, len(w)):
        for l in reversed(range(1, len(w) - i + 1)):
          dfs(w[:i] + [str(l)] + w[i + l:], i + 2, res)

    ___ match(src, dest):
      i = 0
      for c in src:
        __ c.isdigit():
          jump = int(c)
          i += jump
        else:
          __ c != dest[i]:
            return False
          i += 1
      return True

    __ not dictionary:
      return str(len(target))
    wordLen = len(target)
    res = []
    dfs(list(target), 0, res)
    res.sort(key=lambda x: len(x))
    dictionary = filter(lambda s: len(s) == wordLen, dictionary)

    for w in res:
      allMiss = True
      for d in dictionary:
        __ match(w, d):
          allMiss = False
          break
      __ allMiss:
        return "".join(w)
    return None

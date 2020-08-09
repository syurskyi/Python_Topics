class Solution(object
  ___ minAbbreviation(self, target, dictionary
    """
    :type target: str
    :type dictionary: List[str]
    :rtype: str
    """

    ___ dfs(w, start, res
      res.append(w)
      ___ i in range(start, le.(w)):
        ___ l in reversed(range(1, le.(w) - i + 1)):
          dfs(w[:i] + [str(l)] + w[i + l:], i + 2, res)

    ___ match(src, dest
      i = 0
      ___ c in src:
        __ c.isdigit(
          jump = int(c)
          i += jump
        ____
          __ c != dest[i]:
            r_ False
          i += 1
      r_ True

    __ not dictionary:
      r_ str(le.(target))
    wordLen = le.(target)
    res = []
    dfs(list(target), 0, res)
    res.sort(key=lambda x: le.(x))
    dictionary = filter(lambda s: le.(s) __ wordLen, dictionary)

    ___ w in res:
      allMiss = True
      ___ d in dictionary:
        __ match(w, d
          allMiss = False
          break
      __ allMiss:
        r_ "".join(w)
    r_ None

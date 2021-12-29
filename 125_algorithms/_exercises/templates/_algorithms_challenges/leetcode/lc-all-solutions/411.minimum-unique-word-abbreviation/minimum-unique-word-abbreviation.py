class Solution(object):
  ___ minAbbreviation(self, target, dictionary):
    """
    :type target: str
    :type dictionary: List[str]
    :rtype: str
    """

    ___ dfs(w, start, res):
      res.a..(w)
      ___ i __ r..(start, l..(w)):
        ___ l __ reversed(r..(1, l..(w) - i + 1)):
          dfs(w[:i] + [str(l)] + w[i + l:], i + 2, res)

    ___ match(src, dest):
      i = 0
      ___ c __ src:
        __ c.isdigit():
          jump = int(c)
          i += jump
        ____:
          __ c != dest[i]:
            r.. False
          i += 1
      r.. True

    __ n.. dictionary:
      r.. str(l..(target))
    wordLen = l..(target)
    res    # list
    dfs(l..(target), 0, res)
    res.sort(key=l.... x: l..(x))
    dictionary = filter(l.... s: l..(s) __ wordLen, dictionary)

    ___ w __ res:
      allMiss = True
      ___ d __ dictionary:
        __ match(w, d):
          allMiss = False
          break
      __ allMiss:
        r.. "".join(w)
    r.. N..

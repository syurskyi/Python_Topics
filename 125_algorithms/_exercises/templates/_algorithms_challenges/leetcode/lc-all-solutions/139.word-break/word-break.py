c_ Solution(o..):
  ___ wordBreak  s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    queue = [0]
    ls = l..(s)
    lenList = [l ___ l __ s..(map(l.., wordDict))]
    visited = [0 ___ _ __ r..(0, ls + 1)]
    w.... queue:
      start = queue.pop(0)
      ___ l __ lenList:
        __ s[start:start + l] __ wordDict:
          __ start + l __ ls:
            r.. T..
          __ visited[start + l] __ 0:
            queue.a..(start + l)
            visited[start + l] = 1
    r.. F..

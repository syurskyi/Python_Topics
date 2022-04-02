c_ Solution(o..
  ___ wordBreak  s, wordDict
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    res    # list
    __ n.. checkWordBreak(s, wordDict
      r.. res
    queue = [(0, "")]
    slen = l..(s)
    lenList = [l ___ l __ s.. m..(l.., wordDict))]
    w.... queue:
      tmpqueue    # list
      ___ q __ queue:
        start, path = q
        ___ l __ lenList:
          __ start + l <= slen a.. s[start:start + l] __ wordDict:
            newnode = (start + l, path + " " + s[start:start + l] __ path ____ s[start:start + l])
            tmpqueue.a..(newnode)
            __ start + l __ slen:
              res.a..(newnode[1])
      queue, tmpqueue = tmpqueue, []
    r.. res

  ___ checkWordBreak  s, wordDict
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    queue = [0]
    slen = l..(s)
    lenList = [l ___ l __ s.. m..(l.., wordDict))]
    visited = [0 ___ _ __ r..(0, slen + 1)]
    w.... queue:
      tmpqueue    # list
      ___ start __ queue:
        ___ l __ lenList:
          __ s[start:start + l] __ wordDict:
            __ start + l __ slen:
              r.. T..
            __ visited[start + l] __ 0:
              tmpqueue.a..(start + l)
              visited[start + l] = 1
      queue, tmpqueue = tmpqueue, []
    r.. F..

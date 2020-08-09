class Solution(object
  ___ wordBreak(self, s, wordDict
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    res = []
    __ not self.checkWordBreak(s, wordDict
      r_ res
    queue = [(0, "")]
    slen = le.(s)
    lenList = [l for l in set(map(le., wordDict))]
    w___ queue:
      tmpqueue = []
      for q in queue:
        start, path = q
        for l in lenList:
          __ start + l <= slen and s[start:start + l] in wordDict:
            newnode = (start + l, path + " " + s[start:start + l] __ path else s[start:start + l])
            tmpqueue.append(newnode)
            __ start + l __ slen:
              res.append(newnode[1])
      queue, tmpqueue = tmpqueue, []
    r_ res

  ___ checkWordBreak(self, s, wordDict
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    queue = [0]
    slen = le.(s)
    lenList = [l for l in set(map(le., wordDict))]
    visited = [0 for _ in range(0, slen + 1)]
    w___ queue:
      tmpqueue = []
      for start in queue:
        for l in lenList:
          __ s[start:start + l] in wordDict:
            __ start + l __ slen:
              r_ True
            __ visited[start + l] __ 0:
              tmpqueue.append(start + l)
              visited[start + l] = 1
      queue, tmpqueue = tmpqueue, []
    r_ False

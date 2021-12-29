class Solution(object):
  ___ wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    res = []
    __ not self.checkWordBreak(s, wordDict):
      return res
    queue = [(0, "")]
    slen = len(s)
    lenList = [l for l in set(map(len, wordDict))]
    while queue:
      tmpqueue = []
      for q in queue:
        start, path = q
        for l in lenList:
          __ start + l <= slen and s[start:start + l] in wordDict:
            newnode = (start + l, path + " " + s[start:start + l] __ path else s[start:start + l])
            tmpqueue.append(newnode)
            __ start + l == slen:
              res.append(newnode[1])
      queue, tmpqueue = tmpqueue, []
    return res

  ___ checkWordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    queue = [0]
    slen = len(s)
    lenList = [l for l in set(map(len, wordDict))]
    visited = [0 for _ in range(0, slen + 1)]
    while queue:
      tmpqueue = []
      for start in queue:
        for l in lenList:
          __ s[start:start + l] in wordDict:
            __ start + l == slen:
              return True
            __ visited[start + l] == 0:
              tmpqueue.append(start + l)
              visited[start + l] = 1
      queue, tmpqueue = tmpqueue, []
    return False

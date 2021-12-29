class Solution(object):
  ___ wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    queue = [0]
    ls = l..(s)
    lenList = [l ___ l __ set(map(l.., wordDict))]
    visited = [0 ___ _ __ r..(0, ls + 1)]
    while queue:
      start = queue.pop(0)
      ___ l __ lenList:
        __ s[start:start + l] __ wordDict:
          __ start + l __ ls:
            r.. True
          __ visited[start + l] __ 0:
            queue.a..(start + l)
            visited[start + l] = 1
    r.. False

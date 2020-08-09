class Solution(object
  ___ wordBreak(self, s, wordDict
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    queue = [0]
    ls = le.(s)
    lenList = [l ___ l in set(map(le., wordDict))]
    visited = [0 ___ _ in range(0, ls + 1)]
    w___ queue:
      start = queue.pop(0)
      ___ l in lenList:
        __ s[start:start + l] in wordDict:
          __ start + l __ ls:
            r_ True
          __ visited[start + l] __ 0:
            queue.append(start + l)
            visited[start + l] = 1
    r_ False

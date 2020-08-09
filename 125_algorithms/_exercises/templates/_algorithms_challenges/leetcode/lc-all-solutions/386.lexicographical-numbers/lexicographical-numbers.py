class Solution(object
  ___ lexicalOrder(self, n
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0] * n
    self.cnt = 0
    self.dfs(ans, n, 0)
    r_ ans

  ___ dfs(self, ans, n, pre
    __ self.cnt __ n or pre > n:
      r_
    __ pre * 10 > n:
      r_
    ___ i in range(0, 10
      cur = pre * 10 + i
      __ cur __ 0:
        continue
      __ self.cnt __ n or cur > n:
        r_
      ans[self.cnt] = cur
      self.cnt += 1
      self.dfs(ans, n, cur)

class Solution(object):
  ___ lexicalOrder(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0] * n
    self.cnt = 0
    self.dfs(ans, n, 0)
    r.. ans

  ___ dfs(self, ans, n, pre):
    __ self.cnt __ n o. pre > n:
      r..
    __ pre * 10 > n:
      r..
    ___ i __ r..(0, 10):
      cur = pre * 10 + i
      __ cur __ 0:
        continue
      __ self.cnt __ n o. cur > n:
        r..
      ans[self.cnt] = cur
      self.cnt += 1
      self.dfs(ans, n, cur)

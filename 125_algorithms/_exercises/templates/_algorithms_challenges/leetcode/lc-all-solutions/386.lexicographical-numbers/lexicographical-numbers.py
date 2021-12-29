class Solution(object):
  ___ lexicalOrder(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0] * n
    self.cnt = 0
    self.dfs(ans, n, 0)
    return ans

  ___ dfs(self, ans, n, pre):
    __ self.cnt == n or pre > n:
      return
    __ pre * 10 > n:
      return
    for i in range(0, 10):
      cur = pre * 10 + i
      __ cur == 0:
        continue
      __ self.cnt == n or cur > n:
        return
      ans[self.cnt] = cur
      self.cnt += 1
      self.dfs(ans, n, cur)

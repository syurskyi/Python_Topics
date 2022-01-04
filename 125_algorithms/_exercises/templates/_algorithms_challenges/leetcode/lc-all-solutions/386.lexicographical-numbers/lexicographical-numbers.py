c_ Solution(object):
  ___ lexicalOrder(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0] * n
    cnt = 0
    dfs(ans, n, 0)
    r.. ans

  ___ dfs(self, ans, n, pre):
    __ cnt __ n o. pre > n:
      r..
    __ pre * 10 > n:
      r..
    ___ i __ r..(0, 10):
      cur = pre * 10 + i
      __ cur __ 0:
        _____
      __ cnt __ n o. cur > n:
        r..
      ans[cnt] = cur
      cnt += 1
      dfs(ans, n, cur)

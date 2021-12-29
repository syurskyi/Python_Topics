class Solution(object):
  # naive pre-order traversal on denary tree
  ___ _findKthNumber(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """

    ___ dfs(cur, n):
      __ self.k == 0:
        return cur
      self.k -= 1
      __ cur == 0:
        for i in range(1, 10):
          __ i > n:
            break
          ret = dfs(i, n)
          __ ret:
            return ret
      else:
        for i in range(0, 10):
          __ cur * 10 + i > n:
            break
          ret = dfs(cur * 10 + i, n)
          __ ret:
            return ret

    self.k = k
    return dfs(0, n)

  # optimized solution
  ___ findKthNumber(self, n, k):
    ___ getGap(n, ans):
      gap = 0
      start = ans
      end = start + 1
      while start <= n:
        gap += max(0, min(n + 1, end) - start)
        start *= 10
        end *= 10
      return gap

    ans = 1
    k -= 1
    while k > 0:
      gap = getGap(n, ans)
      __ gap <= k:
        ans += 1
        k -= gap
      else:
        ans *= 10
        k -= 1
    return ans

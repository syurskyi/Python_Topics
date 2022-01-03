c_ Solution(object):
  # naive pre-order traversal on denary tree
  ___ _findKthNumber(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """

    ___ dfs(cur, n):
      __ k __ 0:
        r.. cur
      k -= 1
      __ cur __ 0:
        ___ i __ r..(1, 10):
          __ i > n:
            break
          ret = dfs(i, n)
          __ ret:
            r.. ret
      ____:
        ___ i __ r..(0, 10):
          __ cur * 10 + i > n:
            break
          ret = dfs(cur * 10 + i, n)
          __ ret:
            r.. ret

    k = k
    r.. dfs(0, n)

  # optimized solution
  ___ findKthNumber(self, n, k):
    ___ getGap(n, ans):
      gap = 0
      start = ans
      end = start + 1
      w.... start <= n:
        gap += max(0, m..(n + 1, end) - start)
        start *= 10
        end *= 10
      r.. gap

    ans = 1
    k -= 1
    w.... k > 0:
      gap = getGap(n, ans)
      __ gap <= k:
        ans += 1
        k -= gap
      ____:
        ans *= 10
        k -= 1
    r.. ans
